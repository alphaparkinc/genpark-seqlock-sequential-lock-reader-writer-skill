import sys
import json
from client import SeqLock

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "read_write":
        sl = SeqLock()
        sl.write(params.get("key", "k"), params.get("val", 0))
        return sl.read(params.get("key", "k"))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == '__main__':
    main()
