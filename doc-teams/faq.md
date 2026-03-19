# FAQ documental

## Publico objetivo
Personas usuarias internas, equipo tecnico y administracion que necesitan aclarar contradicciones entre vision, historial operativo y comportamiento real de `main`.

## La aplicacion esta disponible para arrancar en `main`?
Si. `make run` levanta un servidor local en `http://127.0.0.1:8000`.

## Entonces que entrega existe realmente hoy?
Existe una entrega minima de descubrimiento con catalogo inicial de oportunidades TI, ficha de detalle, cobertura inicial del MVP y clasificacion TI auditable.

## Que rutas estan verificadas?
- `/`
- `/api/oportunidades`
- `/oportunidades/<id>`
- `/api/oportunidades/<id>`
- `/cobertura-fuentes`
- `/api/fuentes`
- `/clasificacion-ti`
- `/api/clasificacion-ti`

## El producto ya tiene catalogo de oportunidades, filtros, alertas o pipeline?
En `main` si existen catalogo inicial y ficha de detalle. No existen todavia filtros, alertas ni pipeline, que siguen en backlog y roadmap de `product-manager/`.

## La ficha de detalle aplica rectificaciones o modificaciones oficiales?
Si. El detalle visible resuelve el ultimo dato oficial publicado cuando el expediente tiene actualizaciones versionadas en `data/opportunities.json`.

## Por que la metadata del paquete no menciona la clasificacion TI?
Porque `pyproject.toml` sigue describiendo el paquete solo como cobertura inicial de fuentes. Esa descripcion ha quedado por detras del estado real de `main`, que ya incluye catalogo inicial, ficha de detalle y la superficie auditable de `PB-006`.

## Se puede instalar algo util con `pip install -e .`?
Si. La instalacion editable deja operativa la aplicacion local y permite ejecutar las pruebas.

## Hay pruebas automatizadas disponibles?
Si. `PYTHONPATH=src python3 -m unittest discover -s tests -v` ejecuta 26 pruebas en esta revision.

## Se puede desplegar en produccion con lo que hay ahora?
No hay base documental suficiente para afirmarlo. Solo esta verificado el arranque local con `wsgiref`.

## Que debe tomarse hoy como fuente de verdad?
- Para reglas del repositorio y coordinacion: `AGENTS.md`
- Para vision y alcance funcional esperado: `product-manager/`
- Para el estado tecnico realmente observable en `main`: los manuales actuales de `doc-teams/` y el codigo versionado

## Que dependencias siguen abiertas?
- Implementar `PB-003`, `PB-004` y `PB-005`.
- Definir una estrategia de despliegue real cuando el alcance tecnico lo requiera.
- Actualizar la metadata del paquete si se quiere alinearla con la superficie visible actual.
