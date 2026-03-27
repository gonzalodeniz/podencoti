from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from podencoti.opportunity_catalog import CatalogFilters, build_catalog, build_opportunity_detail, load_opportunity_records


def _atom_entry(
    *,
    contract_folder_id: str,
    updated: str,
    title: str,
    summary: str,
    organization: str,
    cpv: str,
    country_subentity_code: str,
    country_subentity: str,
    amount: str,
    deadline: str,
    status: str = "PUB",
    procedure: str = "1",
) -> str:
    return f"""
  <entry xmlns="http://www.w3.org/2005/Atom"
         xmlns:cac="urn:dgpe:names:draft:codice:schema:xsd:CommonAggregateComponents-2"
         xmlns:cbc="urn:dgpe:names:draft:codice:schema:xsd:CommonBasicComponents-2"
         xmlns:cac-place-ext="urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonAggregateComponents-2"
         xmlns:cbc-place-ext="urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonBasicComponents-2">
    <id>{contract_folder_id}</id>
    <link href="https://contrataciondelestado.es/detalle/{contract_folder_id}" />
    <summary>{summary}</summary>
    <title>{title}</title>
    <updated>{updated}</updated>
    <cac-place-ext:ContractFolderStatus>
      <cbc:ContractFolderID>{contract_folder_id}</cbc:ContractFolderID>
      <cbc-place-ext:ContractFolderStatusCode>{status}</cbc-place-ext:ContractFolderStatusCode>
      <cac-place-ext:LocatedContractingParty>
        <cac:Party>
          <cac:PartyName>
            <cbc:Name>{organization}</cbc:Name>
          </cac:PartyName>
        </cac:Party>
        <cac-place-ext:ParentLocatedParty>
          <cac:PartyName>
            <cbc:Name>Canarias</cbc:Name>
          </cac:PartyName>
        </cac-place-ext:ParentLocatedParty>
      </cac-place-ext:LocatedContractingParty>
      <cac:ProcurementProject>
        <cbc:Name>{title}</cbc:Name>
        <cac:BudgetAmount>
          <cbc:TotalAmount>{amount}</cbc:TotalAmount>
        </cac:BudgetAmount>
        <cac:RequiredCommodityClassification>
          <cbc:ItemClassificationCode>{cpv}</cbc:ItemClassificationCode>
        </cac:RequiredCommodityClassification>
        <cac:RealizedLocation>
          <cbc:CountrySubentity>{country_subentity}</cbc:CountrySubentity>
          <cbc:CountrySubentityCode>{country_subentity_code}</cbc:CountrySubentityCode>
        </cac:RealizedLocation>
      </cac:ProcurementProject>
      <cac:TenderingProcess>
        <cbc:ProcedureCode>{procedure}</cbc:ProcedureCode>
        <cac:TenderSubmissionDeadlinePeriod>
          <cbc:EndDate>{deadline}</cbc:EndDate>
        </cac:TenderSubmissionDeadlinePeriod>
      </cac:TenderingProcess>
    </cac-place-ext:ContractFolderStatus>
  </entry>
"""


def _atom_feed(*entries: str) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<feed xmlns="http://www.w3.org/2005/Atom">'
        + "".join(entries)
        + "</feed>\n"
    )


