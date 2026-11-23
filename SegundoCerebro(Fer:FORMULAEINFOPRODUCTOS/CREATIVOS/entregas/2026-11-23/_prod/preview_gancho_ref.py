"""Gancho estilo referencia del usuario: toma única en mano. Tramo sin voz (pared vacía + paneo de vuelta) acelerado 2x; voz intacta."""
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from subs import ass
from alinear import alinear
D = "mente-activa-bf-ugc1"; F = f"{D}/clips/C1_v3_ref.mp4"; OUT = f"{D}/prod"
W = alinear(F, "Chega! Não aguento mais ficar o dia inteiro nesse celular!")
P1, P2 = 2.70, W[0]["s"] - 0.10            # tramo sin voz a acelerar
END = W[-1]["e"] + 0.16
SP = 2.0
mapa = lambda t: t if t <= P1 else (P1 + (t - P1) / SP if t <= P2 else P1 + (P2 - P1) / SP + (t - P2))
IMP_PARED, IMP_PISO = mapa(1.95), mapa(2.55)
dur = mapa(END)
g = lambda i, j, cl=(): (mapa(W[i]["s"]), mapa(W[j]["e"]) + 0.05, [(W[k]["w"], k in cl) for k in range(i, j + 1)])
grupos = [g(0, 0, (0,)), g(1, 3), g(4, 6), g(7, 8), g(9, 9, (9,))]
open(f"{OUT}/gancho_ref.ass", "w").write(ass(grupos, y_pct=0.60, estilo="caja"))
fc = (f"[0:v]split=3[a][b][c];"
      f"[a]trim=0:{P1},setpts=PTS-STARTPTS[va];[b]trim={P1}:{P2:.3f},setpts=(PTS-STARTPTS)/{SP}[vb];[c]trim={P2:.3f}:{END:.3f},setpts=PTS-STARTPTS[vc];"
      f"[va][vb][vc]concat=n=3:v=1:a=0,fps=30,setsar=1,subtitles={OUT}/gancho_ref.ass:fontsdir=/root/.fonts[v];"
      f"[0:a]asplit=3[x][y][z];[x]atrim=0:{P1},asetpts=PTS-STARTPTS,volume=0.6[xa];[y]atrim={P1}:{P2:.3f},asetpts=PTS-STARTPTS,atempo={SP},volume=0.6[ya];"
      f"[z]atrim={P2:.3f}:{END:.3f},asetpts=PTS-STARTPTS[za];[xa][ya][za]concat=n=3:v=0:a=1,aresample=48000[voz];"
      f"[1:a]atrim=7.78:9.0,asetpts=PTS-STARTPTS,afade=t=out:st=0.7:d=0.5,volume=1.8,adelay={int((IMP_PARED-0.12)*1000)}|{int((IMP_PARED-0.12)*1000)},aresample=48000[s1];"
      f"[2:a]atrim=5.65:6.5,asetpts=PTS-STARTPTS,afade=t=out:st=0.5:d=0.35,volume=0.9,adelay={int((IMP_PISO-0.12)*1000)}|{int((IMP_PISO-0.12)*1000)},aresample=48000[s2];"
      f"[voz][s1][s2]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5[aout]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", F, "-i", "_prod/sfx_impacto_0.wav", "-i", "_prod/sfx_impacto_1.wav", "-filter_complex", fc,
                "-map", "[v]", "-map", "[aout]", "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-c:a", "aac", "-b:a", "160k",
                f"{OUT}/preview_gancho_ref.mp4"], check=True)
print("ok", round(dur, 2), "s; pared", round(IMP_PARED, 2), "piso", round(IMP_PISO, 2))
