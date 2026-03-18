from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from podencoti.opportunity_catalog import build_catalog, load_opportunity_records


class OpportunityCatalogTests(unittest.TestCase):
    def test_load_opportunity_records_returns_versioned_seed_data(self) -> None:
        reference, records = load_opportunity_records()

        self.assertIn("PB-001", reference)
        self.assertEqual(5, len(records))
        self.assertEqual("govcan-backup-cloud-2026", records[0].id)

    def test_build_catalog_filters_to_mvp_ti_opportunities_only(self) -> None:
        catalog = build_catalog()

        self.assertEqual(5, catalog["total_registros_origen"])
        self.assertEqual(3, catalog["total_oportunidades_catalogo"])
        self.assertEqual(
            [
                "pcsp-cabildo-licencias-2026",
                "govcan-backup-cloud-2026",
                "cabildo-redes-2026",
            ],
            [item["id"] for item in catalog["oportunidades"]],
        )
        self.assertTrue(
            all(item["fuente_oficial"] != "Ayuntamientos con perfiles del contratante propios" for item in catalog["oportunidades"])
        )
        self.assertTrue(all(item["clasificacion_ti"] == "TI" for item in catalog["oportunidades"]))

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
