# Manual de Rayo X · Por Fer Guerrero

> Pegá este archivo entero en tu segundo cerebro (proyecto de Claude, Obsidian, Notion o el CLAUDE.md de tu carpeta).
> Después escribile a tu IA: **"Hacele un rayo X a [competidor] siguiendo el Manual de Rayo X."**
> Ejemplos: "Rayo X a [link de la biblioteca de anuncios de la página]", "Rayo X a [página], mi oferta es [producto, precio, país]", "Con qué anuncios salgo a testear [oferta]".
> Los anuncios del competidor se estudian para modelar formato y estructura. El texto, las caras, la voz y el footage son siempre propios.

---

## 0. Instrucción para la IA que lee este archivo

Sos mi analista de anuncios. Cuando te diga "hacele un rayo X a [competidor]":

1. **Identificá al competidor.** Acepto un link a su biblioteca de anuncios (`view_all_page_id=…`), un link a un anuncio suelto (`?id=…`), el nombre de la página, o "la candidata A de la caza de [nicho]". Si solo tenés el nombre, buscalo en `facebook.com/ads/library` y abrí "Ver todos los anuncios" de esa página.
2. **Preguntame a qué mercado lo quiero lanzar y a qué idioma traducir** antes de empezar. Esa respuesta manda sobre todo lo que sigue: las transcripciones, los títulos, los copies y los guiones se adaptan a ese idioma y a ese mercado, no al español por defecto.
3. **Pedime mi oferta propia**: producto, promesa, precio y mecanismo con nombre. Si no te la doy, hacé el barrido igual y dejá los guiones adaptados como "pendientes".
4. **Herramienta:** primero `ads_library_search` del conector oficial de Meta (Facebook) con `page_ids`. Es solo lectura. Si no está instalado, usá `facebook.com/ads/library` en el navegador, **siempre con `country=ALL`**.
5. **Seguí las secciones 3 a 10 en orden.** No saltees el barrido completo para "ir directo a los más vistosos": el ranking es lo que vale. La base es: **todos los anuncios barridos y los 10 a 20 mejores rescatados en una carpeta**, ordenados por duplicados y días.
6. **Pedime OK antes de bajar cualquier video** (nombre, origen y tamaño de cada uno). Nunca hagas una compra de prueba ni completes un quiz con datos reales sin mi OK explícito.
7. **Cuando la carpeta y el ranking estén listos, ofreceme transcribirlos** para modelarlos al idioma destino. Es una opción, no un paso obligatorio: si digo que no, la base igual queda hecha.
8. Entregame el reporte con el formato de la sección 11 y el swipe con títulos, copies y guiones. Si un dato no lo pudiste confirmar, marcalo como "no confirmado": nunca lo infieras.

---

## 1. Dónde entra el rayo X

Un lanzamiento tiene **dos pilares: la oferta y los creativos**. Se puede encontrar una oferta ganadora y fallar en los anuncios con los que se sale a testearla.

| Paso | Qué resuelve | Manual |
|---|---|---|
| **Caza** | Qué oferta vender y en qué mercado | Manual de Caza de Ofertas |
| **Rayo X** | Con qué anuncios salir a testearla | Este manual |
| **Producción** | Hacer esos anuncios y subirlos | Manual de Edición IA |

**Apego al competidor directo.** Los primeros anuncios no se inventan. Se analiza la biblioteca de anuncios de la página a la que le modelaste la oferta y se modelan el **formato y la estructura** de sus piezas más ganadoras. Variar, reinventar, probar formatos nuevos o imágenes viene **después** de validar la oferta.

**Cuáles son las ganadoras:** las que tienen **más días corriendo y más duplicados** (el mismo creativo repetido en muchos anuncios). Un creativo que el competidor duplica 10, 20 o 40 veces ya ganó su test interno: no hay que adivinar, hay que leerlo.

> **Regla de mínimos:** no se descarta una oferta sin haber corrido **20 a 30 anuncios distintos durante al menos 3 días**. Los primeros 5 o 10 pueden no pegar: se renueva una, dos o tres veces desde el arsenal del competidor antes de cambiar de oferta.

