"""Cliente mínimo de ApiMart: manda tareas, guarda el ID apenas sale, poll y descarga con reanudación."""
import json, os, sys, time, subprocess, urllib.request
API = "https://api.apimart.ai"
H = {"Authorization": "Bearer proxy-injected", "Content-Type": "application/json"}
LOG = os.path.join(os.path.dirname(__file__), "tareas.jsonl")

def _req(method, path, body=None):
    r = urllib.request.Request(API + path, method=method, headers=H,
                               data=json.dumps(body).encode() if body else None)
    with urllib.request.urlopen(r, timeout=120) as resp:
        return json.loads(resp.read())

def submit(kind, name, body):
    out = _req("POST", f"/v1/{kind}/generations", body)
    tid = out["data"][0]["task_id"]
    with open(LOG, "a") as f:
        f.write(json.dumps({"name": name, "task_id": tid, "model": body["model"], "t": time.time()}) + "\n")
    print("enviada", name, tid, flush=True)
    return tid

def wait(tid, every=10, max_s=1800):
    t0 = time.time()
    while time.time() - t0 < max_s:
        d = _req("GET", f"/v1/tasks/{tid}")["data"]
        if d["status"] in ("completed", "failed", "cancelled"):
            return d
        time.sleep(every)
    raise TimeoutError(tid)

def download(url, dest, nuevo=True):
    """nuevo=True: borra el archivo previo (otra generación). Para reanudar una descarga cortada, nuevo=False."""
    if nuevo and os.path.exists(dest):
        os.remove(dest)
    for _ in range(4):
        if subprocess.run(["curl", "-sL", "-C", "-", "--retry", "3", "--max-time", "300", "-o", dest, url]).returncode == 0:
            return dest
    raise RuntimeError("descarga fallida " + dest)

def urls(d):
    res = d.get("result") or {}
    out = []
    for k in ("images", "videos"):
        for it in res.get(k, []) or []:
            u = it.get("url")
            out += u if isinstance(u, list) else [u]
    return [u for u in out if u]

def submit_sfx(name, body):
    out = _req("POST", "/v1/music/generations/sounds", body)
    tid = out["data"][0]["task_id"]
    with open(LOG, "a") as f:
        f.write(json.dumps({"name": name, "task_id": tid, "model": "suno-sounds", "t": time.time()}) + "\n")
    print("enviada", name, tid, flush=True)
    return tid

def wait_music(tid, every=4, max_s=900):
    t0 = time.time()
    while time.time() - t0 < max_s:
        d = _req("GET", f"/v1/music/tasks/{tid}")["data"]
        if d["status"] in ("completed", "failed"):
            return d
        time.sleep(every)
    raise TimeoutError(tid)
