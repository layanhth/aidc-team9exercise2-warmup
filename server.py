import importlib
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

routes = {}
for file in os.listdir("routes"):
    if file.endswith(".py"):
        mod_name = file[:-3]
        mod = importlib.import_module(f"routes.{mod_name}")
        if hasattr(mod, "PATH") and hasattr(mod, "handle"):
            routes[mod.PATH] = mod.handle

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in routes:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            res = routes[self.path]()
            self.wfile.write(json.dumps(res).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), RequestHandler)
    server.serve_forever()
