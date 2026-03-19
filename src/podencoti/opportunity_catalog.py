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
    solvencia_tecnica: str | None
    criterios_adjudicacion: tuple[str, ...]
    fuente_oficial: str
    url_fuente_oficial: str
    cpvs: tuple[str, ...]
    actualizaciones_oficiales: tuple[dict[str, object], ...]


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


@dataclass(frozen=True)
class OpportunityDetail:
    id: str
    titulo: str
    descripcion: str
    organismo: str
    ubicacion: str
    procedimiento: str | None
    presupuesto: int | None
    fecha_limite: str
    estado: str
    solvencia_tecnica: str | None
    criterios_adjudicacion: tuple[str, ...]
    fuente_oficial: str
    url_fuente_oficial: str
    clasificacion_ti: str
    referencia_funcional: str
    actualizacion_oficial_mas_reciente: dict[str, object] | None
    historial_actualizaciones: tuple[dict[str, object], ...]


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
            solvencia_tecnica=item.get("solvencia_tecnica"),
            criterios_adjudicacion=tuple(item.get("criterios_adjudicacion") or ()),
            fuente_oficial=item["fuente_oficial"],
            url_fuente_oficial=item["url_fuente_oficial"],
            cpvs=tuple(item.get("cpvs", [])),
            actualizaciones_oficiales=tuple(item.get("actualizaciones_oficiales", [])),
        )
        for item in payload["opportunities"]
    ]
    return payload["referencia_funcional"], records


def _sorted_updates(record: OpportunityRecord) -> tuple[dict[str, object], ...]:
    return tuple(
        sorted(
            record.actualizaciones_oficiales,
            key=lambda item: str(item.get("fecha_publicacion", "")),
        )
    )


def _resolve_latest_visible_snapshot(record: OpportunityRecord) -> dict[str, object]:
    snapshot: dict[str, object] = {
        "procedimiento": record.procedimiento,
        "presupuesto": record.presupuesto,
        "fecha_limite": record.fecha_limite,
        "estado": record.estado,
        "solvencia_tecnica": record.solvencia_tecnica,
        "criterios_adjudicacion": list(record.criterios_adjudicacion),
    }
    for update in _sorted_updates(record):
        for field in (
            "procedimiento",
            "presupuesto",
            "fecha_limite",
            "estado",
            "solvencia_tecnica",
            "criterios_adjudicacion",
        ):
            if field in update:
                value = update[field]
                if field == "criterios_adjudicacion":
                    snapshot[field] = list(value or [])
                else:
                    snapshot[field] = value
    return snapshot


def _classify_record(record: OpportunityRecord, rules) -> str:
    decision = classify_opportunity(
        OpportunityCandidate(
            titulo=record.titulo,
            descripcion=record.descripcion,
            cpvs=record.cpvs,
        ),
        rules,
    )
    return decision.clasificacion


def build_opportunity_detail(
    opportunity_id: str,
    path: Path = DEFAULT_DATA_PATH,
) -> dict[str, object] | None:
    reference, records = load_opportunity_records(path)
    rules = load_rule_set()
    mvp_sources = {source.nombre for source in load_source_coverage() if source.estado == "MVP"}

    for record in records:
        if record.id != opportunity_id:
            continue
        if record.fuente_oficial not in mvp_sources:
            return None

        classification = _classify_record(record, rules)
        if classification != "TI":
            return None

        snapshot = _resolve_latest_visible_snapshot(record)
        updates = _sorted_updates(record)
        detail = OpportunityDetail(
            id=record.id,
            titulo=record.titulo,
            descripcion=record.descripcion,
            organismo=record.organismo,
            ubicacion=record.ubicacion,
            procedimiento=snapshot["procedimiento"],
            presupuesto=snapshot["presupuesto"],
            fecha_limite=str(snapshot["fecha_limite"]),
            estado=str(snapshot["estado"]),
            solvencia_tecnica=snapshot["solvencia_tecnica"],
            criterios_adjudicacion=tuple(snapshot["criterios_adjudicacion"]),
            fuente_oficial=record.fuente_oficial,
            url_fuente_oficial=record.url_fuente_oficial,
            clasificacion_ti=classification,
            referencia_funcional=reference,
            actualizacion_oficial_mas_reciente=(dict(updates[-1]) if updates else None),
            historial_actualizaciones=tuple(dict(item) for item in updates),
        )
        return detail.__dict__

    return None


def build_catalog(path: Path = DEFAULT_DATA_PATH) -> dict[str, object]:
    reference, records = load_opportunity_records(path)
    rules = load_rule_set()
    mvp_sources = {source.nombre for source in load_source_coverage() if source.estado == "MVP"}

    opportunities: list[CatalogOpportunity] = []
    for record in records:
        if record.fuente_oficial not in mvp_sources:
            continue

        classification = _classify_record(record, rules)
        if classification != "TI":
            continue
        snapshot = _resolve_latest_visible_snapshot(record)

        opportunities.append(
            CatalogOpportunity(
                id=record.id,
                titulo=record.titulo,
                organismo=record.organismo,
                ubicacion=record.ubicacion,
                procedimiento=snapshot["procedimiento"],
                presupuesto=snapshot["presupuesto"],
                fecha_limite=str(snapshot["fecha_limite"]),
                estado=str(snapshot["estado"]),
                fuente_oficial=record.fuente_oficial,
                url_fuente_oficial=record.url_fuente_oficial,
                clasificacion_ti=classification,
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
