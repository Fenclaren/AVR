from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # HTTP статус 200 (OK)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hello, world!")  # Ответ в теле сообщения

# Указываем адрес и порт для сервера
host = ("localhost", 8080)

# Создаем сервер
httpd = HTTPServer(host, SimpleHTTPRequestHandler)
print(f"Сервер запущен на http://{host[0]}:{host[1]}")

# Запускаем сервер
httpd.serve_forever()
