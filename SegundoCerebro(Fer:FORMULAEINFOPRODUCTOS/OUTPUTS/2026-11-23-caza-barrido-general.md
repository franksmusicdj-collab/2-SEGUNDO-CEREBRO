---
fecha: 2026-11-23
pregunta: "Cazá ofertas ahora y decime qué me conviene salir a probar al mercado"
fuentes: [RAW/manuales/manual-caza-de-ofertas.md, WIKI/funnel-hacking.md, WIKI/seleccion-y-modelado-de-oferta.md, WIKI/validacion-de-oferta.md]
---

# Caza · barrido general · 2026-11-23

**Herramienta usada:** EspiAd (el conector oficial de Meta no está instalado). Los conteos son los de EspiAd, que mide pauta activa, no ventas. La Biblioteca de Meta **no se pudo abrir** desde este entorno (Facebook devuelve 403 y bloquea sus recursos), así que **los duplicados por creativo y la fecha real del anuncio más viejo quedan como no confirmados.**

**Barrido:** ofertas con 40 o más anuncios activos en portugués (40), inglés (40) y español (40), más los movimientos de los últimos 14 días. Huecos verificados en español con búsquedas por "pilates", "calistenia", "caminata" y los nichos fitness y salud en español.

## Shortlist

| Campo | **A · Desafío Pilates en Casa 50+** | **B · Calistenia Asiática para mujeres 40+** |
|---|---|---|
| Página | [Biblioteca](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&search_type=page&view_all_page_id=2016271568674266) | [Biblioteca](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&search_type=page&view_all_page_id=634382966425687) |
| Mercado fuente | Brasil, portugués | Brasil, portugués (ya testea en Italia: 12 anuncios) |
| Arsenal | 480 anuncios activos (pico de 500), 189 días corriendo, creciendo desde 240 en septiembre | 685 anuncios activos (pico de 823), 129 días; la misma página corre dos fichas (685 + 660) |
| Producto y precio | Desafío de pilates en casa, sin aparatos. **29,90 BRL** según EspiAd (checkout de OnProfit: no confirmado, no cargó) | Programa de calistenia con quiz por edad. **US$ 6,39** en el checkout de Lastlink, visto desde EE. UU. (EspiAd: 37,90 BRL) |
| Embudo | Quiz → checkout OnProfit | Quiz "Teste de 1 minuto" (primera pregunta: edad 39-45 / 46-50 / 51-60 / 60+) → checkout Lastlink |
| Order bumps | No confirmado | 3 bumps a US$ 2,51-3,36: "Shots Acelerador de Intestino", "Jejum Noturno Inteligente", "Protocolo Zero Flacidez" |
| Mecanismo | Pilates adaptado a +50: "sin gimnasio, sin aparatos, sin lastimarte" | Calistenia "asiática": tendencia de redes adaptada a mujeres maduras |
| Sofisticación fuente | 4 · mecanismo + identidad por edad | 4 · mecanismo con nombre + identidad por edad |
| Ángulo principal | "El ejercicio ya no es para mí / miedo a lastimarme" | "Entrenar en casa a mi ritmo, sin equipamiento" |
| Creativos a modelar | No confirmado (Biblioteca bloqueada) | No confirmado (Biblioteca bloqueada) |
| Puntaje | **3/4 confirmado + 1 pendiente.** Longevidad ✔ (189 d), volumen ✔ (480), hueco ✔ (cero ofertas activas de pilates 50+ en español en EspiAd), duplicación: no confirmada | **2/4 confirmado + 1 pendiente.** Longevidad ✔, volumen ✔, duplicación: no confirmada, hueco ✘ parcial (en español ya hay "Protocolo Calistenia Militar", 106 anuncios, y un tester de hace 2 días, "Calistenia Suave en Casa", 18 anuncios) |

## Descartadas o en observación

| Oferta | Motivo |
|---|---|
| Perca peso com caminhada (792 anuncios) | **Falso positivo:** es una app (walk-fit.io), no un infoproducto modelable |
| El Juego del Deseo (130 anuncios en LATAM, 12 días) | Ya está en español y en varios idiomas: la ventana se está cerrando. Observar |
| Dieta das 3 Fases, Segredo da Insulina, Protocolo de Desparasitação Articular, Zero Lipedema | Mucho volumen, pero el ángulo descansa en promesas médicas que no se pueden modelar en el anuncio. Descartadas por límites del manual |
| +300 Mapas Mentais de Inglês (665) | Fuera de los tres grandes nichos; ya hay clones en español (italiano, informática) |

## Veredicto

**MODELAR Y MUDAR — Desafío Pilates en Casa 50+.**

- **Par de arbitraje:** Brasil (nivel 4) → Latinoamérica hispana (México como primer mercado, después Colombia, Argentina y Chile) y España. En español no aparece ninguna oferta activa de pilates para +50 (nivel 1-2 en el destino). Hay que confirmarlo en la Biblioteca con "pilates en casa", "pilates para mujeres de 50" y "pilates en la pared" con `country=MX` y `ES`.
- **Por qué no la calistenia:** vende más, pero el hueco en español ya se está llenando y sus bumps se apoyan en promesas de salud ("elimine 1 kg de grasa por las heces") que no pasan los límites.
- **Compliance:** el ángulo de "desinflamar" se trabaja como bienestar y movilidad, nunca como promesa médica. Nada de cifras de kilos ni de días en el anuncio.

## Próximo paso

1. Confirmar en la Biblioteca el arsenal de la página 2016271568674266 (duplicados, anuncio más viejo, landing única) y el hueco en México y España. Hace falta habilitar los dominios de Facebook o revisarlo a mano.
2. Abrir el checkout de OnProfit para confirmar precio, bumps y garantía.
3. **Rayo X** a esa página para sacar los 10 a 20 creativos ganadores y los guiones en español.
4. Validar con la regla del método: 20 a 30 anuncios y al menos 3 días antes de descartar.
