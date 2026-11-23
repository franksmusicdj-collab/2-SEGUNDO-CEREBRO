import sys, os, json, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from subs import ass
D = "mente-activa-bf-ugc1"; OUT = f"{D}/prod"; os.makedirs(OUT, exist_ok=True)
a0, a1 = 0.70, 3.513 + 0.16          # bordes por alineación forzada (0,10 s antes / 0,16 s después)
i0, i1 = 0.25, 1.45                  # tramo del inserto; impacto visual ~0,58 s del inserto
seg = a1 - a0; imp = seg + (0.58 - i0)
grupos = [(0.80, 1.40, [("Chega!", 1)]), (1.77, 2.29, [("Não", 0), ("aguento", 0), ("mais", 0)]),
          (2.29, 2.57, [("ficar", 0), ("o", 0), ("dia", 0)]), (2.57, 3.19, [("inteiro", 0), ("nesse", 0)]),
          (3.19, a1, [("celular!", 1)])]
grupos = [(s - a0, e - a0, w) for s, e, w in grupos]
open(f"{OUT}/gancho.ass", "w").write(ass(grupos))
shake = f"crop=720:1280:'20+12*sin(70*t)*between(t,{imp-seg:.2f},{imp-seg+0.4:.2f})':'20+10*cos(83*t)*between(t,{imp-seg:.2f},{imp-seg+0.4:.2f})'"
fc = (f"[0:v]trim={a0}:{a1},setpts=PTS-STARTPTS,scale=720:1280,fps=30,setsar=1[v0];"
      f"[1:v]trim={i0}:{i1},setpts=PTS-STARTPTS,scale=760:1336:force_original_aspect_ratio=increase,crop=760:1320,{shake},scale=720:1280,fps=30,setsar=1[v1];"
      f"[v0][v1]concat=n=2:v=1:a=0[vc];[vc]subtitles={OUT}/gancho.ass:fontsdir=/root/.fonts[v];"
      f"[0:a]atrim={a0}:{a1},asetpts=PTS-STARTPTS,aresample=48000[a0];"
      f"[2:a]atrim=7.78:9.1,asetpts=PTS-STARTPTS,afade=t=out:st=0.8:d=0.5,volume=1.6,adelay={int((imp-0.12)*1000)}|{int((imp-0.12)*1000)},aresample=48000[sfx];"
      f"[a0]apad=whole_dur={seg + i1 - i0}[a0p];[a0p][sfx]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5[a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{D}/clips/C1_v1.mp4", "-i", f"{D}/broll/inserto_celular_v1.mp4",
                "-i", "_prod/sfx_impacto_0.wav", "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
                "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-c:a", "aac", "-b:a", "160k", f"{OUT}/preview_gancho.mp4"], check=True)
print("ok", seg + i1 - i0, "s; impacto en", round(imp, 2))
