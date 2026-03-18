# Guia de instalacion

## Publico objetivo
Equipo tecnico o persona de soporte que necesita preparar el repositorio en local y comprobar de forma reproducible el estado actual de `main`.

## Objetivo real de esta guia
Esta guia no instala una aplicacion funcional completa de `PodencoTI` porque esa implementacion no esta presente en la rama revisada. Su objetivo es dejar preparado el entorno y verificar exactamente hasta donde llega hoy el repositorio.

## Prerequisitos
- Sistema con `python3`.
- Version compatible: `3.12` o superior.
- Acceso local al repositorio en `/opt/apps/podencoti`.

## Preparacion local
1. Situa la terminal en la raiz del proyecto:

```bash
cd /opt/apps/podencoti
```

2. Crea un entorno virtual si quieres aislar la instalacion:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instala el paquete en modo editable:

```bash
python3 -m pip install -e .
```

## Verificaciones posteriores
1. Comprueba el descubrimiento de pruebas:

```bash
python3 -m unittest discover -s tests -v
```

Resultado esperado en esta revision:
- `NO TESTS RAN`

2. Comprueba el objetivo de pruebas del `Makefile`:

```bash
make test
```

Resultado esperado en esta revision:
- fallo por ausencia de pruebas descubiertas

3. Comprueba el objetivo de arranque:

```bash
make run
```

Resultado esperado en esta revision:
- error `No module named podencoti.app`

## Que queda instalado realmente
- Metadatos del paquete `podencoti`.
- Enlace editable al repositorio local.

## Que no queda disponible
- Aplicacion HTTP ejecutable.
- API local.
- Datos de cobertura versionados dentro de `data/`.
- Suite de pruebas versionada y ejecutable.

## Limitaciones y dependencias abiertas
- El `Makefile` y el `README.md` describen una aplicacion que no esta presente en `main`.
- Si se recupera la implementacion tecnica en una revision posterior, esta guia debe actualizarse para reflejar los comandos reales de arranque, prueba y verificacion manual.