---

## 2. Qué necesitás antes de empezar

- **El competidor**: link a su biblioteca de anuncios, link a un anuncio suelto, o el nombre de la página. Si viene de una caza anterior, el reporte de esa caza ya lo tiene.
- **El mercado destino y el idioma**: a qué país vas a lanzar y a qué idioma hay que traducir. La IA lo pregunta primero si no lo dijiste. Un rayo X a una página de Brasil puede terminar en guiones en inglés para Estados Unidos o en italiano para Italia: el idioma de salida es el del destino, no el de la fuente ni el tuyo.
- **Tu oferta propia**: producto, promesa, precio, mecanismo con nombre y, si hay quiz, cómo se llama. Sin esto el barrido se hace igual, pero los guiones adaptados quedan pendientes.
- **La herramienta**: el conector oficial de Meta (`ads_library_search` con `page_ids`) o la biblioteca en el navegador. En el navegador, el link de la página es `facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=<id>`.

**Cómo pedirlo:**

- "Rayo X a https://www.facebook.com/ads/library/?…view_all_page_id=123" → barrido de esa página.
- "Rayo X a [página], lo quiero lanzar en Estados Unidos en inglés, mi oferta es un curso de resina a USD 17" → barrido + títulos, copies y guiones en inglés.
- "Hacele un rayo X a la candidata A de la caza de renta extra" → se toma del reporte de esa caza.
- "Con qué anuncios salgo a testear [oferta]" → se pregunta a quién se le modeló la oferta y se le hace el rayo X a esa página.

---

## 3. Paso 1: barrido completo

Se cargan **todos** los anuncios activos de la página. El total que vale es la línea "~N resultados" de la biblioteca. Por cada tarjeta se anota:

| Campo | De dónde sale |
|---|---|
| ID del anuncio | "Identificador de la biblioteca: <n>" |
| Fecha de inicio → **días en circulación** | "En circulación desde el D MMM AAAA" |
| **Duplicados** | Tarjetas con el mismo creativo (mismo video o imagen + mismos primeros 60 caracteres del copy). A veces la biblioteca lo dice sola: "N anuncios usan este creativo y texto" |
| Impresiones | **Solo si la biblioteca las muestra** (anuncios que corren en la Unión Europea). Si no aparecen, no se inventan ni se estiman |
| Formato | Video, imagen o carrusel; si es video, su duración |
| **Título y copy** | El título (headline) y el texto principal completos, tal cual están, con sus emojis. Se guardan siempre: son materia prima del paso 7 |
| Landing | El link `l.facebook.com/l.php?u=…` de la tarjeta. Sin link suele ser un embudo de WhatsApp |
| Vista previa | `https://www.facebook.com/ads/library/?id=<ID>` |

**Lo que hay que saber de la biblioteca en el navegador:**

- La vista de página carga 30 tarjetas y después pagina con un botón **"Ver más"** de a 10. El scroll solo no alcanza: hay que clickearlo en bucle esperando 2 o 3 segundos cada vez. Si aparece un spinner, esperar antes de concluir que no hay más.
- **La vista de página viene ordenada por impresiones** aunque el número no se muestre: la posición de la tarjeta ya es un ranking. Las últimas dicen "Número de impresiones bajo".
- **Duplicados reales:** la URL del video de cada tarjeta trae un parámetro `efg` con un `xpv_asset_id`. Dos anuncios con el mismo asset son el mismo video. Algunos operadores suben cada variación como asset nuevo: ahí la señal "N anuncios usan este creativo" no aparece y hay que agrupar por familias de guion después de transcribir.
- **Buscar una frase literal con `country=ALL` también matchea lo que se dice o se muestra en los videos**, no solo el copy. Sirve para encontrar familias de guion dentro de un arsenal grande.

**Resultado del paso:** una tabla con **una fila por creativo distinto** (no por anuncio), con duplicados, días, impresiones si hay, formato, landing y vista previa.

