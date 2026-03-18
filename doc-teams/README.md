# Documentacion de `doc-teams`

## Objetivo
Centralizar la documentacion oficial del proyecto `PodencoTI` diferenciando claramente entre audiencia usuaria, tecnica y de administracion.

## Estado documental de referencia
Fecha de revision: `2026-03-18`.

Esta carpeta documenta el estado real observable de la rama `main`. En esta revision se ha detectado que `main` conserva la vision de producto y artefactos funcionales, pero no contiene la implementacion fuente versionada que describian algunos manuales previos.

## Audiencias cubiertas
- Usuario final o stakeholder funcional: [manual-usuario.md](manual-usuario.md)
- Equipo tecnico: [manual-tecnico.md](manual-tecnico.md)
- Administracion u operacion: [manual-administracion.md](manual-administracion.md)
- Preparacion local reproducible: [guia-instalacion.md](guia-instalacion.md)
- Despliegue y publicacion operativa: [guia-despliegue.md](guia-despliegue.md)
- Preguntas frecuentes y contradicciones: [faq.md](faq.md)
- Terminologia transversal del proyecto: [glosario.md](glosario.md)

## Hallazgos principales de esta revision
- `product-manager/` describe una vision y un backlog futuros validos como fuente funcional, pero esas capacidades no estan implementadas en `main`.
- `main` no contiene ficheros fuente Python trazables bajo `src/podencoti/` ni pruebas versionadas bajo `tests/`; solo aparecen artefactos `__pycache__` no versionados en el arbol local.
- `make run` falla con `No module named podencoti.app`.
- `python3 -m unittest discover -s tests -v` no descubre pruebas y termina con `NO TESTS RAN`.
- El paquete editable puede instalarse porque existe la configuracion minima en `pyproject.toml`, pero esa instalacion no habilita la aplicacion descrita en los manuales anteriores.

## Dependencias y contradicciones abiertas
- La descripcion de la entrega tecnica en `README.md` de raiz no coincide con el contenido actual observable de `main`.
- `changelog/2026-03-17.md` y `changelog/2026-03-18.md` hablan de una implementacion y unas pruebas que no estan presentes en esta rama en el momento de la revision.
- La vision del producto mantiene capacidades futuras como catalogo, filtros, alertas y pipeline, pero no deben documentarse como comportamiento disponible.

## Criterio documental aplicado
- Se documenta solo lo verificable en `main`.
- Las contradicciones entre vision, historial y estado real se dejan explicitas.
- Cuando una capacidad pertenece al backlog pero no al producto actual, se marca como pendiente o no disponible.
