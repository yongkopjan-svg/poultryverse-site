# Poultryverse farm server — serves the site, receives every record change,
# writes farm-live.json. Seed backup data.json is never modified.
import json, os, sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

ROOT = os.path.dirname(os.path.abspath(__file__))
LIVE = os.path.join(ROOT, "farm-live.json")
SEED = os.path.join(ROOT, "data.json")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8621

class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw): super().__init__(*a, directory=ROOT, **kw)

    def _json(self, code, obj):
        b = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(b)

    def _read_body(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n).decode("utf-8")) if n else None

    def do_GET(self):
        if self.path == "/api/data":
            try:
                with open(LIVE, "r", encoding="utf-8") as f:
                    return self._json(200, json.load(f))
            except FileNotFoundError:
                with open(SEED, "r", encoding="utf-8") as f:
                    return self._json(200, json.load(f))
            except Exception as e:
                return self._json(500, {"error": str(e)})
        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/save":
            try:
                data = self._read_body()
                if not isinstance(data, dict): return self._json(400, {"error": "bad body"})
                tmp = LIVE + ".tmp"
                with open(tmp, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False)
                os.replace(tmp, LIVE)
                return self._json(200, {"ok": True})
            except Exception as e:
                return self._json(500, {"error": str(e)})
        if self.path == "/api/reset":
            try:
                if os.path.exists(LIVE): os.remove(LIVE)
                with open(SEED, "r", encoding="utf-8") as f:
                    return self._json(200, json.load(f))
            except Exception as e:
                return self._json(500, {"error": str(e)})
        return self._json(404, {"error": "no route"})

    def log_message(self, fmt, *args): pass

print(f"Poultryverse server on http://localhost:{PORT}  (records -> {os.path.basename(LIVE)})")
ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