---

## 4. Paso 2: ranking y selección de ganadores

**Orden:** duplicados ↓, después días ↓, después impresiones ↓ (cuando existen).

Se rescatan **los 10 mejores como mínimo y hasta 20** (si la página tiene menos de 10 creativos distintos, se rescatan todos): los que combinan más días corriendo con más duplicados. Al arrancar alcanza con los primeros 10; los otros 10 son la reserva para las renovaciones.

| Caso | Lectura |
|---|---|
| 48 duplicados, 9 días | **Ganador** aunque sea nuevo: ya ganó el test interno |
| 39 duplicados, 19 días | **Ganador** y sostenido |
| 21 días, 0 duplicados | **Viejo, no ganador.** No entra |
| Dos anuncios con el mismo gancho y el mismo video | Cuentan como **uno**: se suman sus duplicados |

Cuando ningún creativo se duplica (cada variación subida como asset nuevo), el criterio pasa a ser **el orden por impresiones de la biblioteca más los días**.

Lo que no entra en el top **queda en la tabla completa del reporte**: es la cantera para las renovaciones, con ganchos que ya están validados en ese mercado.

**La base que tiene que quedar siempre**, aunque no se transcriba ni se escriba un solo guion: una carpeta del rayo X con los 10 a 20 ganadores numerados por ranking (`01-`, `02-`…) y un índice que diga, por cada uno, duplicados, días en circulación, formato, título, copy y link de vista previa. Eso es lo que se mira antes de producir y lo que se vuelve a abrir en cada renovación.

---

## 5. Paso 3: bajar los ganadores (con OK)

Los videos se bajan para **estudiarlos**, no para usarlos. Son material ajeno: **nunca se suben a una cuenta publicitaria ni se reusan como b-roll** (copyright y rechazo de Meta).

**1. Sacar la URL del video.** En la vista de página cada tarjeta ya trae su `<video src>` con la URL directa (`video.*.fbcdn.net/…mp4`, 360p). Esas URLs llevan firma y **vencen en horas**: bajar enseguida. Si una tarjeta no la trae, abrir su vista previa (`/ads/library/?id=<ID>&country=ALL`), esperar 2 o 3 segundos y leer los `<video>` de la página.

**2. Medir y pedir OK** en un solo mensaje con todos los videos: nombre de destino, origen (ID del anuncio y página) y tamaño en MB.

```
curl -sIL "<url>" | grep -i -E "content-length|content-type"
```

**3. Bajar** a la carpeta del rayo X (`swipe/<fecha>-rayo-x-<competidor>/videos/`), con el número de ranking adelante: `<nn>-<gancho-corto>.mp4` (el `01` es el más duplicado y más longevo). Las imágenes y carruseles ganadores se guardan en la misma carpeta con el mismo criterio:

```
curl -L -o "<n>-<gancho-corto>.mp4" "<url>"
```

Si la VSL del competidor está en HLS, se localiza el `.m3u8` en las peticiones de red y se baja con `ffmpeg -i <m3u8> -c copy salida.mp4`. A 360p, un video de 1 o 2 minutos pesa entre 2 y 6 MB.

---

## 6. Paso 4: transcribir (opcional)

Con la carpeta y el ranking listos, la IA **ofrece** transcribir los ganadores para modelarlos al idioma destino. Es una opción: si no se transcribe, la base del paso 2 igual queda hecha y sirve. Si se acepta, se transcribe en **el idioma de la fuente** (`pt` para Brasil, `en` para Estados Unidos, `es` para Latinoamérica y España) y se traduce al **idioma del mercado destino** que se eligió al principio:

```
ffmpeg -y -i "<n>-<gancho-corto>.mp4" -ar 16000 -ac 1 -c:a pcm_s16le "<n>.wav"
whisper-cli -m ggml-small.bin -l pt -otxt -osrt -of "<n>" "<n>.wav"
```

