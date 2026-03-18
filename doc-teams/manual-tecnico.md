# Manual tecnico

## Publico objetivo
Equipo tecnico que necesita conocer el estado real de `main`, sus limites y las contradicciones documentales detectadas.

## Resumen tecnico verificable
El repositorio contiene configuracion minima de paquete Python y documentacion de roles, pero no expone en `main` una implementacion fuente versionada de la aplicacion que describian versiones previas de este manual.

## Artefactos tecnicos presentes
- Configuracion de paquete: `pyproject.toml`
- Automatizacion minima local: `Makefile`
- Estructura de codigo esperada pero sin fuentes versionadas: `src/podencoti/`
- Estructura de pruebas esperada pero sin pruebas versionadas: `tests/`

## Evidencia observada en esta revision
- `git ls-files src tests` no devuelve ficheros versionados.
- `src/podencoti/` contiene solo artefactos `__pycache__` en el arbol local.
- No existe `data/source_coverage.json` en la rama revisada.
- `python3 -m pip install -e .` finaliza correctamente.
- `python3 - <<'PY' ... import podencoti ... PY` permite importar el paquete de espacio de nombres `podencoti`, pero `import podencoti.app` falla con `ModuleNotFoundError`.
- `python3 -m unittest discover -s tests -v` termina con `NO TESTS RAN`.
- `make test` falla por ese mismo motivo.
- `make run` falla con `No module named podencoti.app`.

## Contradicciones explicitadas
- El `README.md` de raiz describe una aplicacion HTTP local y una API JSON que no pueden ejecutarse en `main`.
- La version anterior de este manual tecnico describia archivos como `src/podencoti/app.py`, `src/podencoti/source_coverage.py` y `data/source_coverage.json`; esos artefactos no estan presentes en la revision actual.
- `changelog/2026-03-17.md` y parte del contexto historico mencionan una implementacion inicial visible del MVP, pero esa implementacion no es trazable desde el contenido actual de la rama revisada.

## Implicaciones tecnicas
- No es posible documentar contrato HTTP, arquitectura WSGI, modelo de datos ni pruebas funcionales como comportamiento vigente.
- La rama `main` conserva la definicion funcional del producto, pero no la materializacion tecnica necesaria para ejecucion local o validacion de QA.
- La instalacion editable del paquete no debe confundirse con disponibilidad de una aplicacion runnable.

## Dependencias abiertas
- Recuperar o reintegrar en `main` la implementacion fuente correspondiente a la entrega mencionada en `README.md` y `changelog/`.
- Reincorporar pruebas versionadas para que `make test` y `python3 -m unittest` sean reproducibles.
- Revisar y alinear `README.md` de raiz cuando exista una fuente tecnica confirmada o, en su defecto, cuando se decida que la referencia a la app ya no debe mantenerse.
