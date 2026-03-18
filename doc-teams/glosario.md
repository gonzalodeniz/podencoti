# Glosario

## Publico objetivo
Usuario interno del proyecto que necesita interpretar de forma consistente la terminologia funcional, tecnica y operativa de `PodencoTI`.

## Terminos del producto
- `PodencoTI`: plataforma orientada a centralizar y detectar oportunidades de contratacion publica TI en Canarias.
- `MVP`: alcance minimo inicial del producto; segun la documentacion funcional vigente, debe comunicarse como cobertura inicial priorizada y no como cobertura total.
- `Oportunidad TI`: licitacion o expediente considerado relevante para tecnologia conforme a las reglas funcionales vigentes de clasificacion.
- `Cobertura funcional`: conjunto de fuentes y capacidades que el producto declara cubrir de forma observable y verificable.
- `Fuente oficial`: portal, perfil del contratante u origen institucional desde el que se obtiene informacion de contratacion publica.
- `Pipeline`: seguimiento del estado de trabajo de una oportunidad por parte del usuario; sigue siendo capacidad planificada, no disponible en `main`.
- `Alerta temprana`: mecanismo para registrar o notificar nuevas oportunidades compatibles con criterios del usuario; sigue siendo capacidad planificada, no disponible en `main`.

## Terminos operativos del repositorio
- `main`: rama de referencia para trabajo funcional, documental y de coordinacion no tecnica.
- `Estado operativo`: etiqueta comun entre equipos para una issue (`nuevo`, `en desarrollo`, `listo para qa`, `no validado`, `validado`, `cerrado`).
- `Impacto documental`: indicador usado por `developer-teams` para señalar que una entrega validada requiere actualizacion documental.
- `Trazabilidad`: relacion explicita entre vision, backlog, historias, casos de uso, implementacion, validacion y documentacion.

## Terminos de esta revision documental
- `Estado real observable`: comportamiento que puede comprobarse en la rama revisada mediante ficheros versionados y comandos reproducibles.
- `Contradiccion documental`: diferencia entre lo que una fuente del repositorio afirma y lo que puede verificarse realmente en `main`.
- `No disponible en main`: capacidad descrita por vision o backlog que no debe documentarse como funcionalidad utilizable hoy.

## Contradicciones clave asociadas al glosario
- `Entrega tecnica actual`: expresion usada en el `README.md` de raiz para describir una app local y pruebas que no son verificables con los ficheros versionados actuales.
- `Validado`: estado que aparece en parte del historial operativo para entregas tecnicas cuyas fuentes no estan presentes en `main`; debe distinguirse del estado realmente desplegable o ejecutable de la rama.