- La transcripción va **con timestamps**, en el idioma original, y debajo de cada bloque la traducción al idioma destino (inglés si se lanza en Estados Unidos, italiano si en Italia, español neutro si en Latinoamérica).
- **Los textos en pantalla** (subtítulos quemados, títulos) se anotan aparte: la transcripción no los ve y a veces son el gancho real.
- Las imágenes y los carruseles no se transcriben: se copia el texto en pantalla y el copy.
- Todas las transcripciones van a un solo archivo, una sección por ganador, con el encabezado: "referencia para modelar estructura y ángulos, no para copiar texto".

---

## 7. Paso 5: leer cada pieza

Por cada ganador, una ficha con estos campos:

- **Formato**: UGC a cámara, animado con IA, voz en off + b-roll, testimonial, estático o carrusel. Duración exacta.
- **Gancho literal** (primeros 3 segundos): lo que se **dice** y lo que se **ve**, y a qué tipo pertenece.
- **Ángulo** y **dolor o deseo** que ataca, en una línea cada uno.
- **Estructura**: los beats en orden mapeados a la fórmula de 7 pasos, con el segundo en que aparece cada uno y en qué segundo se nombra el producto.
- **CTA** y a qué landing manda.
- **Título y copy** del anuncio, literales, con sus emojis.
- **Por qué gana** (hipótesis, marcada como tal): qué tiene este que no tienen los que no se duplican.

**Tipos de gancho para clasificar:**

| Tipo | Ejemplo |
|---|---|
| Pregunta + promesa | "¿Sabías que podés… en 7 días?" |
| Secreto oculto | "Esto es lo que no te cuentan sobre…" |
| Nostalgia + superlativo | "La receta de mi abuela que…" · "El método más simple que existe" |
| Eliminación de objeciones | "Sin gimnasio, sin dieta, sin horno" |
| Tiempo ultra corto | "En menos de 10 minutos" |
| Series y sistemas | "7 días de…", "los 3 pasos para…" |
| Testimonio personal | "Bajé X kilos en Y meses" · "Mirá a mi mujer, está irreconocible" |
| Minidrama | Una escena cotidiana con conflicto ("¿Otra vez esto? Volvé a dormir") |

**La fórmula de 7 pasos** (para mapear los beats):

| # | Paso | Función |
|---|---|---|
| 1 | **Hook** | Frase y visual que detienen el scroll en 3 segundos |
| 2 | **Re-hook** | Empatía: "yo también estaba…", valida el problema |
| 3 | **Presentación del producto** | "Hasta que conocí [nombre]…" |
| 4 | **Beneficios** | "Tiene X que te permite Y" |
| 5 | **Mecánica** | Demostración breve de cómo funciona |
| 6 | **Prueba social** | "Miles de [avatar] ya…" |
| 7 | **CTA** | Instrucción directa |

---

## 8. Paso 6: rescatar títulos y copies de los ganadores

El video no es lo único que gana: el **título** (headline) y el **copy** (texto principal) de los anuncios ganadores también pasaron el test del competidor. Se rescatan siempre, con o sin transcripción.

**1. Rescatar.** Por cada ganador, título y copy literales, con sus emojis, en el idioma original. Si varios ganadores comparten el mismo copy (es común: un copy, muchos videos), se anota una vez y se dice en cuántos anuncios corre. Esa cantidad es la señal: el copy más repetido es el más validado.

**2. Leer.** De cada uno: gancho escrito (la primera línea, que es lo que se ve antes del "Ver más"), promesa, dolor o deseo, prueba, CTA, y qué emojis usa y dónde (al inicio como señal visual, como viñetas de beneficios, antes del CTA).

**3. Adaptar al idioma y mercado destino.** Se entregan, como mínimo, **4 títulos y 3 copies** listos para subir (más si el arsenal da para más). Reglas:

| Se mantiene | Se reescribe |
|---|---|
| El tipo de gancho y la estructura del copy (gancho → dolor → mecanismo → prueba → CTA) | Texto completo en el idioma destino, como habla ese público |
| La longitud aproximada y el uso de emojis como estructura visual | Nombre del producto, mecanismo con nombre propio, precio y moneda |
| El dolor o deseo que ataca | Referencias locales y expresiones |

