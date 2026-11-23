"""Alineación forzada MMS_FA contra el guion: devuelve los tiempos de cada palabra."""
import re, sys, json, subprocess, tempfile, unicodedata
import torch, torchaudio, soundfile as sf
_B = torchaudio.pipelines.MMS_FA
_M = _B.get_model(); _T = _B.get_tokenizer(); _A = _B.get_aligner()

def _norm(w):
    w = unicodedata.normalize("NFKD", w.lower())
    w = "".join(c for c in w if not unicodedata.combining(c))
    return re.sub(r"[^a-z']", "", w)

def alinear(media, texto):
    with tempfile.NamedTemporaryFile(suffix=".wav") as f:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", media, "-ar", "16000", "-ac", "1", f.name], check=True)
        a, sr = sf.read(f.name, dtype="float32")
    orig = texto.split()
    pares = [(o, _norm(o)) for o in orig if _norm(o)]
    wav = torch.from_numpy(a).unsqueeze(0)
    with torch.inference_mode():
        em, _ = _M(wav)
        spans = _A(em[0], _T([n for _, n in pares]))
    r = wav.shape[1] / em.shape[1] / sr
    return [{"w": o, "s": round(sp[0].start * r, 3), "e": round(sp[-1].end * r, 3)} for (o, _), sp in zip(pares, spans)]

if __name__ == "__main__":
    print(json.dumps(alinear(sys.argv[1], sys.argv[2]), ensure_ascii=False))
