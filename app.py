from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>Привет! Это мой первый сайт 🚀</h1>".encode())


print("Сайт запущен: http://localhost:8000")
HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()