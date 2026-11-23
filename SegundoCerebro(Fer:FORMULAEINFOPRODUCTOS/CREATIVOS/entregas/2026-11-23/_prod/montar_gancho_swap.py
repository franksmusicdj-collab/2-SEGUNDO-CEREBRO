"""Gancho final: video generado (movimiento copiado del video del usuario), SIN efectos agregados.
Audio del tirón/golpe = audio original del video de referencia del usuario hasta que el personaje empieza a hablar; después, la voz del clip."""
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from subs import ass
from alinear import alinear
k, frase, gancho = sys.argv[1], sys.argv[2], sys.argv[3]       # gancho: texto de pantalla desde el cuadro 1, ej. "Chega de tela."
D = f"mente-activa-bf-{k}"; F = f"{D}/clips/C1_swap.mp4"; OUT = f"{D}/prod"; REF = "_referencia/referencia_usuario.mp4"
W = alinear(F, frase)
S0 = W[0]["s"] - 0.10            # desde acá, voz del personaje
END = W[-1]["e"] + 0.16
palabras = frase.split()
claves = {0, len(W) - 1}
grupos, i = [], 0
while i < len(W):                # grupos de 2-3 palabras, cortando en signos de puntuación
    j = i
    while j < len(W) - 1 and j - i < 2 and not W[j]["w"][-1] in ".,!?":
        j += 1
    grupos.append((W[i]["s"], W[j]["e"] + 0.05, [(W[m]["w"], m in claves) for m in range(i, j + 1)]))
    i = j + 1
g0 = gancho.split()
grupos.insert(0, (0.0, S0 + 0.05, [(w, n < len(g0) - 1) for n, w in enumerate(g0)]))
open(f"{OUT}/gancho_swap.ass", "w").write(ass(grupos, y_pct=0.60, estilo="caja"))
fc = (f"[0:v]trim=0:{END:.3f},setpts=PTS-STARTPTS,fps=30,setsar=1,subtitles={OUT}/gancho_swap.ass:fontsdir=/root/.fonts[v];"
      f"[1:a]atrim=0:{S0 + 0.08:.3f},asetpts=PTS-STARTPTS,aresample=48000[ref];"
      f"[0:a]atrim={S0:.3f}:{END:.3f},asetpts=PTS-STARTPTS,aresample=48000[voz];"
      f"[ref][voz]acrossfade=d=0.08,loudnorm=I=-14:TP=-1.5[aout]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", F, "-i", REF, "-filter_complex", fc, "-map", "[v]", "-map", "[aout]",
                "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-c:a", "aac", "-b:a", "160k", f"{OUT}/gancho_{k}.mp4"], check=True)
print("ok", k, round(END, 2), "s; voz desde", round(S0, 2))
