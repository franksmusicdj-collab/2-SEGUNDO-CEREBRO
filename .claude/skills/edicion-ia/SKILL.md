---
name: edicion-ia
description: Editor de creativos con IA. Genera, monta, corrige, revisa o dobla anuncios y VSL con avatar IA (UGC, voz en off + b-roll, VSL post-pago, traducción de ganadores) siguiendo el Manual de Edición IA de Fer Guerrero: voz fija, clip de prueba, regenerar solo los malos, cortes por alineación forzada y energía, control final. Usar cuando el usuario pida "generá el anuncio", "montá este video", "producí los guiones del rayo X", "VSL con avatar", "doblá este ganador", "revisá este MP4" o diga "seguí el Manual de Edición IA".
---

# Edición IA

El método completo está en el manual. **Leelo entero antes de generar, recortar, montar o entregar cualquier video** y seguilo al pie de la letra:

`SegundoCerebro(Fer:FORMULAEINFOPRODUCTOS/RAW/manuales/manual-edicion-ia.md`

Va después de `rayo-x`: el rayo X entrega los guiones del swipe y esta skill los produce. Para las VSL post-pago también se apoya en `entregables` (lo que el guion promete tiene que estar en el producto). Contexto en la wiki: `ugc-y-video-generativo.md`, `guiones-de-video-ads.md`, `hooks.md` y `embudo-vsl-post-pago.md`.

## Antes de gastar un peso

1. Elegí la ruta con la tabla de la sección 2 del manual y **decí el costo estimado antes de generar**. Los precios del manual son de octubre de 2026: verificalos antes de presupuestar.
2. **Un clip de prueba**, mostralo y esperá OK antes del lote.
3. **Una sola voz fija por video**, elegida según el país, con una muestra de referencia (`reference_voice`), nunca con una descripción repetida.

## Reglas de oro (resumen; mandan las del manual)

- Cero SFX. Solo música baja con ducking.
- Bordes de cada clip por **alineación forzada contra el guion**, nunca por Whisper. Pausas internas por **energía del audio**.
- **Regenerar solo los clips malos**, con la lista exacta. Nunca regenerar porque falló una descarga: re-bajar con `curl -C -`.
- Guardar el ID de cada tarea apenas se manda.
- Recortar cada clip al mínimo entre audio y video. Re-renderizar antes de analizar.
- **Control final completo** (sección 11) antes de entregar, y decir qué no se verificó. Mirar el video entero no lo reemplaza ningún script: si no lo pudiste escuchar, decilo.
- **Límites (sección 13), aunque el usuario insista:** nada de testimonios fabricados, prensa o avales falsos, marcas ajenas, promesas médicas ni credenciales inventadas para un avatar.

## Herramientas en este entorno

- **Instalado:** `ffmpeg` (recortes, atempo + setpts, loudnorm a -14 LUFS, render 1080x1920 a 30 fps) y Python.
- **No instalado** (avisá y ofrecé instalarlo antes de usarlo): Whisper (para el QC hace falta el modelo **medium**), `torchaudio` (alineación forzada MMS_FA), OpenCV y un OCR como Tesseract (para los detectores de cara, saltos y texto quemado).
- **Generación:** el conector **Higgsfield** está disponible (Veo 3.1 Lite, Kling, Nano Banana, GPT Image, voces) y tiene `estimate_video_cost` y `estimate_image_cost` para el presupuesto. Antes de usarlo, cargá sus instrucciones de workflow como pide el propio conector.
- **ApiMart, HeyGen, ElevenLabs y Kie.ai no tienen clave cargada.** Si la ruta elegida los necesita, pedí la clave con `request_credential` para el host que corresponda. Nunca pidas que la peguen en el chat.

## Dónde guardar

Un proyecto por video en `SegundoCerebro(Fer:FORMULAEINFOPRODUCTOS/CREATIVOS/entregas/<YYYY-MM-DD>/<producto>-<pieza>/`, con la estructura de la sección 14 del manual (`guion/`, `img/`, `voz/`, `clips/`, `clips_malos/`, `broll/`, `prod/`, `final/` con MP4 + LEEME).

Los MP4 pesan: **no subas al repo** `clips/`, `clips_malos/` ni `broll/`. Commiteá solo el guion, el plan, los scripts y el LEEME, y mandá el MP4 final con `SendUserFile`. Si de producir sale conocimiento nuevo (un precio, un modelo que falló, un bloqueo del filtro), avisá para sumarlo a la wiki por la vía normal.
