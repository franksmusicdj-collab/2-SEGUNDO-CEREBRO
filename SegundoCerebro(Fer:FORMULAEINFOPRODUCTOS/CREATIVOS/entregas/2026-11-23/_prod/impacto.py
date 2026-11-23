import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from apimart import submit, wait, urls, download, submit_sfx, wait_music
foto = [json.loads(l) for l in open(os.path.join(os.path.dirname(__file__), "tareas.jsonl")) if json.loads(l)["name"] == "foto-ugc1"][-1]
foto_url = urls(wait(foto["task_id"]))[0]
v = submit("videos", "ugc1-INSERTO-celular-pared", {
  "model": "grok-imagine-1.5-video-ext", "size": "9:16", "duration": 3, "resolution": "720p",
  "image_urls": [foto_url],
  "prompt": ("Realistic vertical smartphone footage inside the same living room as the reference image. Close shot of a plain light-colored wall. "
             "A black smartphone flies in fast from the left and smashes hard against the wall: the screen shatters, glass shards and small pieces burst outward, "
             "the phone bounces off and drops to the floor. Brief slow motion exactly at the moment of impact. No people visible, no hands, no text, no logos.")})
s = submit_sfx("sfx-impacto-celular", {"model": "suno", "type": "one-shot", "audio_format": "wav",
  "prompt": "Loud close-up impact of a smartphone smashed hard against a wall: sharp crack, glass screen shattering, plastic pieces scattering on a tile floor. Dry, punchy, no music."})
d = wait(v, every=10); print("video", d["status"], "costo:", d.get("cost"), json.dumps(d.get("error"), ensure_ascii=False))
if d["status"] == "completed": download(urls(d)[0], "mente-activa-bf-ugc1/broll/inserto_celular_v1.mp4"); print("video ok")
m = wait_music(s); print("sfx", m["status"], "costo:", m.get("cost"), json.dumps(m.get("error"), ensure_ascii=False))
if m["status"] == "completed":
    mus = (m.get("result") or {}).get("music") or []
    for i, it in enumerate(mus):
        download(it["audio_url"], f"_prod/sfx_impacto_{i}.wav"); print("sfx ok", i)
