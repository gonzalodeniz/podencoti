from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from podencoti.source_coverage import load_source_coverage
from podencoti.ti_classification import OpportunityCandidate, classify_opportunity, load_rule_set


BASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_DATA_PATH = BASE_DIR / "data" / "opportunities.json"


@dataclass(frozen=True)
class OpportunityRecord:
    id: str
    titulo: str
    descripcion: str
    organismo: str
    ubicacion: str
    procedimiento: str | None
    presupuesto: int | None
    fecha_limite: str
    estado: str
    fuente_oficial: str
    url_fuente_oficial: str
    cpvs: tuple[str, ...]


@dataclass(frozen=True)
class CatalogOpportunity:
    id: str
    titulo: str
    organismo: str
    ubicacion: str
    procedimiento: str | None
    presupuesto: int | None
    fecha_limite: str
    estado: str
    fuente_oficial: str
    url_fuente_oficial: str
    clasificacion_ti: str


def load_opportunity_records(path: Path = DEFAULT_DATA_PATH) -> tuple[str, list[OpportunityRecord]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = [
        OpportunityRecord(
            id=item["id"],
            titulo=item["titulo"],
            descripcion=item["descripcion"],
            organismo=item["organismo"],
            ubicacion=item["ubicacion"],
            procedimiento=item.get("procedimiento"),
            presupuesto=item.get("presupuesto"),
            fecha_limite=item["fecha_limite"],
            estado=item["estado"],
            fuente_oficial=item["fuente_oficial"],
            url_fuente_oficial=item["url_fuente_oficial"],
            cpvs=tuple(item.get("cpvs", [])),
        )
        for item in payload["opportunities"]
    ]
    return payload["referencia_funcional"], records


def build_catalog(path: Path = DEFAULT_DATA_PATH) -> dict[str, object]:
    reference, records = load_opportunity_records(path)
    rules = load_rule_set()
    mvp_sources = {source.nombre for source in load_source_coverage() if source.estado == "MVP"}

    opportunities: list[CatalogOpportunity] = []
    for record in records:
        if record.fuente_oficial not in mvp_sources:
            continue

        decision = classify_opportunity(
            OpportunityCandidate(
                titulo=record.titulo,
                descripcion=record.descripcion,
                cpvs=record.cpvs,
            ),
            rules,
        )
        if decision.clasificacion != "TI":
            continue

        opportunities.append(
            CatalogOpportunity(
                id=record.id,
                titulo=record.titulo,
                organismo=record.organismo,
                ubicacion=record.ubicacion,
                procedimiento=record.procedimiento,
                presupuesto=record.presupuesto,
                fecha_limite=record.fecha_limite,
                estado=record.estado,
                fuente_oficial=record.fuente_oficial,
                url_fuente_oficial=record.url_fuente_oficial,
                clasificacion_ti=decision.clasificacion,
            )
        )

    opportunities.sort(key=lambda opportunity: opportunity.fecha_limite)
    return {
        "referencia_funcional": reference,
        "cobertura_aplicada": sorted(mvp_sources),
        "total_registros_origen": len(records),
        "total_oportunidades_catalogo": len(opportunities),
        "oportunidades": [opportunity.__dict__ for opportunity in opportunities],
    }
