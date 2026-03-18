# Manual de administracion y operacion

## Publico objetivo
Persona responsable de preparar el entorno local, verificar el estado operativo de `main` y mantener expectativas correctas sobre lo que realmente puede ponerse en marcha.

## Alcance operativo actual
En la revision actual de `main` no hay un servicio de aplicacion arrancable desde el repositorio. Este manual documenta la verificacion de esa limitacion y los controles minimos para no asumir una operacion inexistente.

## Prerequisitos
- Acceso al arbol del proyecto en `/opt/apps/podencoti`.
- `python3` compatible con `>=3.12`.
- `make` si se quieren usar los objetivos definidos en `Makefile`.

## Verificaciones reproducibles
Desde la raiz del proyecto:

```bash
cd /opt/apps/podencoti
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
make run
make test
```

## Resultado esperado en esta revision
- La instalacion editable termina correctamente.
- La ejecucion de pruebas devuelve `NO TESTS RAN`.
- `make test` falla porque no hay pruebas descubiertas.
- `make run` falla porque no existe el modulo `podencoti.app`.

## Operacion no disponible
No existe en `main`:
- servicio HTTP arrancable
- unidad `systemd`
- supervisor de procesos
- contenedor
- healthcheck
- procedimiento de despliegue reproducible

## Riesgos operativos
- Comunicar que el producto esta desplegable desde `main` induciria a error.
- Usar como referencia manuales anteriores sin esta correccion puede provocar intentos fallidos de arranque, validacion o soporte.
- La ausencia de fuentes y pruebas versionadas impide una administracion tecnica normal del producto.

## Dependencias abiertas para administracion
- Reintegracion de la aplicacion ejecutable en `main`.
- Reposicion de pruebas versionadas y datos operativos si siguen formando parte de la entrega objetivo.
- Alineacion posterior entre `README.md`, `Makefile` y los procedimientos de operacion cuando la implementacion vuelva a estar disponible.
