from __future__ import annotations

import json
import unittest

from podencoti.app import application


def invoke_app(path: str) -> tuple[str, dict[str, str], bytes]:
    captured: dict[str, object] = {}

    def start_response(status: str, headers: list[tuple[str, str]]) -> None:
        captured["status"] = status
        captured["headers"] = dict(headers)

    body = b"".join(application({"PATH_INFO": path}, start_response))
    return captured["status"], captured["headers"], body


class ApplicationTests(unittest.TestCase):
    def test_root_renders_visible_coverage_page(self) -> None:
        status, headers, body = invoke_app("/")
        html = body.decode("utf-8")

        self.assertEqual("200 OK", status)
        self.assertEqual("text/html; charset=utf-8", headers["Content-Type"])
        self.assertIn("Cobertura inicial de fuentes oficiales del MVP", html)
        self.assertIn("Gobierno de Canarias", html)
        self.assertIn("data/source_coverage.json", html)

    def test_api_returns_configured_source_coverage(self) -> None:
        status, headers, body = invoke_app("/api/fuentes")
        payload = json.loads(body)

        self.assertEqual("200 OK", status)
        self.assertEqual("application/json; charset=utf-8", headers["Content-Type"])
        self.assertEqual(6, len(payload["sources"]))
        self.assertEqual({"MVP": 3, "Posterior": 2, "Por definir": 1}, payload["summary"])

    def test_unknown_path_returns_404(self) -> None:
        status, headers, body = invoke_app("/desconocido")

        self.assertEqual("404 Not Found", status)
        self.assertEqual("text/plain; charset=utf-8", headers["Content-Type"])
        self.assertEqual("No encontrado", body.decode("utf-8"))