class OpportunityCatalogTests(unittest.TestCase):
    def test_load_opportunity_records_returns_consolidated_atom_seed_data(self) -> None:
        reference, records = load_opportunity_records()

        self.assertEqual("PB-011", reference)
        self.assertEqual(14, len(records))
        self.assertEqual("pao-0120-2021", records[0].id)
        self.assertTrue(all(record.fichero_origen_atom for record in records))

    def test_build_catalog_returns_consolidated_canarias_ti_opportunities(self) -> None:
        catalog = build_catalog()

        self.assertEqual(14, catalog["total_registros_origen"])
        self.assertEqual(14, catalog["total_oportunidades_catalogo"])
        self.assertEqual(
            [
                "pao-0120-2021",
                "fue-96-2023",
                "2565-2024",
                "ser-2025-0000122082",
                "iter-2025-14",
                "9518-2025",
                "42-16-25s",
                "expte-001-2026",
                "ace-13-2026",
                "2026-800",
                "25sv22",
                "sum-2026-0000004656",
                "ser-2026-0000004892",
                "sct2024000193",
            ],
            [item["id"] for item in catalog["oportunidades"]],
        )
        self.assertEqual(5, len(catalog["cobertura_aplicada"]))
        self.assertTrue(all(item["clasificacion_ti"] == "TI" for item in catalog["oportunidades"]))

    def test_build_opportunity_detail_includes_atom_source_filename(self) -> None:
        detail = build_opportunity_detail("ser-2025-0000122082")

        assert detail is not None
        self.assertEqual("2026-03-23", detail["fecha_publicacion_oficial"])
        self.assertEqual("2025-12-10", detail["fecha_limite"])
        self.assertEqual(919422, detail["presupuesto"])
        self.assertEqual("Resuelta", detail["estado"])
        self.assertEqual(
            "licitacionesPerfilesContratanteCompleto3_20260323_190607_3.atom",
            detail["fichero_origen_atom"],
        )

    def test_build_opportunity_detail_returns_none_for_non_visible_record(self) -> None:
        self.assertIsNone(build_opportunity_detail("govcan-teleco-mixto-2026"))

    def test_build_catalog_can_return_empty_catalog(self) -> None:
        payload = {
            "referencia_funcional": "PB-001",
            "opportunities": [
                {
                    "id": "solo-no-ti",
                    "titulo": "Compra de mobiliario de oficina",
                    "descripcion": "Mesas, sillas y armarios.",
                    "organismo": "Gobierno de Canarias",
                    "ubicacion": "Canarias",
                    "procedimiento": "Abierto",
                    "presupuesto": 12000,
                    "fecha_publicacion_oficial": "2026-04-01",
                    "fecha_limite": "2026-05-01",
                    "estado": "Abierta",
                    "fuente_oficial": "Gobierno de Canarias",
                    "url_fuente_oficial": "https://www.gobiernodecanarias.org/perfil_del_contratante/",
                    "cpvs": ["39130000"],
                }
            ],
        }

        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "opportunities.json"
            path.write_text(json.dumps(payload), encoding="utf-8")

            catalog = build_catalog(path)

        self.assertEqual(1, catalog["total_registros_origen"])
        self.assertEqual(0, catalog["total_oportunidades_catalogo"])
        self.assertEqual([], catalog["oportunidades"])

    def test_build_catalog_applies_combined_filters(self) -> None:
        catalog = build_catalog(
            filters=CatalogFilters(
                palabra_clave="incidencias",
                presupuesto_min=90000,
                presupuesto_max=120000,
                procedimiento="Abierto",
                ubicacion="Canarias",
            )
        )

        self.assertEqual(14, catalog["total_oportunidades_visibles"])
        self.assertEqual(1, catalog["total_oportunidades_catalogo"])
        self.assertEqual(["ser-2026-0000004892"], [item["id"] for item in catalog["oportunidades"]])
        self.assertEqual(
            {
                "palabra_clave": "incidencias",
                "presupuesto_min": 90000,
                "presupuesto_max": 120000,
                "procedimiento": "Abierto",
                "ubicacion": "Canarias",
            },
            catalog["filtros_activos"],
        )

    def test_build_catalog_excludes_records_without_known_budget_when_range_is_requested(self) -> None:
        catalog = build_catalog(filters=CatalogFilters(presupuesto_max=100000))

        self.assertEqual(
            [
                "fue-96-2023",
                "42-16-25s",
                "ace-13-2026",
                "2026-800",
                "25sv22",
                "ser-2026-0000004892",
            ],
            [item["id"] for item in catalog["oportunidades"]],
        )

    def test_build_catalog_flags_invalid_budget_range_without_treating_it_as_empty_result(self) -> None:
        catalog = build_catalog(filters=CatalogFilters(presupuesto_min=120000, presupuesto_max=90000))

        self.assertEqual(
            "El presupuesto mínimo no puede ser mayor que el presupuesto máximo. "
            "Revisa el rango antes de aplicar los filtros.",
            catalog["error_validacion"],
        )
        self.assertEqual(14, catalog["total_oportunidades_catalogo"])
        self.assertEqual(14, len(catalog["oportunidades"]))

    def test_load_opportunity_records_consolidates_latest_snapshot_from_atom_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            data_dir = Path(tmp_dir)
            older_feed = _atom_feed(
                _atom_entry(
                    contract_folder_id="EXP-01/2026",
                    updated="2026-03-20T10:00:00+01:00",
                    title="Servicio TI inicial",
                    summary="Version inicial del expediente.",
                    organization="Cabildo de Tenerife",
                    cpv="72222300",
                    country_subentity_code="ES709",
                    country_subentity="Tenerife",
                    amount="100000",
                    deadline="2026-04-10",
                )
            )
            newer_feed = _atom_feed(
                _atom_entry(
                    contract_folder_id="EXP-01/2026",
                    updated="2026-03-22T12:00:00+01:00",
                    title="Servicio TI consolidado",
                    summary="Version mas reciente del expediente.",
                    organization="Cabildo de Tenerife",
                    cpv="72222300",
                    country_subentity_code="ES709",
                    country_subentity="Tenerife",
                    amount="125000",
                    deadline="2026-04-15",
                )
            )
            (data_dir / "snapshot_1.atom").write_text(older_feed, encoding="utf-8")
            (data_dir / "snapshot_2.atom").write_text(newer_feed, encoding="utf-8")

            reference, records = load_opportunity_records(data_dir)

        self.assertEqual("PB-011", reference)
        self.assertEqual(1, len(records))
        self.assertEqual("exp-01-2026", records[0].id)
        self.assertEqual("Servicio TI consolidado", records[0].titulo)
        self.assertEqual(125000, records[0].presupuesto)
        self.assertEqual("snapshot_2.atom", records[0].fichero_origen_atom)
