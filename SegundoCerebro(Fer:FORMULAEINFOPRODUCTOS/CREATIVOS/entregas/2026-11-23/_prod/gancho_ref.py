import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from apimart import submit, wait, urls, download
L = [json.loads(l) for l in open(os.path.join(os.path.dirname(__file__), "tareas.jsonl"))]
fotoA = urls(wait([t for t in L if t["name"] == "foto-ugc1"][-1]["task_id"]))[0]
PRIMER = "https://getapib.org/image/9998204532956345-c560f315-3331-4a9c-9ebd-082c7989a0be-C_ref.png"
VOZ = "https://getapib.org/audio/9998204533657278-594575d8-f602-4a04-9b8b-1c0987a2be26-muestra_grito.wav"
prompt = ("Amateur handheld smartphone video, natural hand shake, one continuous take with no cuts. It starts exactly like the first frame: "
          "the woman from image 1 stands behind a wooden table with a workbook on it, arm raised holding a phone. Immediately, at the very first second, "
          "she throws the phone hard and fast toward the plain wall behind her. The camera quickly pans to follow the throw: the phone, small and at real size, "
          "flies at real speed, hits the wall in the background with a loud crack and drops to the floor. No slow motion, no close-up of the phone. "
          "The camera pans back to her; she turns to the camera, furious, and shouts in Brazilian Portuguese with a native accent: "
          "Chega! Não aguento mais ficar o dia inteiro nesse celular! Realistic expressions, accurate lip sync, the workbook stays on the table in the foreground.")
tid = submit("videos", "ugc1-C1-ref", {"model": "wan2.7-r2v", "prompt": prompt,
    "image_with_roles": [{"url": fotoA, "role": "reference_image", "reference_voice": VOZ}, {"url": PRIMER, "role": "first_frame"}],
    "negative_prompt": "cuts, scene change, slow motion, close-up insert, subtitles, captions, text on screen, watermark, logo, background music, extra people, tripod, oversized phone",
    "resolution": "720P", "duration": 7, "prompt_extend": False, "watermark": False})
d = wait(tid, every=15)
print(d["status"], "costo:", d.get("cost"), json.dumps(d.get("error"), ensure_ascii=False))
if d["status"] == "completed":
    download(urls(d)[0], "mente-activa-bf-ugc1/clips/C1_v3_ref.mp4"); print("descargado")
