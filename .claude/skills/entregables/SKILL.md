---
name: entregables
description: Productor de entregables. Lee una landing y produce lo que promete después de la compra (ebook PDF celular + imprimible, checklists, planillas .xlsx, PDF de acceso, guiones de video), con muestra de 3 páginas, OK, lote y carpeta con LEEME, siguiendo el Manual de Entregables de Fer Guerrero. Usar cuando el usuario diga "entregables para [URL]", "muestra de entregables", "armá el producto de esta landing", "armá los bonos de [URL]" o pida producir lo que recibe el comprador.
---

# Entregables

El método completo está en el manual. **Leelo entero antes de cada pedido** y seguí los pasos en orden: leer la landing, mapear promesa → archivo, preguntar, muestra, OK, lote, entrega.

`SegundoCerebro(Fer:FORMULAEINFOPRODUCTOS/RAW/manuales/manual-entregables.md`

Va después de `cazar` y `rayo-x`: la caza elige la oferta, el rayo X define los anuncios y esta skill produce lo que recibe el comprador. Contexto en la wiki: `creacion-de-productos-digitales.md`, `imagenes-y-mockups.md` y `aumento-de-aov.md`. Si la skill `anthropic-skills:ebook-higgsfield` está disponible, sirve de apoyo para los prompts visuales, pero mandan las reglas de este manual.

## Reglas que no se negocian

- **Regla madre:** nada pasa de la muestra al lote sin OK, y ninguna imagen se genera sin decir antes cuántas son y cuánto cuestan. La única excepción son las 3 a 5 imágenes de la muestra, que el pedido de muestra ya autoriza.
- **Abrí la landing sin reproducir audio.**
- **Como máximo 5 preguntas**, solo las que cambian el trabajo, y esperá la respuesta.
- **Primero el front.** Los bonos van después de la primera venta, salvo los que entran en la misma plantilla.
- **El texto crítico siempre como texto real en HTML**, nunca dentro de una imagen. Los diagramas y las tablas van en HTML o SVG.
- **Imágenes sin texto, sin caras reconocibles, sin logos ni marcas**, con la paleta de la landing.
- **Nunca inventes** estadísticas, testimonios, premios, cifras ni fuentes. Los valores técnicos van en cajas «Referencia» para que los valide un experto.
- **Salud, electricidad, dinero o legal:** el LEEME dice que un profesional tiene que validar el contenido antes de vender.
- **Nunca borres ni sobrescribas** una entrega anterior sin preguntar.

## Herramientas en este entorno

- **PDF:** Chrome está en `/usr/bin/google-chrome` (headless, costo cero) y `pdftoppm` para rasterizar y revisar cada página. Playwright también sirve para leer la landing y su CSS.
- **Imágenes:** el manual usa Kie.ai (`nano-banana-2-1` por defecto), pero **en este entorno no hay clave de Kie.ai cargada**. Si el usuario quiere usar Kie, pedila con `request_credential` para `api.kie.ai` y consultá el precio del día antes de generar. Si no, usá el conector **Higgsfield** (`generate_image`) y consultá el costo con `estimate_image_cost`. Decí siempre qué modelo usaste y cuánto costó.
- **Planillas:** `.xlsx` con la skill `anthropic-skills:xlsx`.
- **Entrega en Impultienda:** el PDF terminado se puede cargar como entregable con `impultienda_cargar_entregable`, **solo con OK explícito**.

## Dónde guardar

Una carpeta por entrega en `SegundoCerebro(Fer:FORMULAEINFOPRODUCTOS/ENTREGABLES/<YYYY-MM-DD>-<producto>/`, con los PDF (uno por formato), los HTML, `img/`, los scripts, el `.xlsx` si lo hay y el `LEEME.md`.

Esto es una sesión en la nube, así que no hay Escritorio: en vez de la copia al Escritorio, mandá los PDF y el LEEME con `SendUserFile` y avisá que queden subidos al repo. Si de producir sale conocimiento nuevo (un precio, un formato, una regla), avisá para procesarlo en la wiki por la vía normal.
