---
name: rayo-x
description: Rayo X a un competidor. Analiza la biblioteca de anuncios de Meta de una página, rankea sus creativos ganadores por duplicados y días y entrega reporte, carpeta de ganadores y swipe con títulos, copies y guiones adaptados al mercado destino, siguiendo el Manual de Rayo X de Fer Guerrero. Usar cuando el usuario diga "rayo X a [competidor/link]", "hacele un rayo X a...", "con qué anuncios salgo a testear [oferta]", "analizá los anuncios de [página]" o pida modelar los creativos de la candidata A de una caza.
---

# Rayo X a un competidor

El método completo está en el manual. **Leelo entero antes de empezar cada rayo X** y seguí las secciones 3 a 10 en orden, sin saltear el barrido completo:

`SegundoCerebro(Fer:FORMULAEINFOPRODUCTOS/RAW/manuales/manual-rayo-x.md`

Es el paso siguiente de la skill `cazar`: la caza elige la oferta y el rayo X define con qué anuncios salir a testearla. Si el competidor viene de una caza, tomá los datos del reporte de esa caza en `OUTPUTS/`.

Contexto del método en la wiki: `hooks.md`, `guiones-de-video-ads.md`, `angulos-publicitarios.md`, `testeo-de-creativos.md` y `renovacion-de-creativos.md`.

## Antes de empezar, preguntá siempre

1. **El mercado destino y el idioma de salida.** Ese idioma manda sobre las transcripciones, los títulos, los copies y los guiones. No asumas español.
2. **La oferta propia**: producto, promesa, precio y mecanismo con nombre. Si no la da, hacé el barrido igual y dejá los guiones como "pendientes".

## Reglas que no se negocian

- **Barrido completo antes de elegir:** todas las tarjetas cargadas, con el total contrastado contra "~N resultados".
- **El ranking es duplicados ↓, después días ↓, después impresiones ↓.** Se rescatan de 10 a 20 ganadores. Un creativo viejo sin duplicados no es ganador.
- **Impresiones:** solo si la biblioteca las muestra. Nunca las estimes.
- **Pedí OK antes de bajar cualquier video**, en un solo mensaje con nombre, origen y tamaño en MB de cada uno.
- **Los videos bajados son para estudiar.** Nunca se suben a una cuenta publicitaria ni se reusan como b-roll.
- Nada de compras de prueba ni quizzes con datos reales sin OK explícito.
- Lo que no se pudo ver va como **"no confirmado"**.
- **Compliance:** nada de promesas de ingresos ni médicas en títulos, copies ni guiones, aunque el competidor las haga.
- **Modelar, no copiar:** se mantienen formato, duración, tipo de gancho, estructura, dolor y CTA. El texto, las caras, la voz, el footage y la marca son propios.

## Herramientas en este entorno

- **Biblioteca de anuncios:** primero `ads_library_search` del conector oficial de Meta (buscalo con ToolSearch). Si no está, usá el navegador en `facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=<id>`. EspiAd (`mcp__ESPIAad__ver_oferta`) sirve para conseguir el link a la Biblioteca de una oferta ya cazada, pero no reemplaza el barrido por página.
- **Video:** `ffmpeg` está instalado.
- **Transcripción:** en vez de `whisper-cli`, usá Whisper de Python, que ya está instalado: `whisper <archivo>.wav --model medium --language pt --output_format srt --fp16 False`, o `import whisper` en un script. Para los textos en pantalla está Tesseract (`pytesseract`) con español, portugués e inglés.

## Dónde guardar

Todo va a `SegundoCerebro(Fer:FORMULAEINFOPRODUCTOS/CREATIVOS/swipe/<YYYY-MM-DD>-rayo-x-<competidor>/`:

- `reporte.md` — reporte A (sección 11).
- `indice.md` + `videos/` — carpeta de ganadores B, numerados por ranking (`01-<gancho-corto>.mp4`…).
- `swipe.md` — swipe C, en el idioma destino.
- `transcripciones.md` — D, solo si se pidieron.

Es salida de trabajo, no conocimiento: no toques `WIKI/` ni `RAW/` desde acá. Si aparece algo para la wiki (un ángulo o una regla nueva), avisá para procesarlo por la vía normal.
