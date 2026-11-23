import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from apimart import submit, wait, download, urls
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = ("Vertical 9:16 photo, hyper-realistic UGC smartphone footage still, natural indoor daylight, "
        "medium shot from the waist up, face in the upper third of the frame, camera at eye level as if the phone "
        "filming is propped on a shelf. The person holds a smartphone in one hand and looks at its screen with a "
        "bored, irritated expression. Real Brazilian home, slightly lived-in, warm tones. No text, no captions, "
        "no logos, no watermark, no brand names visible.")
P = {
 "ugc1": "A 40-year-old attractive, expressive Brazilian woman, light-brown skin, wavy dark hair, casual t-shirt and jeans, standing in a modern Brazilian living room with plants and a sofa behind her. " + BASE,
 "ugc2": "A friendly 55-year-old Brazilian woman with a natural look, short silver-streaked hair, floral blouse, sitting on a beige sofa in a cozy traditional Brazilian living room with family photos on a side table. " + BASE,
 "ugc3": "A charismatic 50-year-old Brazilian man, tanned skin, short salt-and-pepper hair and light beard, casual polo shirt, standing in a bright Brazilian apartment living room with a TV unit and a balcony door behind him. " + BASE,
}
tids = {k: submit("images", f"foto-{k}", {"model": "gpt-image-2", "prompt": v, "size": "9:16", "resolution": "1k", "n": 1}) for k, v in P.items()}
for k, tid in tids.items():
    d = wait(tid, every=5)
    print(k, d["status"], "costo:", d.get("cost"), d.get("credits_cost"))
    if d["status"] == "completed":
        u = urls(d)[0]
        dest = os.path.join(B, f"mente-activa-bf-{k}", "img", "A.png")
        download(u, dest); print("ok", dest, u)
    else:
        print(json.dumps(d.get("error"), ensure_ascii=False))
