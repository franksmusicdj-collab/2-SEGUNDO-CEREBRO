import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from apimart import submit, wait, urls, download
foto = [json.loads(l) for l in open(os.path.join(os.path.dirname(__file__), "tareas.jsonl")) if json.loads(l)["name"] == "foto-ugc1"][-1]
ref = urls(wait(foto["task_id"]))[0]
tid = submit("images", "foto-ugc1-B-pared", {"model": "gpt-image-2", "size": "9:16", "resolution": "1k", "n": 1, "image_urls": [ref],
  "prompt": ("Same woman, same clothes, same Brazilian living room as the reference photo. Wider vertical 9:16 UGC smartphone shot, full body from the knees up, "
             "she stands on the LEFT side of the frame holding her smartphone and looking at it irritated. On the RIGHT side of the frame, about two meters from her, "
             "there is a plain empty light-beige wall clearly visible from floor to head height, with nothing hanging on it. Natural daylight, realistic, "
             "no text, no logos, no watermark.")})
d = wait(tid, every=5); print(d["status"], d.get("cost"))
download(urls(d)[0], "mente-activa-bf-ugc1/img/B_pared.png"); print("ok")
