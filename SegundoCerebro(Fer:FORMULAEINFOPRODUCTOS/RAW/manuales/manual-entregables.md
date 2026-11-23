# Manual de Entregables · Por Fer Guerrero

Por Fer Guerrero · Fórmula E. Cómo producir lo que una landing promete: leer, mapear, preguntar, muestra con imágenes, OK, lote, entrega con LEEME.

## 0. Instrucción para la IA que lee este archivo

Sos mi productor de entregables. Cuando te diga **"entregables para [URL]"** o te pase una landing pidiendo lo que se entrega después de la compra:

1. **Abrí la landing en el navegador sin reproducir audio** y extraé: nombre del producto, promesa principal, idioma y mercado, precio y tachado, formato prometido (PDF, celular, imprimible, video, planilla, acceso), la lista completa de entregables y bonos con su texto literal, la garantía y las preguntas frecuentes. Sacá también la paleta y las tipografías de la página.
2. **Armá la tabla promesa → archivo** (sección 04) y marcá qué es front y qué es bono. Primero el front; los bonos, después de la primera venta.
3. **Hacé como máximo 5 preguntas**, solo las que cambian el trabajo (sección 05). Esperá mi respuesta.
4. **Producí una muestra de 3 páginas reales con imágenes** (sección 06) con la IA más barata del día (sección 07). El pedido de muestra ya es el OK para esas 3 a 5 imágenes; decime el costo exacto en la misma respuesta. Entregá la muestra y **esperá mi OK**.
5. **Con el OK, producí el lote** (sección 08). Antes de generar las imágenes del lote decime cuántas son y cuánto cuestan, y esperá el OK.
6. **Entregá en una carpeta con un LEEME** (sección 10) que diga qué hay, qué se decidió, qué QC se hizo, cuánto costó en IA y qué NO se verificó.
7. **Nunca inventes** estadísticas, testimonios, premios ni cifras. Los valores técnicos van en cajas «Referencia» marcadas para que los valide un experto.

> **Regla madre:** nada pasa de la muestra al lote sin mi OK, y ninguna imagen se genera sin que me hayas dicho antes cuánto cuesta. La única excepción son las 3 a 5 imágenes de la muestra, que el pedido de muestra ya autoriza.

---

## 1. Dónde entran los entregables

El producto digital **no adquiere clientes: los retiene**. Lo que vende es la comunicación (anuncios y landing). Pero lo que la persona recibe en su casilla tiene que ser lo mejor que puede recibir por lo que pagó, porque de eso dependen los reembolsos, la recompra y el backend.

| Paso | Qué resuelve | Manual |
|---|---|---|
| **Caza** | Qué oferta vender y en qué mercado | Manual de Caza de Ofertas |
| **Rayo X** | Con qué anuncios salir a testearla | Manual de Rayo X |
| **Entregables** | Qué recibe el cliente cuando paga | Este manual |
| **Embudo post-compra** | Qué más se le ofrece después de pagar | Manual del Embudo Post-Compra |

**Dos afirmaciones que parecen contradecirse y no lo hacen:** el producto es lo menos importante para vender, y aun así tiene que ser 10/10. Se resuelve así: se produce **rápido** para salir a validar, pero con una plantilla que garantiza la calidad desde la primera página.

**El error clásico:** tardar un mes haciendo el PDF antes de saber si la oferta vende. **El error opuesto:** mandar un PDF genérico que no se parece a lo que la landing prometió. Este manual evita los dos con el mismo truco: una muestra de 3 páginas con el diseño final, antes de producir nada más.

---

## 2. Qué necesitás antes de empezar

- **La landing publicada** con la lista de entregables y bonos. Si la landing cambió de producto (pasa cuando se reutiliza un dominio), vale lo que está publicado hoy.
- **Una IA de imagen por API** con la clave cargada. Hoy la más barata que sirve es Nano Banana 2.1 en Kie.ai; la IA tiene que consultar el precio del día antes de generar (sección 07).
- **Google Chrome instalado**: el PDF se arma con HTML y CSS y se exporta con Chrome en modo headless. No hace falta ningún programa de diseño ni suscripción.
- **Un experto que valide lo técnico** si el producto toca salud, electricidad, dinero o legal. Si no lo hay, el LEEME lo dice y el producto no se vende hasta tenerlo.
- **Material previo**, si existe: PDF viejo, producto del competidor comprado, transcripciones, bonos anteriores.

**Cómo pedirlo:**

- "Entregables para https://miproducto.impultienda.ar/" → todo el flujo, empezando por la lectura y las preguntas.
- "Muestra de entregables para [URL], en inglés, solo la versión celular" → la muestra directa con esas dos decisiones ya tomadas.
- "Armá los bonos 3 y 6 de [URL] con la misma plantilla" → lote parcial sobre una plantilla ya aprobada.

---

## 3. Paso 1: leer la landing

Se abre la landing en el navegador, **sin reproducir el audio** de ningún video. Se lee el texto completo y se anota:

| Dato | Dónde está | Para qué sirve |
|---|---|---|
| Nombre y promesa principal | Hero | Título y portada del entregable |
| Idioma y mercado | Texto, moneda, dominio | Idioma del entregable; formato de papel (Letter o A4) |
| Precio y tachado | Bloque de oferta | Nivel de ambición del producto |
| Formato prometido | Bloque «qué recibís», FAQ | PDF, celular, imprimible, video, planilla, acceso |
| Lista de entregables y bonos | Stack de la oferta | Una fila por ítem en la tabla del paso 2 |
| Garantía y FAQ | Pie | Qué no puede faltar sin generar reembolsos |
| Paleta y tipografías | CSS de la página | El entregable se ve de la misma familia que la landing |

La paleta se saca de las variables de color de la página y de los botones; las tipografías, de los títulos y el cuerpo. Si no se pueden leer, se eligen dos colores dominantes a ojo y se anota que fue a ojo.

---

## 4. Paso 2: mapear promesa → archivo

Antes de preguntar nada, la IA arma esta tabla con **una fila por cada cosa que la landing promete**:

| Promesa (texto de la landing) | Archivo a producir | Formato | Páginas o duración | Front o bono |
|---|---|---|---|---|
| «120 diagnósticos listos» | Ebook principal, una ficha por página | PDF celular + Letter | 120 fichas | Front |
| «Checklist antes de reemplazar» | Checklist de 4 a 6 páginas | PDF, misma plantilla | 6 | Bono (entra en el mismo build) |
| «Calculadora de presupuesto» | Planilla con fórmulas | .xlsx | 1 hoja | Bono |
| «Acceso a la herramienta IA» | PDF de acceso con link y QR | PDF | 1 | Front |

**Reglas de mapeo:**

- **Primero el front, los bonos después de la primera venta**, salvo los que entran en la misma plantilla (checklists, guías cortas), que se producen en el mismo build.
- Lo prometido como **planilla o calculadora es .xlsx**, no un PDF con una tabla.
- Lo prometido como **video es video**; este manual escribe el guion y el plan, y la producción sigue el Manual de Producción con IA.
- Lo prometido como **«celular + imprimible» son dos versiones del mismo HTML**: una vertical para teléfono y una Letter o A4 para imprimir.
- Si la landing promete PDF, **no se agrega un videocurso al front**: ese videocurso es el OTO 1 del embudo post-compra.
- Siempre que haya algo que no es un archivo (una herramienta, un grupo, un área), va un **PDF de acceso** con link y QR.
- El **idioma del entregable es el de la landing**, salvo que yo diga otra cosa.

---

## 5. Paso 3: preguntar (máximo 5)

Solo se pregunta lo que **cambia el trabajo**. Lo que ya responde la landing no se pregunta.

- ¿Idioma final? (si la landing es bilingüe o el mercado no está claro)
- ¿Qué bono priorizar después del front?
- ¿Hay un experto que valide lo técnico? (salud, electricidad, dinero, legal)
- ¿Existe material previo que haya que respetar o reutilizar?
- ¿Los dos formatos (celular e imprimible) o uno solo?
- ¿Lleva marca, nombre de autor o firma?

Se hacen las que apliquen, nunca más de cinco, y se espera la respuesta antes de producir.

---

## 6. Paso 4: la muestra con imágenes

La muestra son **3 páginas o fichas reales del front**, con el diseño final: portada con imagen, una apertura de sección con imagen y contenido real, no de relleno. Si hay dos formatos, la muestra va en los dos.

### Cómo se construye

- **Texto y armado en HTML y CSS; PDF con Chrome headless.** El texto crítico (títulos, tablas, precios, pasos, valores) siempre como texto real, nunca dentro de una imagen. Así no hay errores de ortografía generados y se puede corregir sin regenerar nada.
- **El contenido vive como datos**, no como páginas sueltas: agregar una ficha es agregar un bloque de texto, y la plantilla la dibuja igual que a las demás. Si una ficha no entra en su página impresa, se acorta el texto; no se agranda la página.
- **Índice con enlaces internos**: en el celular se toca el ítem y abre la página; cada página tiene un «↑ Índice».
- **Imágenes solo donde no hay datos**: portada, apertura de cada sección, ambiente. Los diagramas, tablas y valores se dibujan con HTML o SVG, nunca con IA de imagen.
- **Prompts de imagen**: fotografía editorial, sin texto, sin caras reconocibles, sin logos ni marcas, con la paleta de la landing pedida explícitamente.

### Control de calidad antes de entregar

- Se rasteriza cada página y se mira: nada cortado, pie visible en todas, portada legible, enlaces del índice presentes.
- Se mira cada imagen: sin texto, sin caras, sin marcas de agua.
- Se dice el costo exacto de las imágenes en la misma respuesta.

> La muestra se entrega y se **espera el OK o los cambios**. No se arranca el lote sin eso.

---

## 7. Paso 5: elegir la IA más barata

Cada vez, antes de generar, la IA **consulta el precio del día** de los candidatos (en Kie.ai: `GET /api/v1/models/<modelo>/price`). Si apareció algo más barato que cumpla (sin texto quemado, sin marca de agua, resolución suficiente), lo usa y lo dice. Si falla o degrada, vuelve al verificado.

### Imagen · verificado en api.kie.ai el 2026-11-09

| Modelo | Precio | Uso |
|---|---|---|
| `nano-banana-2-1` | 4 créditos (0,02 USD) en 1K · 6 (0,03) en 2K | Separadores, fondos, ambiente. **Por defecto.** |
| `nano-banana-pro` | 18 créditos (≈0,09 USD) en 1K/2K | Solo si la imagen lleva texto o necesita referencia de personaje |

Regla de costo: un ebook con portada en 2K y 8 aperturas en 1K cuesta **≈0,20 USD** en imágenes. La muestra de 3 páginas, con portada y 3 aperturas, **≈0,09 USD**.

### Video con avatar · precios de trabajo

| Modelo | Precio | Nota |
|---|---|---|
| Omni Flash 1.1 (ApiMart) | ≈0,036 USD/s · VSL de 6 min ≈ 13 USD | **Por defecto.** La voz puede variar: clip de prueba siempre |
| OmniHuman 2.0 (Kie) | 0,07 USD/s | El más limpio. Para clips cortos donde la cara tiene que ser perfecta |
| Kling AI Avatar (Kie) | 0,05 USD/s | **No usar**: quema pseudo-subtítulos en ~40 % de los clips |

Voz: ElevenLabs Turbo 2.5 vía Kie, 6 créditos por mil caracteres (≈0,03 USD). PDF y armado: **costo cero**, es HTML más Chrome.

Herramientas de suscripción (Gamma, Canva, HeyGen) sirven para un MVP de un día; por pieza producida salen más caras que este flujo. Si ya pagás una, usala; si no, no hace falta contratarla.

---

## 8. Paso 6: el lote

- Con el OK, se produce el **front completo** y después los bonos en el orden acordado. Mismo build: agregar contenido es agregar datos, no diseñar páginas nuevas.
- Antes de generar las imágenes del lote, la IA dice **cuántas son y cuánto cuestan**, y espera el OK.
- Producción larga en tandas y en segundo plano; se revisa cada tanda rasterizada igual que la muestra.
- Si hay video (bienvenida, clases, clips): guion y plan acá; producción con el Manual de Producción con IA, con el avatar por defecto de la sección 07 y clip de prueba antes de la tanda.
- **Segunda pasada de revisión del texto** con otro modelo antes de cerrar: ortografía, coherencia entre fichas, promesas que no se cumplen.

---

## 9. Reglas de contenido

- **Nada de estadísticas, testimonios, premios, cifras ni fuentes inventadas.**
- Cada sección responde el **«¿y cómo?» en el mismo lugar**. Si es una referencia de consulta, una unidad por página y el mismo orden de bloques en todas.
- Los **valores técnicos** van en cajas «Referencia» marcadas para validar por un experto. Donde no hay un dato confiable, se dice cómo obtenerlo en vez de inventarlo.
- En salud, electricidad, dinero y legal, el LEEME dice explícitamente que **un profesional debe validar antes de vender**.
- El entregable tiene que **parecerse a la promesa**. Si la landing dice «abrís el síntoma y tenés el primer chequeo delante», el PDF no puede ser un manual de teoría. El reembolso más común es el del producto que no se parece a lo que se compró.

---

## 10. Entrega y LEEME

Todo va en **una carpeta por entrega** con fecha y nombre del producto:

- Los PDF (uno por formato), los HTML, la carpeta `img/`, los scripts que los generan y el `.xlsx` si lo hay.
- Un `LEEME.md` con: qué hay, qué se decidió del diseño, qué QC se hizo, **cuánto costó en IA**, y **qué NO se verificó** (y quién tiene que verificarlo).
- Una copia de la carpeta en el Escritorio, para abrirla sin buscar.
- Nunca se borra ni se sobrescribe una entrega anterior sin preguntar.

Si de producir salió conocimiento nuevo (un formato que funcionó, un precio nuevo, una regla), se avisa para sumarlo al segundo cerebro. Este manual se actualiza con la fecha de los precios.

---

## 11. La plantilla técnica

No hace falta saber programar para usarla, pero la IA sí tiene que seguir esta estructura:

- Un script con el **contenido como datos** (una lista de fichas o capítulos), la **hoja de estilos** con las variables de color y tipografía de la landing, y **dos bloques `@page`**: uno de 108 × 192 mm para el celular (9:16) y uno Letter o A4 para imprimir.
- Dos funciones que reparten el contenido: en celular, varias pantallas por ficha; en impreso, **una ficha por página**.
- Un segundo script que genera las imágenes por API y las baja a `img/`. Idempotente: no regenera lo que ya existe.
- El render se hace con Chrome:

```
chrome --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=salida.pdf archivo.html
```

- Para revisar: `pdftoppm -r 60 -png salida.pdf pagina` y mirar cada PNG.
- Dos errores que ya costaron una vuelta: una regla genérica de pie de página que pisa el color del pie de la portada (texto invisible sobre fondo oscuro), y fichas largas que desbordan la página impresa sin aviso. Se revisan siempre la última fila y el pie.

---

## 12. Checklist de entregables

1. Landing leída sin audio: promesa, formato, lista de entregables y bonos, garantía, paleta y tipografías.
2. Tabla promesa → archivo con una fila por ítem, front y bonos marcados.
3. Preguntas hechas (máximo 5) y respondidas.
4. Muestra de 3 páginas reales con imágenes, en los formatos prometidos, con costo dicho.
5. Precio del día consultado antes de generar; modelo elegido y justificado.
6. QC de la muestra: páginas rasterizadas, nada cortado, imágenes sin texto ni caras.
7. OK recibido antes del lote. Costo de las imágenes del lote dicho y aprobado.
8. Front completo, bonos en orden acordado, planillas en .xlsx, PDF de acceso si corresponde.
9. Segunda pasada de revisión del texto.
10. Carpeta de entrega con LEEME (qué hay, decisiones, QC, costo, no verificado) y copia en el Escritorio.
11. Lo técnico marcado para validar por un experto; en salud, electricidad, dinero y legal, nada se vende sin esa validación.
