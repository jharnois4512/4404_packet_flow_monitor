from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import ssl

class SimpleHTTPRequestHandler1(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

httpd = HTTPServer(('192.168.1.2', 443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='server.pem', server_side=True, ssl_version=ssl.PROTOCOL_TLSv1_2)

httpd.serve_forever()
