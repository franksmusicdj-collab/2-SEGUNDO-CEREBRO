"""Gancho copiado del video de referencia: toma única sin acelerar (el ritmo es el del original).
Texto de gancho "CHEGA DE TELA." desde el primer cuadro (como la referencia) y después los subtítulos de lo que dice."""
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from subs import ass
from alinear import alinear
D = "mente-activa-bf-ugc1"; F = f"{D}/clips/C1_videoref3s.mp4"; OUT = f"{D}/prod"
W = alinear(F, "Chega! Não aguento mais ficar o dia inteiro nesse celular!")
END = W[-1]["e"] + 0.16
PARED, PISO = 0.90, 1.30          # mismos tiempos de impacto que el video de referencia
g = lambda i, j, cl=(): (W[i]["s"], W[j]["e"] + 0.05, [(W[k]["w"], k in cl) for k in range(i, j + 1)])
grupos = [(0.0, W[0]["s"] - 0.05, [("Chega", 1), ("de", 1), ("tela.", 0)]),
          g(0, 0, (0,)), g(1, 3), g(4, 6), g(7, 8), g(9, 9, (9,))]
open(f"{OUT}/gancho_videoref.ass", "w").write(ass(grupos, y_pct=0.60, estilo="caja"))
fc = (f"[0:v]trim=0:{END:.3f},setpts=PTS-STARTPTS,fps=30,setsar=1,subtitles={OUT}/gancho_videoref.ass:fontsdir=/root/.fonts[v];"
      f"[0:a]atrim=0:{END:.3f},asetpts=PTS-STARTPTS,aresample=48000[voz];"
      f"[1:a]atrim=7.78:9.0,asetpts=PTS-STARTPTS,afade=t=out:st=0.7:d=0.5,volume=1.8,adelay={int((PARED-0.12)*1000)}|{int((PARED-0.12)*1000)},aresample=48000[s1];"
      f"[2:a]atrim=5.65:6.5,asetpts=PTS-STARTPTS,afade=t=out:st=0.5:d=0.35,volume=0.9,adelay={int((PISO-0.12)*1000)}|{int((PISO-0.12)*1000)},aresample=48000[s2];"
      f"[voz][s1][s2]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5[aout]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", F, "-i", "_prod/sfx_impacto_0.wav", "-i", "_prod/sfx_impacto_1.wav", "-filter_complex", fc,
                "-map", "[v]", "-map", "[aout]", "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-c:a", "aac", "-b:a", "160k",
                f"{OUT}/preview_gancho_videoref.mp4"], check=True)
print("ok", round(END, 2), "s")
