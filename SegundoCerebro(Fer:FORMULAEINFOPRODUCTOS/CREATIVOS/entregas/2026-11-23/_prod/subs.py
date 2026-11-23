"""Subtítulos estilo anuncio: 2-3 palabras, MAYÚSCULAS, Anton, contorno grueso, clave en amarillo, pop 72-110-100%."""
def _t(s):
    s = max(0, s); h = int(s // 3600); m = int(s % 3600 // 60)
    return f"{h}:{m:02d}:{s % 60:05.2f}"

def ass(grupos, W=720, H=1280, y_pct=0.64):
    """grupos: lista de (inicio, fin, [(palabra, es_clave), ...])"""
    cab = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: S,Anton,{int(W*0.105)},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,1,0,1,{max(4,int(W*0.009))},2,5,30,30,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    x, y = W // 2, int(H * y_pct)
    out = []
    for s, e, ws in grupos:
        txt = " ".join(("{\\c&H00E5FF&}" + w.upper() + "{\\c&HFFFFFF&}") if k else w.upper() for w, k in ws)
        pop = "{\\pos(%d,%d)\\fscx72\\fscy72\\t(0,90,\\fscx110\\fscy110)\\t(90,160,\\fscx100\\fscy100)}" % (x, y)
        out.append(f"Dialogue: 0,{_t(s)},{_t(e)},S,,0,0,0,,{pop}{txt}")
    return cab + "\n".join(out) + "\n"
