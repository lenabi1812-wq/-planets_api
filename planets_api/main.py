from http.server import BaseHTTPRequestHandler, HTTPServer
import json

planets = [
    {
        "name": "Земля",
        "type": "Каменистая планета",
        "distance": "149,6 млн км"
    },
    {
        "name": "Марс",
        "type": "Каменистая планета",
        "distance": "227,9 млн км"
    },
    {
        "name": "Юпитер",
        "type": "Газовый гигант",
        "distance": "778,5 млн км"
    }
]

class PlanetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/planets':
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()

            response = json.dumps(planets, ensure_ascii=False)
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write("<h1>404 Not Found</h1>".encode('utf-8'))

if __name__ == '__main__':
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, PlanetHandler)
    print('Сервер запущен на http://127.0.0.1:8000/planets')
    print('Для остановки нажмите Ctrl+C')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nСервер остановлен.')
        httpd.server_close()