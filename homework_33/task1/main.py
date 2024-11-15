from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Get request received!")


    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {
            "message": "POST request received!",
            "received_data": json.loads(post_data.decode("utf-8"))
        }

        self.wfile.write(json.dumps(response).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
