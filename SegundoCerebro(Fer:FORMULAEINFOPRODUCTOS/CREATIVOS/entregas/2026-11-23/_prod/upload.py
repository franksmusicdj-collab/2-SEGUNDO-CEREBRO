import json, subprocess, sys
def subir(path, kind):
    out = subprocess.run(["curl", "-s", "-m", "120", "-X", "POST", f"https://api.apimart.ai/v1/uploads/{kind}?retention_days=3",
                          "-H", "Authorization: Bearer proxy-injected", "-F", f"file=@{path}"], capture_output=True, text=True).stdout
    return json.loads(out)
if __name__ == "__main__":
    print(json.dumps(subir(sys.argv[1], sys.argv[2]), ensure_ascii=False))
