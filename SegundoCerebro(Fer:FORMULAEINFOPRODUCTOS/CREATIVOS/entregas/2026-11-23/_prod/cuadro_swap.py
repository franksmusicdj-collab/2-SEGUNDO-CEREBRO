"""Primer cuadro: el personaje nuestro (image 2) en el lugar de la mujer del video de referencia (image 1), misma pose y misma escena."""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from apimart import submit, wait, urls, download
L = [json.loads(l) for l in open(os.path.join(os.path.dirname(__file__), "tareas.jsonl"))]
REF0 = "https://getapib.org/image/9998204533102345-c275c3af-6ec1-4865-9311-505ec1534551-cuadro_0.png"
tids = {}
for k in sys.argv[1:]:
    foto = urls(wait([t for t in L if t["name"] == f"foto-{k}"][-1]["task_id"]))[0]
    tids[k] = submit("images", f"cuadro-swap-{k}", {"model": "gpt-image-2", "size": "9:16", "resolution": "1k", "n": 1, "image_urls": [REF0, foto],
        "prompt": ("Keep image 1 exactly the same: same room, same camera angle and framing, same wooden table, same black and gold workbook in the foreground "
                   "with the cover text MENTE ACTIVA, same green pencil, same light. Only replace the woman of image 1 with the person of image 2 "
                   "(same face, hair, age, body and clothes as image 2), in exactly the same pose: one arm raised above the head holding a black smartphone, about to throw it, angry. "
                   "Remove the caption box and its text (CHEGA DE TELA) completely, so no subtitles or added text remain. Photorealistic amateur smartphone photo.")})
for k, tid in tids.items():
    d = wait(tid, every=5); print(k, d["status"], d.get("cost"))
    if d["status"] == "completed":
        download(urls(d)[0], f"mente-activa-bf-{k}/img/D_swap.png"); print("ok", k)
