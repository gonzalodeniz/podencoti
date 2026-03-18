# Roadmap de PodencoTI

## Criterios de planificacion
- Se prioriza validar primero la propuesta de valor central: centralizacion y filtrado de oportunidades TI.
- Las fases representan releases funcionales, no decisiones tecnicas de implementacion.
- Cada release debe dejar un resultado verificable por `qa-teams` y trazable a backlog e issues.

## Estado de referencia de la iteracion
- Fecha de corte documental: 2026-03-18.
- Estado confirmado: `PB-007` validado por `qa-teams` en la issue #1.
- Estado actual de trabajo tecnico: `PB-006` esta `no validado` en la issue #2 y debe corregirse en la rama `feat/pb-006-clasificacion-ti-auditable`.
- Siguiente recomendacion para `developer-teams`: resolver `PB-006` antes de construir `PB-001`.

## Release 0: Delimitacion funcional del MVP
- Objetivo: Cerrar ambiguedades criticas antes de la implementacion del catalogo.
- Alcance:
  - PB-007 Cobertura inicial de fuentes prioritarias.
- Criterios de salida:
  - Existe una lista visible y verificable de fuentes `MVP`, `Posterior` y `Por definir`.
  - La interfaz o configuracion no induce a pensar que existe cobertura total.
- Estado actual:
  - `PB-007` validado por `qa-teams`.
  - Permanece pendiente de cierre administrativo en GitHub hasta resolver su integracion final y seguimiento de rama.

## Release 1: Regla de relevancia y descubrimiento
- Objetivo: Permitir descubrir y evaluar oportunidades TI con criterio funcional consistente.
- Alcance:
  - PB-006 Reglas funcionales de clasificacion TI.
  - PB-001 Catalogo inicial de oportunidades TI de Canarias.
  - PB-002 Ficha de detalle de licitacion.
  - PB-003 Filtros funcionales de busqueda.
- Criterios de salida:
  - El catalogo solo muestra oportunidades alineadas con la cobertura y la regla TI.
  - El usuario puede localizar, revisar y filtrar oportunidades sin recorrer varios portales.
  - `qa-teams` puede verificar una muestra de inclusiones, exclusiones y campos visibles.
- Riesgo principal:
  - Que el equipo implemente un catalogo visible sin haber cerrado suficientemente los casos frontera de relevancia TI.
- Estado operativo actual:
  - `PB-006` no supero la validacion funcional de `qa-teams` porque la entrega no expuso las superficies prometidas para QA y la rama no integraba limpia con `main`.
  - `PB-001`, `PB-002` y `PB-003` no deben activarse mientras este bloqueo siga abierto.

## Release 2: Alertas y seguimiento operativo
- Objetivo: Convertir el descubrimiento en uso recurrente y gestion operativa.
- Alcance:
  - PB-004 Configuracion de alertas tempranas.
  - PB-005 Pipeline de seguimiento de oportunidades.
- Criterios de salida:
  - El usuario puede dejar configurados criterios persistentes de interes.
  - El usuario puede seguir oportunidades guardadas sin duplicados y con estados consistentes.
- Dependencia clave:
  - Requiere que Release 1 haya validado el valor del catalogo y de los filtros.
- Decision funcional vigente:
  - Las alertas del MVP registran coincidencias de forma interna; la notificacion saliente queda fuera de esta release.
  - El pipeline del MVP es individual por usuario; la colaboracion por empresa queda para una release posterior.

## Release 3: Medicion y aprendizaje
- Objetivo: Mejorar precision, cobertura y priorizacion apoyandose en indicadores.
- Alcance:
  - PB-008 Medicion basica de valor del producto.
  - Ajustes de priorizacion segun feedback y resultados de QA.
- Criterios de salida:
  - Existen definiciones de KPI utilizables para decidir siguientes inversiones funcionales.
  - El roadmap posterior puede justificarse con evidencia y no solo con intuicion.

## Dependencias abiertas de roadmap
- Confirmar el tratamiento funcional de expedientes mixtos donde TI no es el componente principal.
- Revalidar `PB-006` con una superficie funcional observable y una rama sincronizada con `main` antes de iniciar el catalogo del Release 1.

## Decision operativa para la siguiente iteracion
- La issue activa que debe continuar `developer-teams` es la #2, asociada a `PB-006`.
- La correccion debe mantenerse en la misma rama `feat/pb-006-clasificacion-ti-auditable` mientras el alcance siga siendo el mismo.
- No se recomienda abrir implementacion de `PB-001` sin haber fijado antes la regla funcional auditable de relevancia TI y sin haber superado validacion funcional de QA.