**Mejorar con emojis:** si el competidor no los usa o los usa poco, se entrega una versión mejorada de cada título y copy con emojis que ordenen la lectura (uno al inicio del gancho, uno por beneficio, uno antes del CTA). Nunca más de uno por línea ni emojis que no aporten nada: en un copy de dinero o salud, los emojis no reemplazan a una promesa que no se puede hacer.

**Compliance:** mismo criterio que para los guiones. Nada de promesas de ingresos ni médicas en el título ni en el copy, aunque el competidor las haga.

---

## 9. Paso 7: recorrer la landing

Una por landing distinta. Si **todos** los anuncios van a la misma landing, es señal de que el competidor ya no está testeando: encontró la que convierte.

De cada landing se anota: estructura, promesa, mecanismo con nombre, prueba, oferta, **precio** (tachado, real, cuotas y order bumps: buscarlos en el código fuente de la página, no solo en el texto visible), garantía y, si hay quiz, cada pantalla **sin cargar datos reales**.

Si esta oferta ya tiene una radiografía hecha en la caza, se enlaza y no se repite.

---

## 10. Paso 8: síntesis del arsenal y guiones adaptados

**Síntesis del arsenal**, en cinco líneas:

- Qué dolor o deseo pesa más, **contado sobre el total de duplicados**, no de creativos.
- Qué formatos dominan y la duración típica.
- Cuántas landings y cuántas caras o avatares distintos usa.
- Qué nivel de sofisticación tiene el mensaje (promesa directa, mecanismo con nombre, historia e identidad).
- Qué tienen los ganadores que no tienen los que no se duplican.

**Guiones adaptados**, uno por ganador transcripto (los 10 primeros al menos). Se escriben en el **idioma del mercado destino**. Máximo apego a lo que se puede modelar:

| Se mantiene igual | Se reescribe |
|---|---|
| **Formato**: si es UGC animado, UGC animado. No se cambia el formato al modelar | **Texto completo**, en el idioma destino y como habla ese público |
| **Duración** (± 10%) y ritmo de los beats | Nombre del producto, mecanismo con nombre propio, precio del destino |
| **Tipo de gancho** y secuencia de la estructura | Caras, voz, testimonios, marca, dominio |
| **Dolor o deseo** que ataca y el CTA | Referencias locales: moneda, lugares, expresiones |

Cada guion lleva: título trazable, formato, duración objetivo, el ganador que modela (link de vista previa), gancho propuesto (dicho y visto), beats con segundos, copy del anuncio, CTA y una línea de **compliance**: nada de promesas de ingresos ni médicas en el anuncio. Si el competidor las hace, se sacan del anuncio y se dejan para la VSL.

---

## 11. Formato del reporte

**A. Reporte del rayo X** (un archivo):

| Sección | Qué va |
|---|---|
| Encabezado | Competidor, link a su biblioteca, mercado fuente, **mercado e idioma destino**, arsenal (~N anuncios, M creativos, L landings, desde cuándo), oferta propia, herramienta usada, si la biblioteca mostró impresiones |
| 1. Arsenal completo | Tabla con una fila por creativo: duplicados, días, impresiones, formato y duración, gancho literal en una línea, landing, vista previa. Ordenada por duplicados ↓, días ↓ |
| 2. Ganadores rescatados | Los 10 a 20, numerados como en la carpeta, con el criterio por el que entra cada uno, y los que quedaron afuera y por qué |
| 3. Fichas | Una por ganador (sección 7) |
| 4. Títulos y copies | Los originales de los ganadores y los adaptados: al menos 4 títulos y 3 copies, con su versión con emojis (sección 8) |
| 5. Landing | Sección 9 |
| 6. Síntesis del arsenal | Sección 10 |
| 7. No confirmado | Lo que no se pudo ver: precio detrás de un quiz, impresiones, un video que no cargó |
| 8. Próximo paso | Producir los guiones del swipe y testear con 20 a 30 anuncios y al menos 3 días |

