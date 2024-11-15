from http.server import BaseHTTPRequestHandler, HTTPServer
import json


users = [
    {"id": 1, "name": "Alice", "email": "alice@mail.com"},
    {"id": 2, "name": "Bob", "email": "bob@mail.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@mail.com"}
]


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/users"):
            if '?' in self.path:
                params = dict(par.split('=') for par in self.path.split('?')[1].split('&'))
                email = params.get("email")

                if email:
                    matching_user = next((user for user in users if user["email"] == email), None)
                    if matching_user:
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(bytes(json.dumps(matching_user), "utf-8"))
                    else:
                        self.send_response(404)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(bytes("User not found", "utf-8"))
                else:
                    self.send_response(400)
                    self.send_header("Content-type", "text/plain")
                    self.end_headers()
                    self.wfile.write(bytes("Email parameter is required", "utf-8"))
            else:
                self.send_response(400)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes("Query parameters are required", "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Not found", "utf-8"))


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {8000}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
