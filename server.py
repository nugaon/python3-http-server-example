from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json

SERVER = "127.0.0.1"
PORT = 8080

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def sort_arrays(self, payload):
        try:
            sort_keys = payload['sortKeys']
            sorted_values = {key: sorted(payload['payload'][key]) for key in sort_keys}

            return {**payload['payload'], **sorted_values}
        except KeyError:
            return "Badly specified keys"

    def do_GET(self):
        if self.path != '/path':
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'This service only gives \'/path\' EP.')
            return

        self.send_response(405)
        self.end_headers()
        self.wfile.write(b'This EP can be called only with POST method')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        body_object = json.loads(body)
        answer = self.sort_arrays(body_object)
        self.send_response(200)
        self.end_headers()
        answer_json = json.dumps(answer)
        response = BytesIO()
        response.write(answer_json.encode())
        self.wfile.write(response.getvalue())


with HTTPServer((SERVER, PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving on address", SERVER)
    print("serving at port", PORT)
    httpd.serve_forever()
