import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from apimart import submit, wait, urls, download
foto = [json.loads(l) for l in open(os.path.join(os.path.dirname(__file__), "tareas.jsonl")) if json.loads(l)["name"] == "foto-ugc1"][-1]
foto_url = urls(wait(foto["task_id"]))[0]
prompt = ("One single continuous shot, no cuts, no jump zooms, static smartphone camera propped on a shelf, vertical UGC video. "
          "The woman in image 1 is a 40-year-old Brazilian woman with a native Brazilian Portuguese accent. "
          "She stares at her phone, gets furious, and shouts in Brazilian Portuguese: Chega! Não aguento mais ficar o dia inteiro nesse celular! "
          "While shouting she throws the phone hard out of frame toward the wall on her right side, with a strong realistic arm movement. "
          "Realistic facial expression, accurate lip sync. She finishes the last word and stays silent for a moment, breathing.")
body = {"model": "wan2.7-r2v", "prompt": prompt,
        "image_with_roles": [{"url": foto_url, "role": "reference_image"}, {"url": foto_url, "role": "first_frame"}],
        "negative_prompt": "subtitles, captions, text on screen, watermark, logo, background music, extra people, tripod, cuts",
        "resolution": "720P", "duration": 5, "prompt_extend": False, "watermark": False}
tid = submit("videos", "ugc1-C1-prueba-b", body)
d = wait(tid, every=15)
print(d["status"], "costo:", d.get("cost"), json.dumps(d.get("error"), ensure_ascii=False))
if d["status"] == "completed":
    download(urls(d)[0], "mente-activa-bf-ugc1/clips/C1_v1.mp4"); print("descargado")
