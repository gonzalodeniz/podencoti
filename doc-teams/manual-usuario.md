# Manual de usuario

## Publico objetivo
Usuario final, stakeholder funcional o persona de negocio que necesita entender que puede utilizar hoy en la rama `main`.

## Estado actual para usuario
En la rama `main` no hay una interfaz de usuario ejecutable ni un catalogo navegable de oportunidades TI verificable desde el repositorio actual.

## Que si existe hoy
- Vision de producto y alcance funcional en `product-manager/`.
- Reglas de coordinacion del repositorio en `AGENTS.md`.
- Documentacion operativa y tecnica en `doc-teams/`.

## Que no esta disponible hoy en `main`
- Catalogo de oportunidades TI.
- Ficha de detalle de licitacion.
- Filtros por palabra clave, presupuesto, procedimiento o ubicacion.
- Alertas tempranas.
- Pipeline de seguimiento.
- Vista HTML o API ejecutable de cobertura de fuentes.

## Como interpretar la documentacion funcional
Los documentos de `product-manager/` describen la vision, el backlog y el comportamiento esperado del producto a medio plazo. No deben interpretarse como funcionalidades ya disponibles para uso final en esta rama.

## Limitaciones relevantes para usuario
- `README.md` de raiz menciona una entrega tecnica minima y rutas HTTP locales, pero ese comportamiento no es reproducible en el estado actual de `main`.
- Si se intenta arrancar la aplicacion con `make run`, el repositorio devuelve un error porque no existe el modulo `podencoti.app` en esta rama.

## Recomendacion de uso
Hasta que `developer-teams` vuelva a integrar una entrega ejecutable en `main`, la documentacion util para usuario o stakeholder es la de vision, backlog y roadmap, no un manual de operacion del producto.
