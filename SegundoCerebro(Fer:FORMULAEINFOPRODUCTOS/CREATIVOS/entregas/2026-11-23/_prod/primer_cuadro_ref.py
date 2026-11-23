"""Primer cuadro al estilo del video de referencia del usuario: cámara en mano detrás de una mesa de madera,
cuadernillo Mente Activa en primer plano, la persona de pie con el brazo levantado a punto de tirar el celular."""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from apimart import submit, wait, urls, download
CUADERNILLO = "https://getapib.org/image/9998204533093613-de1a5d6c-8e46-42dd-ac66-076c8eec1f70-cuadernillo.png"
L = [json.loads(l) for l in open(os.path.join(os.path.dirname(__file__), "tareas.jsonl"))]
def foto(k): return urls(wait([t for t in L if t["name"] == f"foto-{k}"][-1]["task_id"]))[0]
ESCENA = ("Vertical 9:16 photo, hyper-realistic amateur smartphone footage still, handheld, natural daylight. "
          "The camera is behind a dark wooden table: in the bottom foreground, lying on the table, is the black and gold spiral-bound workbook "
          "from image 2, exactly as it looks there, with a green pencil next to it. The cover text must read exactly MENTE ACTIVA (spelled M-E-N-T-E A-C-T-I-V-A) with the small line CADERNO DE ATIVIDADES, and nothing else: no page count, no numbers, no other words. Behind the table, about two meters away, the person from image 1 "
          "stands facing the camera, angry, with one arm raised above the head holding a black smartphone, about to throw it hard. "
          "Behind and to the side there is a plain wall. Real Brazilian apartment living room with a TV unit, a standing fan and big windows. "
          "No subtitles, no captions, no added text except what is printed on the workbook cover, no watermark.")
k = sys.argv[1]
tid = submit("images", f"cuadro-ref-{k}-b", {"model": "gpt-image-2", "size": "9:16", "resolution": "1k", "n": 1,
             "image_urls": [foto(k), CUADERNILLO], "prompt": ESCENA})
d = wait(tid, every=5); print(d["status"], d.get("cost"))
download(urls(d)[0], f"mente-activa-bf-{k}/img/C_ref.png"); print("ok")
