import urllib.request
import json

req_local = urllib.request.Request("http://localhost:8000/generate")
with urllib.request.urlopen(req_local) as response:
    data = json.loads(response.read().decode())

payload = {
    "team": "9",
    "by": "Layan",
    "model": data["model"],
    "image": "ghcr.io/layanhth/aidc-team9exercise2-warmup:latest",
    "tokens_per_sec": data["tokens_per_sec"],
    "sample": data["sample"]
}
req_board = urllib.request.Request(
    "https://aidc.nadir.sh/model",
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    },
    method='POST'
)

with urllib.request.urlopen(req_board) as response:
    print("Submitted successfully! Response:", response.read().decode())
