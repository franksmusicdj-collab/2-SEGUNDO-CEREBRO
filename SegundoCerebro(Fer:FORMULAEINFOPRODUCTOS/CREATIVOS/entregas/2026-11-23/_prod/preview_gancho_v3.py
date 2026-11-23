"""Gancho v3: misma toma única, pero desde que suelta el celular la acción va a 2,5x con desenfoque de movimiento (la voz no se acelera)."""
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from subs import ass
from alinear import alinear
D = "mente-activa-bf-ugc1"; F = f"{D}/clips/C1_v2_plano_unico.mp4"; OUT = f"{D}/prod"
W = alinear(F, "Chega! Não aguento mais ficar o dia inteiro nesse celular!")
a0 = W[0]["s"] - 0.10
CUT = 3.45            # fin de la voz (3,37) + aire; desde acá solo hay acción
END = 5.30            # celular en el piso
SP = 2.5
IMP_ORIG = 3.67
segA = CUT - a0
IMP = segA + (IMP_ORIG - CUT) / SP
dur = segA + (END - CUT) / SP
g = lambda i, j, claves=(): (W[i]["s"] - a0, W[j]["e"] - a0, [(W[k]["w"], k in claves) for k in range(i, j + 1)])
grupos = [g(0, 0, (0,)), g(1, 3), g(4, 6), g(7, 8), g(9, 9, (9,))]
grupos[-1] = (grupos[-1][0], IMP - 0.02, grupos[-1][2])
open(f"{OUT}/gancho_v3.ass", "w").write(ass(grupos))
sh = f"between(t,{IMP:.2f},{IMP+0.30:.2f})"
fc = (f"[0:v]split[s1][s2];"
      f"[s1]trim={a0:.3f}:{CUT},setpts=PTS-STARTPTS,fps=30[va];"
      f"[s2]trim={CUT}:{END},setpts=(PTS-STARTPTS)/{SP},fps=75,tmix=frames=3:weights='1 2 1',fps=30[vb];"
      f"[va][vb]concat=n=2:v=1:a=0,scale=760:1352,crop=720:1280:'20+16*sin(75*t)*{sh}':'36+14*cos(88*t)*{sh}',setsar=1,"
      f"subtitles={OUT}/gancho_v3.ass:fontsdir=/root/.fonts[v];"
      f"[0:a]atrim={a0:.3f}:{CUT},asetpts=PTS-STARTPTS,afade=t=out:st={segA-0.06:.2f}:d=0.06,aresample=48000,apad=whole_dur={dur:.3f}[a0];"
      f"[1:a]atrim=7.78:9.1,asetpts=PTS-STARTPTS,afade=t=out:st=0.8:d=0.5,volume=1.8,adelay={int((IMP-0.12)*1000)}|{int((IMP-0.12)*1000)},aresample=48000[sfx];"
      f"[a0][sfx]amix=inputs=2:normalize=0:duration=longest,atrim=0:{dur+0.4:.3f},loudnorm=I=-14:TP=-1.5[a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", F, "-i", "_prod/sfx_impacto_0.wav", "-filter_complex", fc,
                "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-c:a", "aac", "-b:a", "160k",
                "-shortest", f"{OUT}/preview_gancho_v3.mp4"], check=True)
print("ok", round(dur, 2), "s; impacto en", round(IMP, 2), "s")
