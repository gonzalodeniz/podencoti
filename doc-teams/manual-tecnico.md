# Manual tecnico

## Publico objetivo
Equipo tecnico que necesita conocer la implementacion actual de `main`, sus rutas verificables y los limites funcionales todavia abiertos.

## Resumen tecnico verificable
`PodencoTI` expone en `main` una aplicacion WSGI minima en Python con cuatro superficies funcionales verificables:

- `PB-001`: catalogo inicial de oportunidades TI.
- `PB-002`: ficha resumida de detalle por oportunidad visible.
- `PB-007`: cobertura inicial visible y verificable de fuentes.
- `PB-006`: regla de clasificacion TI auditable con ejemplos trazables.

La descripcion de paquete en `pyproject.toml` sigue mencionando solo cobertura de fuentes. Esa metadata ya no resume por completo el comportamiento observable de la rama.

## Artefactos tecnicos presentes
- Configuracion de paquete: `pyproject.toml`
- Automatizacion local: `Makefile`
- Aplicacion WSGI: `src/podencoti/app.py`
- Catalogo y detalle de oportunidades: `src/podencoti/opportunity_catalog.py`
- Carga de cobertura de fuentes: `src/podencoti/source_coverage.py`
- Carga y evaluacion de reglas TI: `src/podencoti/ti_classification.py`
- Datos versionados: `data/opportunities.json`, `data/source_coverage.json`, `data/ti_classification_rules.json`
- Suite tecnica: `tests/test_app.py`, `tests/test_opportunity_catalog.py`, `tests/test_source_coverage.py`, `tests/test_ti_classification.py`

## Superficie HTTP vigente
- `/`: vista HTML del catalogo inicial de oportunidades TI.
- `/api/oportunidades`: JSON del catalogo filtrado por cobertura MVP y clasificacion TI.
- `/oportunidades/<id>`: ficha HTML de detalle de una oportunidad visible.
- `/api/oportunidades/<id>`: JSON trazable de la ficha de detalle.
- `/cobertura-fuentes`: vista HTML de cobertura inicial del MVP.
- `/api/fuentes`: JSON con fuentes y resumen por estado.
- `/clasificacion-ti`: vista HTML de la regla TI auditable.
- `/api/clasificacion-ti`: JSON con reglas y ejemplos auditados.

La aplicacion devuelve `404 Not Found` para cualquier otra ruta no declarada.

### Campos visibles por superficie
- `/api/oportunidades`: devuelve `referencia_funcional`, `cobertura_aplicada`, `total_registros_origen`, `total_oportunidades_catalogo` y `oportunidades`.
- `/api/oportunidades/<id>`: devuelve datos criticos visibles, `actualizacion_oficial_mas_reciente` y `historial_actualizaciones`.
- `/api/fuentes`: devuelve `sources` y `summary`.
- `/api/clasificacion-ti`: devuelve `referencia_funcional`, `reglas` y `ejemplos_auditados`.

## Estructura tecnica
- [app.py](/opt/apps/podencoti/src/podencoti/app.py) centraliza el router WSGI, el renderizado HTML y las respuestas JSON.
- [opportunity_catalog.py](/opt/apps/podencoti/src/podencoti/opportunity_catalog.py) carga registros versionados, filtra por cobertura MVP, aplica la clasificacion TI y resuelve el ultimo dato oficial visible para ficha y catalogo.
- [source_coverage.py](/opt/apps/podencoti/src/podencoti/source_coverage.py) valida estados de cobertura permitidos (`MVP`, `Posterior`, `Por definir`) y resume conteos.
- [ti_classification.py](/opt/apps/podencoti/src/podencoti/ti_classification.py) normaliza texto, aplica reglas funcionales y audita ejemplos con tres salidas posibles: `TI`, `No TI` y `Caso frontera`.

## Verificacion reproducible
Desde la raiz del proyecto:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m podencoti.app
```

Resultado verificado en esta revision:
- 26 pruebas automatizadas en verde.
- Servidor local disponible en `http://127.0.0.1:8000`.

## Contradicciones explicitadas
- `pyproject.toml` sigue describiendo el paquete como una release centrada solo en cobertura de fuentes, aunque la rama ya expone catalogo, detalle y clasificacion TI auditable.
- La documentacion funcional de `product-manager/` describe backlog posterior valido, pero no debe leerse como contrato tecnico ya implementado para filtros, alertas o pipeline.

## Limitaciones tecnicas actuales
- No existe persistencia de usuario ni ingestion automatizada real de licitaciones; el catalogo se alimenta desde `data/opportunities.json`.
- No hay autenticacion, base de datos, tareas programadas ni integracion externa.
- No hay contrato de despliegue productivo versionado, mas alla del arranque local con `wsgiref`.

## Dependencias abiertas
- Implementar `PB-003`, `PB-004` y `PB-005` para evolucionar desde el descubrimiento inicial a un MVP mas operativo.
- Actualizar la metadata de paquete si se quiere que describa fielmente la superficie observable de `main`.
