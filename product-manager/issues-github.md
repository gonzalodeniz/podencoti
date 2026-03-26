# Borradores de issues de GitHub

## Estado actual
- La issue de `PB-010` ya fue creada en GitHub como issue #10 el 2026-03-26.

## Issue creada: Navegacion principal responsive con menu lateral de iconos

Titulo sugerido: `[product-manager] PB-010 Navegacion principal responsive con menu lateral de iconos`

Backlog: PB-010 Navegacion principal responsive con menu lateral de iconos
Historia de usuario: HU-10 Navegar por los modulos principales desde una estructura comun adaptable al ancho de la ventana
Caso de uso: CU-10 Navegar por los modulos principales con una estructura responsive
Criterios de aceptacion:
1. En resoluciones amplias la aplicacion muestra un menu lateral izquierdo persistente con iconos en disposicion vertical para las opciones principales.
2. La opcion activa de navegacion queda resaltada de forma visible y consistente entre vistas.
3. La interfaz adapta la navegacion y el contenido al ancho disponible sin solapamientos ni necesidad de scroll horizontal estructural.
4. En anchos reducidos la navegacion principal sigue siendo accesible mediante una variante responsive coherente con la estructura general de la aplicacion.
5. Las opciones aun no disponibles no deben presentarse como rutas plenamente operativas; si se muestran, deben quedar marcadas de forma explicita como `proximamente`.
6. La entrega no debe degradar las superficies ya validadas de catalogo, detalle, filtros y alertas.
Dependencias: PB-001, PB-002, PB-003 y coordinacion de visibilidad con PB-004 y PB-005 segun estado real de implementacion
Estado operativo: nuevo

Contexto funcional:
- El producto necesita una base de navegacion comun para sostener el crecimiento de catalogo, alertas, pipeline y futuras vistas sin obligar al usuario a reaprender la estructura en cada pantalla.
- El patron deseado es una navegacion principal situada a la izquierda con iconos en vertical, priorizando claridad, ubicacion rapida y escalabilidad de modulos.
- La adaptacion al ancho de ventana es un requisito de producto, no una mejora cosmetica opcional.

Alcance esperado para `developer-teams`:
- Definir una estructura de layout comun reutilizable para las pantallas principales.
- Incorporar el menu lateral izquierdo de iconos en vistas donde aplique.
- Resolver el comportamiento responsive de la navegacion y del contenedor principal.
- Mantener coherencia visual de estado activo, foco y jerarquia de contenido.
- Evitar exponer como disponibles modulos que aun no tengan una superficie funcional utilizable.

Tareas sugeridas:
- Inventariar las opciones principales reales que ya existen en la aplicacion y distinguirlas de las previstas.
- Proponer la estructura base de navegacion y su correspondencia con las vistas actuales.
- Implementar el layout comun y aplicar la navegacion a las pantallas principales existentes.
- Definir y aplicar el comportamiento responsive para anchos reducidos.
- Revisar regresiones visuales y funcionales sobre catalogo, detalle, filtros y alertas.
- Añadir evidencia de verificacion tecnica y capturas o descripcion verificable para `qa-teams`.

Preguntas abiertas que `developer-teams` debe aclarar si bloquean:
- Que opciones deben aparecer desde el primer dia como modulos principales visibles y cuales deben quedar ocultas o marcadas como `proximamente`.
- Si alguna vista actual requiere ajuste de contenido adicional para encajar en el nuevo layout sin perder legibilidad.
