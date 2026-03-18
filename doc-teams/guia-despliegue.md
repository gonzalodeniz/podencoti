# Guia de despliegue

## Publico objetivo
Persona responsable de publicar, exponer o poner en servicio `PodencoTI` en un entorno distinto al local.

## Estado actual del despliegue
En la rama `main` no existe una aplicacion desplegable de forma reproducible. Esta guia documenta esa limitacion para evitar procedimientos de despliegue ficticios o no verificables.

## Verificacion previa obligatoria
Antes de intentar cualquier despliegue, confirma desde la raiz del proyecto:

```bash
cd /opt/apps/podencoti
python3 -m pip install -e .
make run
make test
```

## Resultado esperado en esta revision
- `python3 -m pip install -e .` termina correctamente.
- `make run` falla con `No module named podencoti.app`.
- `make test` falla porque no se descubren pruebas y termina con `NO TESTS RAN`.

## Conclusion operativa
No debe intentarse un despliegue en servidor, contenedor, servicio gestionado o entorno de preproduccion con el contenido actual de `main`, porque falta la aplicacion versionada que deberia exponerse.

## Elementos de despliegue no disponibles
- comando de arranque funcional
- fichero de configuracion de entorno
- servicio `systemd`
- definicion de contenedor
- proxy inverso o configuracion de publicacion
- procedimiento de rollback
- healthcheck

## Dependencias abiertas para habilitar despliegue
- Reintegrar en `main` la aplicacion ejecutable que el `README.md` de raiz describe.
- Reincorporar pruebas versionadas para validar una entrega antes de publicarla.
- Alinear `README.md`, `Makefile` y esta guia cuando exista una superficie de ejecucion real.

## Riesgos
- Cualquier intento de documentar despliegue real hoy seria especulativo.
- Prometer una publicacion operativa con el estado actual de `main` generaria una expectativa falsa frente a producto, QA y administracion.
