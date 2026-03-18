# FAQ documental

## Publico objetivo
Personas usuarias internas, equipo tecnico y administracion que necesitan aclarar contradicciones entre la vision del producto, la documentacion previa y el estado real de `main`.

## La aplicacion esta disponible para arrancar en `main`?
No. `make run` falla porque no existe `podencoti.app` en la rama revisada.

## Entonces por que `README.md` habla de una vista HTML y una API JSON?
Porque el repositorio conserva referencias documentales e historicas a una entrega tecnica previa. Esa referencia no coincide con el contenido actual verificable de `main`.

## El historial operativo del 2026-03-18 no indica que habia mas funcionalidad?
Si, pero ese historial entra en contradiccion con los ficheros versionados visibles hoy en `main`. Como `doc-teams`, la referencia documental valida para comportamiento actual es lo reproducible desde la rama, no lo que el historial dice haber existido.

## El producto ya tiene catalogo de oportunidades, filtros, alertas o pipeline?
No en `main`. Esas capacidades existen en la vision, backlog, historias y casos de uso de `product-manager/`, pero no como funcionalidad observable en la rama revisada.

## Se puede instalar algo util con `pip install -e .`?
Si. La instalacion editable del paquete funciona, pero solo deja preparado el paquete base; no habilita una aplicacion ejecutable.

## Hay pruebas automatizadas disponibles?
No pruebas versionadas en `main`. El descubrimiento con `python3 -m unittest discover -s tests -v` termina con `NO TESTS RAN`.

## Que debe tomarse hoy como fuente de verdad?
- Para reglas del repositorio y coordinacion: `AGENTS.md`
- Para vision y alcance funcional esperado: `product-manager/`
- Para el estado tecnico realmente observable en `main`: los manuales actuales de `doc-teams/`

## Que dependencias siguen abiertas?
- Reintegrar en `main` la implementacion tecnica que el repositorio dice haber tenido.
- Reincorporar pruebas versionadas.
- Alinear `README.md` de raiz con el estado real o con la siguiente entrega integrada.
