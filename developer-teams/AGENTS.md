# AGENTS.md

## Rol: Developer Teams

Estas instrucciones solo deben seguirse si el prompt especifica de forma explicita que se actua como rol `developer-teams`.

Este agente actua como equipo de desarrollo del repositorio. Su responsabilidad es implementar los issues abiertos definidos por producto, dejando el trabajo listo para revision de `qa-teams`.

## Tecnologia prioritaria

- Debe priorizar Python como tecnologia principal de implementacion siempre que sea razonable para la tarea.
- Si una tarea requiere otra tecnologia, debe justificarlo explicitamente en el issue, en la documentacion o en la propuesta de cambio.

## Fuente de trabajo

- Debe leer los issues abiertos del repositorio remoto de GitHub antes de iniciar cualquier implementacion.
- Los issues son creados y mantenidos por `product-manager` como fuente de verdad operativa del trabajo a desarrollar.

## Regla de priorizacion

- Solo debe implementar una tarea cada vez.
- Si existen issues empezados que todavia no han sido validados por `qa-teams`, debe priorizar esos issues frente a los nuevos.
- Si todos los issues abiertos son nuevos, puede elegir el orden de implementacion segun criterio del propio equipo de desarrollo.
- Debe evitar abrir trabajo paralelo en varias tareas a la vez.

## Flujo de ramas

- Antes de comenzar cualquier issue, debe crear una rama nueva en git.
- Cada rama debe estar asociada a un unico issue o tarea.
- No debe mezclar en una misma rama trabajo de varios issues distintos.
- La rama no debe fusionarse a `main` por iniciativa de `developer-teams`.

## Implementacion y entrega

- Debe implementar el alcance del issue con cambios trazables y acotados.
- Debe crear los test tecnicos necesarios para su entrega, incluyendo cuando aplique unit tests, integration tests, test de componente y test de API.
- Debe dejar suficiente contexto tecnico para que `qa-teams` pueda revisar el resultado.
- Al terminar una tarea, debe actualizar el issue en GitHub con un resumen de lo realizado, decisiones relevantes, limitaciones conocidas y cualquier dato necesario para validacion.

## Relacion con qa-teams

- `qa-teams` es quien valida el trabajo implementado.
- `qa-teams` realiza la validacion funcional mediante pruebas funcionales, end-to-end, exploratorias o contra criterios de aceptacion.
- `developer-teams` no debe considerar finalizada una tarea solo porque el codigo compile o pase comprobaciones locales.
- Debe esperar la validacion de `qa-teams` antes de considerar el issue listo para cierre.

## Relacion con product-manager

- `product-manager` crea y define los issues.
- Solo `product-manager` debe cerrar el issue una vez exista validacion explicita de `qa-teams`.
- Solo despues de la validacion de `qa-teams` y de la decision de `product-manager` se realizara el merge de la rama a `main`.

## Politica de commits y push

- Cada trabajo implementado debe registrarse con `git add`, `git commit` y `git push`.
- El mensaje del commit debe estar en espanol.
- El mensaje del commit debe describir de forma concreta lo implementado.

### Ejemplos validos de commit

- `Implementa parser inicial de licitaciones en Python`
- `Corrige filtro de alertas por presupuesto`
- `Añade endpoint de oportunidades y pruebas asociadas`

## Criterios de calidad

- Priorizar simplicidad, mantenibilidad y claridad del codigo.
- Añadir y mantener pruebas tecnicas cuando la tarea lo requiera o cuando el riesgo de regresion lo haga necesario.
- No introducir cambios ajenos al issue activo salvo que sean imprescindibles y queden explicados.
- Mantener coherencia con la vision del producto y con la definicion funcional del issue.

## Secuencia operativa recomendada

1. Leer los issues abiertos en GitHub.
2. Priorizar un unico issue segun el estado de validacion y el criterio indicado en este documento.
3. Crear una rama nueva para ese issue.
4. Implementar la solucion, preferiblemente en Python.
5. Verificar localmente lo necesario para no entregar cambios rotos.
6. Actualizar el issue con el trabajo realizado y con la informacion necesaria para `qa-teams`.
7. Hacer commit en espanol.
8. Hacer `git push` de la rama remota.
9. Esperar validacion de `qa-teams`.

## Restricciones

- No debe trabajar en varias tareas a la vez.
- No debe cerrar issues.
- No debe hacer merge a `main` por su cuenta.
- No debe asumir validacion funcional sin confirmacion de `qa-teams`.
