# AGENTS.md

## Proposito

Este archivo define las reglas globales del repositorio `podencoti` y aclara como deben activarse las instrucciones especificas de cada rol.

## Regla de activacion por rol

Las instrucciones de subdirectorios solo se aplicaran si el prompt lo indica de forma explicita.

- Solo se seguiran las instrucciones de `product-manager/AGENTS.md` si en el prompt se especifica que se actua como rol `product-manager`.
- Solo se seguiran las instrucciones de `developer-teams/AGENTS.md` si en el prompt se especifica que se actua como rol `developer-teams`.
- Solo se seguiran las instrucciones de `qa-teams/AGENTS.md` si en el prompt se especifica que se actua como rol `qa-teams`.

Si el prompt no activa uno de esos roles de forma explicita, no deben asumirse ni heredarse automaticamente sus instrucciones.

## Jerarquia de instrucciones del proyecto

1. Este `AGENTS.md` de raiz define las reglas generales del repositorio.
2. Los archivos `AGENTS.md` de cada area definen instrucciones especificas de ese rol.
3. Las instrucciones de area solo complementan a las de raiz cuando el rol ha sido activado expresamente en el prompt.

## Estructura actual del proyecto

```text
/
|-- AGENTS.md
|-- product-manager/
|   |-- AGENTS.md
|   `-- vision-product.md
|-- developer-teams/
`-- qa-teams/
```

### Descripcion de carpetas

- `product-manager/`: documentacion de producto, vision, backlog y artefactos funcionales.
- `developer-teams/`: espacio reservado para instrucciones, entregables y documentacion de desarrollo.
- `qa-teams/`: espacio reservado para instrucciones, criterios y evidencia de validacion de calidad.

## Vision del producto

`PodencoTI` es una plataforma para centralizar y detectar oportunidades de contratacion publica TI en Canarias. El producto busca evitar la busqueda manual en multiples portales, agregando licitaciones, clasificandolas como relevantes para tecnologia y enviando alertas tempranas para que empresas y profesionales puedan preparar ofertas con mas tiempo y mejor informacion.

### Problema que resuelve

- La contratacion publica canaria esta fragmentada en muchos portales y perfiles del contratante.
- La identificacion manual de licitaciones TI consume tiempo y produce errores u oportunidades perdidas.
- Los equipos comerciales y tecnicos llegan tarde a pliegos relevantes por falta de centralizacion y filtrado.

### Usuarios objetivo

- Pymes y startups tecnologicas.
- Consultoras e integradores TI.
- Profesionales autonomos del sector tecnologico.

### Capacidades clave esperadas

- Rastreo automatizado de fuentes oficiales de contratacion en Canarias.
- Clasificacion inteligente de oportunidades TI.
- Filtros por palabras clave, presupuesto, procedimiento y ubicacion.
- Extraccion de datos criticos de cada licitacion.
- Alertas y seguimiento de oportunidades en un pipeline de trabajo.

## Principios operativos recomendados

- Escribir en espanol salvo que el prompt indique lo contrario.
- Mantener trazabilidad entre vision, requisitos, desarrollo y validacion.
- No mezclar decisiones de producto con decisiones tecnicas sin dejar claras las dependencias.
- Priorizar documentos y entregables accionables frente a texto ambiguo o decorativo.
- Hacer explicitos supuestos, riesgos, dependencias y preguntas abiertas.

## Recomendaciones para evolucionar el repositorio

- Crear `developer-teams/AGENTS.md` para definir estandares de arquitectura, desarrollo, testing y despliegue.
- Crear `qa-teams/AGENTS.md` para definir estrategia de pruebas, criterios de aceptacion y politica de validacion.
- Mantener en `product-manager/` la fuente de verdad funcional y de negocio.
- Añadir documentacion transversal si el proyecto crece, por ejemplo `README.md`, decision records y convenciones de versionado.
- Evitar que un rol modifique artefactos propios de otro sin dejar constancia clara del motivo.

## Regla de seguridad organizativa

Ningun rol debe darse por activado por contexto implicito, por nombre de carpeta o por historial previo del chat. La activacion debe venir indicada expresamente en el prompt actual del usuario.
