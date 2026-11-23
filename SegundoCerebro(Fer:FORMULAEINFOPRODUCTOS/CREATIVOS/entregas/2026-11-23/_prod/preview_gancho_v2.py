"""Gancho en un solo plano: grito + tirón + impacto dentro de la misma toma. Sonido de impacto sincronizado al cuadro del choque."""
import sys, os, json, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from subs import ass
from alinear import alinear
D = "mente-activa-bf-ugc1"; F = f"{D}/clips/C1_v2_plano_unico.mp4"; OUT = f"{D}/prod"
TXT = "Chega! Não aguento mais ficar o dia inteiro nesse celular!"
W = alinear(F, TXT)
a0 = W[0]["s"] - 0.10          # 0,10 s de aire antes de la primera palabra
a1 = 5.30                      # el celular ya cayó al piso
IMP = 3.67 - a0                # cuadro del choque contra la pared
g = lambda i, j, claves=(): (W[i]["s"] - a0, W[j]["e"] - a0, [(W[k]["w"], k in claves) for k in range(i, j + 1)])
grupos = [g(0, 0, (0,)), g(1, 3), g(4, 6), g(7, 8), g(9, 9, (9,))]
grupos[-1] = (grupos[-1][0], IMP - 0.05, grupos[-1][2])
open(f"{OUT}/gancho_v2.ass", "w").write(ass(grupos))
sh = f"between(t,{IMP:.2f},{IMP+0.35:.2f})"
fc = (f"[0:v]trim={a0:.3f}:{a1},setpts=PTS-STARTPTS,fps=30,"
      f"scale=760:1352,crop=720:1280:'20+14*sin(75*t)*{sh}':'36+12*cos(88*t)*{sh}',setsar=1,"
      f"subtitles={OUT}/gancho_v2.ass:fontsdir=/root/.fonts[v];"
      f"[0:a]atrim={a0:.3f}:{a1},asetpts=PTS-STARTPTS,aresample=48000[a0];"
      f"[1:a]atrim=7.78:9.1,asetpts=PTS-STARTPTS,afade=t=out:st=0.8:d=0.5,volume=1.8,adelay={int((IMP-0.12)*1000)}|{int((IMP-0.12)*1000)},aresample=48000[sfx];"
      f"[a0][sfx]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5[a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", F, "-i", "_prod/sfx_impacto_0.wav", "-filter_complex", fc,
                "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-c:a", "aac", "-b:a", "160k",
                f"{OUT}/preview_gancho_v2.mp4"], check=True)
print("ok", round(a1 - a0, 2), "s; impacto en", round(IMP, 2), "s")
