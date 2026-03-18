from __future__ import annotations

import json
from html import escape
from wsgiref.simple_server import make_server

from podencoti.source_coverage import load_source_coverage, summary_by_status
from podencoti.ti_classification import audit_examples, load_rule_set


def _html_response() -> str:
    sources = load_source_coverage()
    summary = summary_by_status(sources)
    rows = "\n".join(
        (
            "<tr>"
            f'<td data-label="Fuente oficial">{escape(source.nombre)}</td>'
            f'<td data-label="Categoría">{escape(source.categoria)}</td>'
            f'<td data-label="Estado">{escape(source.estado)}</td>'
            f'<td data-label="Alcance">{escape(source.alcance)}</td>'
            f'<td data-label="Justificación funcional">{escape(source.descripcion)}</td>'
            f'<td data-label="Trazabilidad">{escape(source.referencia_funcional)}</td>'
            "</tr>"
        )
        for source in sources
    )

    return f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>PodencoTI | Cobertura inicial del MVP</title>
    <style>
      :root {{
        color-scheme: light;
        --bg: #f4efe6;
        --card: #fffdf9;
        --ink: #1c2733;
        --muted: #5f6b76;
        --line: #d7c7af;
        --accent: #a7502b;
        --accent-soft: #f4d8c7;
      }}
      body {{
        margin: 0;
        font-family: Georgia, "Times New Roman", serif;
        background:
          radial-gradient(circle at top right, #f8dfca 0, transparent 22rem),
          linear-gradient(180deg, #f9f4ec 0%, var(--bg) 100%);
        color: var(--ink);
      }}
      main {{
        max-width: 1100px;
        margin: 0 auto;
        padding: 3rem 1.5rem 4rem;
      }}
      .hero, .panel {{
        background: color-mix(in srgb, var(--card) 94%, white);
        border: 1px solid var(--line);
        border-radius: 20px;
        box-shadow: 0 18px 40px rgb(28 39 51 / 0.08);
      }}
      .hero {{
        padding: 2rem;
        margin-bottom: 1.5rem;
      }}
      h1, h2 {{
        margin-top: 0;
      }}
      p {{
        line-height: 1.6;
      }}
      .muted {{
        color: var(--muted);
      }}
      .summary {{
        display: grid;
        gap: 1rem;
        grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
        margin: 1.5rem 0;
      }}
      .metric {{
        background: var(--accent-soft);
        border-radius: 16px;
        padding: 1rem;
      }}
      .metric strong {{
        display: block;
        font-size: 2rem;
        color: var(--accent);
      }}
      .panel {{
        overflow: hidden;
      }}
      table {{
        width: 100%;
        border-collapse: collapse;
      }}
      th, td {{
        text-align: left;
        padding: 0.9rem 1rem;
        border-bottom: 1px solid var(--line);
        vertical-align: top;
      }}
      th {{
        background: #f6ebdf;
      }}
      tr:last-child td {{
        border-bottom: 0;
      }}
      .note {{
        margin-top: 1rem;
        padding: 1rem 1.25rem;
        border-left: 4px solid var(--accent);
        background: #fff4ea;
      }}
      @media (max-width: 720px) {{
        table, thead, tbody, th, td, tr {{
          display: block;
        }}
        thead {{
          display: none;
        }}
        td {{
          padding-top: 0.35rem;
          padding-bottom: 0.35rem;
        }}
        td::before {{
          content: attr(data-label);
          display: block;
          color: var(--muted);
          font-size: 0.85rem;
          text-transform: uppercase;
          letter-spacing: 0.04em;
          margin-bottom: 0.2rem;
        }}
      }}
    </style>
  </head>
  <body>
    <main>
      <section class="hero">
        <p class="muted">Release 0 · PB-007 · Cobertura visible y verificable</p>
        <h1>Cobertura inicial de fuentes oficiales del MVP</h1>
        <p>
          PodencoTI no comunica cobertura total del ecosistema canario en esta entrega.
          Esta vista delimita qué fuentes oficiales entran en el MVP, cuáles quedan para una fase posterior
          y cuáles siguen pendientes de decisión funcional.
        </p>
        <div class="summary">
          <article class="metric"><strong>{summary["MVP"]}</strong>Fuentes objetivo en MVP</article>
          <article class="metric"><strong>{summary["Posterior"]}</strong>Fuentes planificadas después del MVP</article>
          <article class="metric"><strong>{summary["Por definir"]}</strong>Fuentes pendientes de decisión</article>
        </div>
        <p class="muted">Los datos se cargan desde una configuración versionada en <code>data/source_coverage.json</code>.</p>
      </section>

      <section class="panel">
        <table>
          <thead>
            <tr>
              <th>Fuente oficial</th>
              <th>Categoría</th>
              <th>Estado</th>
              <th>Alcance</th>
              <th>Justificación funcional</th>
              <th>Trazabilidad</th>
            </tr>
          </thead>
          <tbody>
            {rows}
          </tbody>
        </table>
      </section>

      <p class="note">
        Referencia funcional alineada con <code>product-manager/refinamiento-funcional.md</code> y <code>product-manager/roadmap.md</code>.
        Esta cobertura sirve de base para el catálogo inicial del MVP sin inducir una expectativa de exhaustividad.
      </p>
    </main>
  </body>
</html>"""


def _classification_html_response() -> str:
    rules = load_rule_set()
    audited_examples = audit_examples(rules)
    example_rows = "\n".join(
        (
            "<tr>"
            f'<td data-label="Ejemplo">{escape(item["titulo"])}</td>'
            f'<td data-label="CPVs">{escape(", ".join(item["cpvs"]) or "No informado")}</td>'
            f'<td data-label="Esperado">{escape(item["clasificacion_esperada"])}</td>'
            f'<td data-label="Obtenido">{escape(item["clasificacion_obtenida"])}</td>'
            f'<td data-label="Coincidencias">{escape(", ".join(item["coincidencias_inclusion"] + item["coincidencias_exclusion"] + item["coincidencias_frontera"]) or "Sin coincidencias")}</td>'
            f'<td data-label="Justificación">{escape(item["motivo_regla"])}</td>'
            "</tr>"
        )
        for item in audited_examples
    )

    def _list_items(items: tuple[str, ...]) -> str:
        return "".join(f"<li>{escape(item)}</li>" for item in items)

    return f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>PodencoTI | Reglas auditables de clasificación TI</title>
    <style>
      :root {{
        color-scheme: light;
        --bg: #f3f0e8;
        --card: #fffdf8;
        --ink: #20303a;
        --muted: #60707a;
        --line: #d5ccb6;
        --accent: #2f6c61;
        --accent-soft: #d8ece7;
      }}
      body {{
        margin: 0;
        font-family: Georgia, "Times New Roman", serif;
        background:
          radial-gradient(circle at top left, #dcefe9 0, transparent 20rem),
          linear-gradient(180deg, #f9f7f1 0%, var(--bg) 100%);
        color: var(--ink);
      }}
      main {{
        max-width: 1180px;
        margin: 0 auto;
        padding: 3rem 1.5rem 4rem;
      }}
      .hero, .panel, .rules {{
        background: color-mix(in srgb, var(--card) 95%, white);
        border: 1px solid var(--line);
        border-radius: 20px;
        box-shadow: 0 18px 40px rgb(32 48 58 / 0.08);
      }}
      .hero, .rules {{
        padding: 2rem;
        margin-bottom: 1.5rem;
      }}
      .rule-grid {{
        display: grid;
        gap: 1rem;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      }}
      .rule-card {{
        background: var(--accent-soft);
        border-radius: 16px;
        padding: 1rem 1.1rem;
      }}
      .muted {{
        color: var(--muted);
      }}
      ul {{
        margin: 0.5rem 0 0;
        padding-left: 1.2rem;
      }}
      table {{
        width: 100%;
        border-collapse: collapse;
      }}
      th, td {{
        text-align: left;
        padding: 0.9rem 1rem;
        border-bottom: 1px solid var(--line);
        vertical-align: top;
      }}
      th {{
        background: #ebf4f1;
      }}
      .panel {{
        overflow: hidden;
      }}
      .note {{
        margin-top: 1rem;
        padding: 1rem 1.25rem;
        border-left: 4px solid var(--accent);
        background: #edf7f4;
      }}
      a {{
        color: var(--accent);
      }}
      @media (max-width: 720px) {{
        table, thead, tbody, th, td, tr {{
          display: block;
        }}
        thead {{
          display: none;
        }}
        td::before {{
          content: attr(data-label);
          display: block;
          color: var(--muted);
          font-size: 0.85rem;
          text-transform: uppercase;
          letter-spacing: 0.04em;
          margin-bottom: 0.2rem;
        }}
      }}
    </style>
  </head>
  <body>
    <main>
      <section class="hero">
        <p class="muted">Release 0 · PB-006 · Reglas funcionales auditables</p>
        <h1>Clasificación TI auditable para oportunidades del catálogo</h1>
        <p>
          Esta entrega fija un criterio funcional verificable antes de construir el catálogo visible.
          La clasificación distingue oportunidades <strong>TI</strong>, <strong>No TI</strong> y <strong>Caso frontera</strong>
          para que QA y producto puedan revisar ejemplos representativos con trazabilidad explícita.
        </p>
        <p class="muted">Referencia funcional: <code>{escape(rules.referencia_funcional)}</code></p>
      </section>

      <section class="rules">
        <div class="rule-grid">
          <article class="rule-card">
            <h2>Inclusión por palabras clave</h2>
            <ul>{_list_items(rules.inclusion_palabras_clave)}</ul>
          </article>
          <article class="rule-card">
            <h2>Inclusión por necesidad explícita</h2>
            <ul>{_list_items(rules.inclusion_necesidades_explicitas)}</ul>
          </article>
          <article class="rule-card">
            <h2>Exclusiones relevantes</h2>
            <ul>{_list_items(rules.exclusion_palabras_clave)}</ul>
          </article>
          <article class="rule-card">
            <h2>Casos frontera a revisar</h2>
            <ul>{_list_items(rules.frontera_palabras_clave)}</ul>
          </article>
        </div>
        <p class="note">
          Los CPVs tecnológicos admitidos se validan por prefijo en <code>data/ti_classification_rules.json</code>.
          La salida JSON en <a href="/api/clasificacion-ti">/api/clasificacion-ti</a> permite contrastar ejemplos y coincidencias.
        </p>
      </section>

      <section class="panel">
        <table>
          <thead>
            <tr>
              <th>Ejemplo</th>
              <th>CPVs</th>
              <th>Esperado</th>
              <th>Obtenido</th>
              <th>Coincidencias</th>
              <th>Justificación</th>
            </tr>
          </thead>
          <tbody>
            {example_rows}
          </tbody>
        </table>
      </section>
    </main>
  </body>
</html>"""


def application(environ, start_response):
    path = environ.get("PATH_INFO", "/")

    if path == "/api/clasificacion-ti":
        rules = load_rule_set()
        payload = {
            "referencia_funcional": rules.referencia_funcional,
            "reglas": {
                "inclusion_palabras_clave": list(rules.inclusion_palabras_clave),
                "inclusion_cpv_prefixes": list(rules.inclusion_cpv_prefixes),
                "inclusion_necesidades_explicitas": list(rules.inclusion_necesidades_explicitas),
                "exclusion_palabras_clave": list(rules.exclusion_palabras_clave),
                "casos_frontera_palabras_clave": list(rules.frontera_palabras_clave),
            },
            "ejemplos_auditados": audit_examples(rules),
        }
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers = [
            ("Content-Type", "application/json; charset=utf-8"),
            ("Content-Length", str(len(body))),
        ]
        start_response("200 OK", headers)
        return [body]

    if path == "/clasificacion-ti":
        body = _classification_html_response().encode("utf-8")
        headers = [
            ("Content-Type", "text/html; charset=utf-8"),
            ("Content-Length", str(len(body))),
        ]
        start_response("200 OK", headers)
        return [body]

    if path == "/api/fuentes":
        sources = load_source_coverage()
        payload = {
            "sources": [source.__dict__ for source in sources],
            "summary": summary_by_status(sources),
        }
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers = [
            ("Content-Type", "application/json; charset=utf-8"),
            ("Content-Length", str(len(body))),
        ]
        start_response("200 OK", headers)
        return [body]

    if path == "/":
        body = _html_response().encode("utf-8")
        headers = [
            ("Content-Type", "text/html; charset=utf-8"),
            ("Content-Length", str(len(body))),
        ]
        start_response("200 OK", headers)
        return [body]

    body = b"No encontrado"
    start_response(
        "404 Not Found",
        [
            ("Content-Type", "text/plain; charset=utf-8"),
            ("Content-Length", str(len(body))),
        ],
    )
    return [body]


def main() -> None:
    host = "127.0.0.1"
    port = 8000
    with make_server(host, port, application) as httpd:
        print(f"Servidor disponible en http://{host}:{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
