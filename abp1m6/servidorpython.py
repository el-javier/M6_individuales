import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Servidor levantado mediante http.server</h1>")

# Especifica el puerto en el que se ejecuta el servidor http://localhost:8000/
puerto = 8000

# Crea el servidor y configura el manejador
with socketserver.TCPServer(("", puerto), MyHandler) as httpd:
    print("Servidor levantado mediante http.server en el puerto", puerto)
    httpd.serve_forever()