**B. Carpeta de ganadores**: los 10 a 20 videos o imágenes numerados por ranking más un índice (duplicados, días, formato, título, copy, vista previa). Es la base; queda aunque no se transcriba nada.

**C. Swipe** (el archivo que lee quien produce), en el idioma destino:

- Tabla de **ganchos del competidor** (gancho, tipo, duplicados, vista previa) para las renovaciones.
- Los **títulos y copies adaptados** (4 y 3 como mínimo), con versión con emojis.
- Los **guiones adaptados**, uno por ganador transcripto, con el formato de la sección 10.

**D. Transcripciones** (solo si se pidieron): una sección por ganador, idioma original con timestamps y traducción al idioma destino debajo.

---

## 12. Modelar sin copiar

La tentación es "transcribir el anuncio, cambiar la oferta y usar exactamente ese mismo anuncio". **No.** Copiar literal es riesgo de copyright, de rechazo de Meta y de sonar extranjero en el mercado destino.

| Se modela | Es propio |
|---|---|
| Formato, duración, ritmo | Texto completo, reescrito como habla tu público |
| Tipo de gancho y estructura de beats | Caras, voz, footage, música |
| Dolor o deseo que ataca, CTA | Marca, nombre del producto, dominio, testimonios |
| Qué landing usa y cómo está armada | Tu landing, tu precio, tu mecanismo con nombre |

**Límites:**

- Nada de marcas registradas ajenas en el nombre ni en los anuncios.
- En salud: nada de promesas médicas, curas ni cifras garantizadas. En dinero: nada de promesas de ingresos en el anuncio.
- No se copian archivos, textos literales, fotos, videos ni testimonios de otros. Los videos bajados se miran y se borran de cualquier flujo de producción.
- Se adapta el mecanismo al nivel del mercado destino: más simple si el público vio menos ofertas.

---

## 13. Lo que el rayo X no hace

- No elige la oferta ni mide el hueco de mercado: eso es el Manual de Caza de Ofertas.
- No produce los creativos ni los sube a Meta: entrega guiones. La producción es el Manual de Edición IA; el testeo, el Manual de Manejo de la CBO.
- No recorre el post-pago del competidor: eso es el Manual del Embudo Post-Compra.
- No copia texto literal, caras, voz ni footage del competidor.
- No hace compras de prueba ni completa quizzes con datos reales sin OK.

---

## 14. Checklist del rayo X

1. Competidor identificado con link a su biblioteca (`country=ALL`).
2. Mercado destino e idioma de salida preguntados y anotados.
3. Oferta propia definida: producto, promesa, precio, mecanismo con nombre.
4. Barrido completo hecho: todas las tarjetas cargadas, total contrastado con "~N resultados".
5. Tabla con una fila por creativo distinto: duplicados, días, impresiones si hay, formato, título, copy, landing, vista previa.
6. Ranking por duplicados ↓, días ↓, impresiones ↓ y 10 a 20 ganadores rescatados con criterio escrito.
7. OK pedido y recibido antes de bajar cada video; carpeta numerada por ranking con su índice.
8. Transcripción ofrecida; si se aceptó, con timestamps en idioma original y traducción al idioma destino, textos en pantalla anotados.
9. Una ficha por ganador: formato, gancho literal y tipo, ángulo, dolor, estructura en 7 pasos, CTA, título y copy, hipótesis.
10. Títulos y copies rescatados y adaptados al idioma destino: al menos 4 títulos y 3 copies, con versión con emojis y compliance.
11. Landing recorrida hasta el precio, quiz sin datos reales.
12. Síntesis del arsenal y guiones adaptados en el idioma destino, con compliance.
13. Reporte, carpeta, swipe y transcripciones (si se pidieron) entregados; lo no confirmado marcado.
14. Próximo paso fijado: producir y testear 20 a 30 anuncios, al menos 3 días, renovando desde el arsenal antes de cambiar de oferta.
