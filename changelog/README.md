# Guia de formato del changelog

## Objetivo
Usar una referencia vigente y unica para registrar actividad diaria de cualquier rol sin depender de ejemplos historicos que puedan haber quedado desfasados por reglas posteriores.

## Reglas de formato
- Usar un fichero diario con nombre `yyyy-mm-dd.md`.
- Anadir siempre la nueva entrada al final del fichero.
- Crear una seccion identificada por rol.
- Incluir al comienzo de cada nueva entrada la linea `Hora: HH:MM:SS UTC`.
- Si el mismo rol registra actividad dos veces en el mismo dia, debe crear dos secciones separadas.
- No reordenar ni intercalar bloques previos de otros roles.

## Plantilla minima

```text
# Changelog 2026-03-18

## agile-coach

Hora: 18:45:00 UTC

- Accion concreta realizada.
- Riesgo, ajuste o resultado relevante.
```

## Nota sobre ficheros historicos
Los ficheros previos a la introduccion de la hora obligatoria por entrada pueden no seguir este formato completo. Deben tomarse como referencia solo para el nivel de detalle, no para contradecir las reglas vigentes.
