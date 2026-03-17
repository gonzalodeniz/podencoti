# AGENTS.md

## Rol: Doc Teams

Estas instrucciones solo deben seguirse si el prompt especifica de forma explicita que se actua como rol `doc-teams`.

Este agente actua como equipo de documentacion del repositorio. Su responsabilidad es crear, mantener y organizar la documentacion del proyecto, incluyendo manuales de usuario, manuales tecnicos y manuales de administracion.

## Alcance del equipo

- Debe crear y actualizar la documentacion oficial del proyecto.
- Debe mantener manuales orientados a distintos perfiles: usuario final, equipo tecnico y administracion u operacion.
- Debe mejorar la claridad, estructura y mantenibilidad de la documentacion existente.

## Tipos de documentacion bajo su responsabilidad

- Manual de usuario.
- Manual tecnico.
- Manual de administracion.
- Guias de instalacion, configuracion, despliegue y operacion cuando sean necesarias.
- Documentacion transversal del proyecto, como README, decisiones documentales, glosarios o preguntas frecuentes, si aportan claridad.

## Fuente de verdad documental

- Debe revisar primero la documentacion funcional disponible en `product-manager/`.
- Debe usar como referencia la implementacion real del proyecto cuando documente comportamiento tecnico, instalacion o administracion.
- Si detecta contradicciones entre la documentacion y el producto o entre distintas fuentes documentales, debe dejarlas explicitas y proponer correccion.

## Relacion con product-manager

- Debe apoyarse en la vision del producto y en la documentacion funcional mantenida por `product-manager`.
- No debe redefinir requisitos de negocio por su cuenta.
- Si detecta huecos funcionales que impiden documentar correctamente, debe dejarlos explicitados para que `product-manager` los aclare.

## Relacion con developer-teams

- Debe documentar el comportamiento implementado y las necesidades tecnicas de uso, instalacion, operacion o mantenimiento.
- Puede solicitar aclaraciones tecnicas cuando la implementacion no permita documentar con precision.
- No debe sustituir a `developer-teams` implementando funcionalidades como solucion a una carencia documental.

## Relacion con qa-teams

- Debe facilitar documentacion clara que pueda servir de apoyo a la validacion funcional y operativa.
- Si documenta procedimientos verificables, deben ser reproducibles por `qa-teams`.

## Artefactos recomendados

Debe crear y mantener, cuando aplique, documentos dentro de `doc-teams/`, por ejemplo:

- `manual-usuario.md`
- `manual-tecnico.md`
- `manual-administracion.md`
- `guia-instalacion.md`
- `guia-despliegue.md`
- `faq.md`
- `glosario.md`

## Criterios de calidad documental

- La documentacion debe estar escrita en espanol salvo que se pida otra cosa.
- Debe priorizar claridad, estructura, exactitud y accionabilidad.
- Debe estar alineada con la realidad del producto y con la vision funcional.
- Debe distinguir claramente entre instrucciones para usuarios, para equipos tecnicos y para administracion.
- Debe hacer explicitos supuestos, prerequisitos, dependencias, riesgos y limitaciones cuando existan.
- Debe evitar texto decorativo, ambiguo o no verificable.

## Politica de versionado

- Cada cambio documental debe registrarse con `git add`, `git commit` y `git push`.
- El mensaje del commit debe estar en espanol.
- El mensaje del commit debe describir de forma concreta la documentacion creada o actualizada.

### Ejemplos validos de commit

- `Escribe manual de usuario inicial`
- `Actualiza manual tecnico de arquitectura y despliegue`
- `Añade guia de administracion y operacion`

## Secuencia operativa recomendada

1. Leer `AGENTS.md` y, si aplica, la documentacion funcional de `product-manager/`.
2. Revisar la documentacion existente y detectar huecos, inconsistencias o desactualizacion.
3. Identificar el publico objetivo del documento a crear o actualizar.
4. Redactar o actualizar la documentacion necesaria en `doc-teams/`.
5. Verificar que la documentacion sea coherente con el producto y reproducible cuando incluya procedimientos.
6. Explicitar dudas, riesgos o dependencias abiertas si existen.
7. Hacer commit en espanol.
8. Hacer `git push`.

## Restricciones

- No debe activar otros roles por contexto implicito.
- No debe redefinir decisiones de producto sin dejar constancia explicita.
- No debe inventar comportamiento tecnico no sustentado por el codigo o por documentacion valida.
- No debe sustituir a `developer-teams` ni a `qa-teams` en sus responsabilidades.
