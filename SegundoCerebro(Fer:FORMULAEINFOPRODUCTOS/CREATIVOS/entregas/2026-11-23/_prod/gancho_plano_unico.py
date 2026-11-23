import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from apimart import submit, wait, urls, download
L = [json.loads(l) for l in open(os.path.join(os.path.dirname(__file__), "tareas.jsonl"))]
fotoA = urls(wait([t for t in L if t["name"] == "foto-ugc1"][-1]["task_id"]))[0]
FOTO_B = "https://getapib.org/image/9998204533655354-104fcf5e-4afb-47f4-9c7b-1b60acb00cc3-B_pared.png"
VOZ = "https://getapib.org/audio/9998204533657278-594575d8-f602-4a04-9b8b-1c0987a2be26-muestra_grito.wav"
prompt = ("One single continuous shot, no cuts, no camera change, static vertical smartphone camera. Image 1 shows the woman's face and identity. "
          "The scene starts exactly like the first frame: the 40-year-old Brazilian woman stands on the left looking furious at her phone, "
          "with a plain empty wall on the right side of the frame. She shouts in Brazilian Portuguese with a native accent: "
          "Chega! Não aguento mais ficar o dia inteiro nesse celular! "
          "Right after the last word she throws the phone overhand with strong force at the wall on the right. Within the same shot, the phone visibly "
          "hits the wall, the screen shatters, pieces fly off and the broken phone falls to the floor. She stays in frame, breathing hard, still angry. "
          "Realistic physics, realistic facial expression, accurate lip sync.")
tid = submit("videos", "ugc1-C1-plano-unico", {"model": "wan2.7-r2v", "prompt": prompt,
    "image_with_roles": [{"url": fotoA, "role": "reference_image", "reference_voice": VOZ}, {"url": FOTO_B, "role": "first_frame"}],
    "negative_prompt": "cuts, scene change, close-up insert, subtitles, captions, text on screen, watermark, logo, background music, extra people, tripod",
    "resolution": "720P", "duration": 6, "prompt_extend": False, "watermark": False})
d = wait(tid, every=15)
print(d["status"], "costo:", d.get("cost"), json.dumps(d.get("error"), ensure_ascii=False))
if d["status"] == "completed":
    download(urls(d)[0], "mente-activa-bf-ugc1/clips/C1_v2_plano_unico.mp4"); print("descargado")
