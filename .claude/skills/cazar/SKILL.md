---
name: cazar
description: Cazador de ofertas low ticket en la Biblioteca de Anuncios de Meta, siguiendo el Manual de Caza de Ofertas de Fer Guerrero. Usar cuando el usuario diga "cazá [nicho]", "cazá ofertas de...", "buscá ofertas ganadoras", "espiá competidores", "qué se está escalando en [nicho]" o pida arbitraje de mercados fuente → destino.
---

# Cazar ofertas

El método completo está en el manual. **Leelo entero antes de empezar cada caza** y seguí las secciones 3 a 9 en orden, sin saltear filtros:

`SegundoCerebro(Fer:FORMULAEINFOPRODUCTOS/RAW/manuales/manual-caza-de-ofertas.md`

Para el contexto del método, mirá también en la wiki `funnel-hacking.md`, `seleccion-y-modelado-de-oferta.md`, `segmentos-de-mercado.md` e `internacionalizacion.md`.

## Reglas que no se negocian

- **Filtro madre:** más de 40 anuncios activos sobre la misma oferta, corriendo hace más de una semana. Lo que no llega, no se recomienda.
- Espiá en los mercados **fuente** (BR, US y el mundo anglo) y verificá el hueco en los mercados **destino** (LatAm, España, Europa no anglo).
- **Abrí siempre la landing y llegá hasta el precio** antes de recomendar algo (sección 7 del manual).
- Si un dato no se pudo confirmar, ponelo como **"no confirmado"**. Nunca lo inventes.
- **Nunca hagas una compra de prueba** sin el OK explícito del usuario.
- Entregá el reporte con el formato de la sección 11 y cerrá con veredicto, par de arbitraje y próximo paso.

## Qué herramienta usar (en este orden)

1. **`ads_library_search` del conector oficial de Meta.** Si está diferida, buscala con ToolSearch y cargala. Es solo lectura.
2. **Si no está instalada:** usá el conector **EspiAd** (`mcp__ESPIAad__buscar_ofertas`, `ver_oferta`, `que_se_movio`). Es un catálogo de ofertas digitales con anuncios activos en Meta, con los links a la Biblioteca, la landing y el checkout. Ojo: EspiAd mide pauta activa, no ventas. No estimes facturación a partir de ese número.
3. **Para contar el arsenal y abrir landings:** usá el navegador (`facebook.com/ads/library` con país, estado Activo y el término) o abrí los links que devuelve EspiAd.

Avisá al usuario qué fuente usaste, porque los conteos de EspiAd y los de la Biblioteca pueden no coincidir.

## Después de la caza

Cuando haya candidata A, ofrecé hacerle un **rayo X** con la skill `rayo-x` para definir con qué anuncios salir a testearla.

## Dónde guardar

Si el usuario quiere conservar el reporte, guardalo en `SegundoCerebro(Fer:FORMULAEINFOPRODUCTOS/OUTPUTS/YYYY-MM-DD-caza-<nicho>.md` con el frontmatter que pide el `CLAUDE.md`, y anotalo en `WIKI/index.md` y en `changelog.md`.
