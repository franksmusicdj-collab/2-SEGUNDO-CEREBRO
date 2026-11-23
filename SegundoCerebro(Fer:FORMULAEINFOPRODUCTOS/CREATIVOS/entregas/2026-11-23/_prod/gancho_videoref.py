"""Gancho copiando el movimiento del video de referencia del usuario (video 1): cámara, tirón y ritmo.
Cambia el personaje (image 1, con su voz) y mantiene el cuadernillo (image 2) en la mesa todo el tiempo."""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from apimart import submit, wait, urls, download
L = [json.loads(l) for l in open(os.path.join(os.path.dirname(__file__), "tareas.jsonl"))]
k = sys.argv[1]; frase = sys.argv[2]; voz = sys.argv[3]; desc = sys.argv[4]
foto = urls(wait([t for t in L if t["name"] == f"foto-{k}"][-1]["task_id"]))[0]
VIDEO = sys.argv[5] if len(sys.argv) > 5 else "https://getapib.org/video/9998204532601161-1582684c-fdd1-467d-8141-cf32de2f2fd8-referencia_gancho_7s.mp4"
TAG = sys.argv[6] if len(sys.argv) > 6 else "videoref"
PRIMER = sys.argv[7] if len(sys.argv) > 7 else None
CUADERNILLO = "https://getapib.org/image/9998204533093613-de1a5d6c-8e46-42dd-ac66-076c8eec1f70-cuadernillo.png"
prompt = (f"Video 1 shows only the throw. Recreate its first seconds shot for shot: the same amateur handheld smartphone camera behind a wooden table, the same camera movement, "
          f"the same timing and the same way of throwing the phone hard against the wall and of the camera following it, at the same real speed. "
          f"The person is NOT the woman of video 1: it is {desc} from image 1 (face, hair, body, clothes and voice of image 1), exactly as in the first frame. "
          f"The black and gold spiral workbook from image 2, with the cover text MENTE ACTIVA, lies on the table in the foreground during the whole video. "
          f"After the throw, the person turns to the camera, furious, and says in Brazilian Portuguese with a native accent: {frase} "
          f"Do not copy any subtitles or captions from video 1. Realistic expressions, accurate lip sync.")
item = {"url": foto, "role": "reference_image"}
if voz != "-": item["reference_voice"] = voz
tid = submit("videos", f"{k}-C1-{TAG}", {"model": "wan2.7-r2v", "prompt": prompt,
    "image_with_roles": [item, {"url": CUADERNILLO, "role": "reference_image"}] + ([{"url": PRIMER, "role": "first_frame"}] if PRIMER else []), "video_urls": [VIDEO],
    "negative_prompt": "subtitles, captions, text on screen, burned-in text, watermark, extra people, slow motion, oversized phone, cuts",
    "resolution": "720P", "duration": 7, "size": "9:16", "prompt_extend": False, "watermark": False})
d = wait(tid, every=15, max_s=2400)
print(d["status"], "costo:", d.get("cost"), json.dumps(d.get("error"), ensure_ascii=False))
if d["status"] == "completed":
    download(urls(d)[0], f"mente-activa-bf-{k}/clips/C1_{TAG}.mp4"); print("descargado")
