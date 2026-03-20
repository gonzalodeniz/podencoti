# Manual de usuario

## Publico objetivo
Stakeholder funcional, producto o persona usuaria interna que necesita entender que se puede consultar hoy en la rama `main`.

## Estado actual para usuario
La rama `main` expone una entrega minima navegable orientada a descubrimiento inicial y validacion funcional temprana, no un producto de uso final completo.

## Que si existe hoy
- Un catalogo inicial de oportunidades TI en `/`.
- Una API JSON del catalogo en `/api/oportunidades`.
- Una ficha HTML de detalle por oportunidad en `/oportunidades/<id>`.
- Una API JSON del detalle en `/api/oportunidades/<id>`.
- Una vista HTML de cobertura inicial del MVP en `/cobertura-fuentes`.
- Una salida JSON de esa cobertura en `/api/fuentes`.
- Una vista HTML de clasificacion TI auditable en `/clasificacion-ti`.
- Una salida JSON de reglas y ejemplos auditados en `/api/clasificacion-ti`.

## Que permite validar esta entrega
- Que el catalogo visible solo publica oportunidades clasificadas como TI y dentro de la cobertura MVP.
- Que cada oportunidad mantiene organismo, ubicacion, estado oficial, fecha limite y referencia a su fuente oficial.
- Que la ficha de detalle refleja el ultimo dato oficial visible cuando existe una rectificacion o modificacion publicada.
- Que la cobertura inicial del MVP esta acotada a fuentes `MVP`, `Posterior` y `Por definir`.
- Que la regla de relevancia TI muestra inclusiones, exclusiones y casos frontera auditables.

## Recorrido recomendado para una revision funcional
1. Abre `/` y revisa el listado de oportunidades visibles.
2. Entra en una ficha desde el titulo de una oportunidad para comprobar presupuesto, fecha limite, estado oficial y enlace a la fuente.
3. Abre `/cobertura-fuentes` para confirmar que la cobertura comunicada sigue siendo parcial y priorizada.
4. Abre `/clasificacion-ti` para entender por que una oportunidad entra, se excluye o queda como caso frontera.

## Que no esta disponible hoy en `main`
- Filtros por palabra clave, presupuesto, procedimiento o ubicacion.
- Alertas tempranas.
- Pipeline de seguimiento.
- Gestion de usuarios o autenticacion.

## Como interpretar la documentacion funcional
Los documentos de `product-manager/` siguen siendo la fuente funcional para vision, backlog, historias y casos de uso. Deben leerse como alcance esperado del producto, no como evidencia de que esas funcionalidades ya esten disponibles en esta entrega.

## Limitaciones relevantes para usuario
- Las superficies actuales permiten descubrimiento inicial y revision de detalle, pero no cubren todavia filtrado, seguimiento operativo ni alertas.
- La cobertura visible sigue siendo parcial y no debe interpretarse como rastreo exhaustivo de todo el ecosistema canario.
- La metadata tecnica del paquete sigue describiendo una release anterior mas limitada que la visible hoy en `main`.
- El `changelog` del proyecto puede mencionar trabajo ya validado por otros equipos en ramas tecnicas; eso no implica que la funcionalidad este disponible para uso en `main`.

## Recomendacion de uso
Para demos o revision funcional temprana, utiliza el catalogo en `/`, la ficha de detalle de una oportunidad visible y, como apoyo, las vistas de cobertura y clasificacion TI. Para capacidades de negocio pendientes, toma como referencia `product-manager/roadmap.md` y `product-manager/product-backlog.md`.
