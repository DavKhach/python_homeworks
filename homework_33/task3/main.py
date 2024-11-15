from http.server import BaseHTTPRequestHandler, HTTPServer
import json


user_data = []

class UserHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/users":
            try:
                content_length = int(self.headers["Content-Length"])
                body = self.rfile.read(content_length)
                data = json.loads(body)

                user_data.append(data)

                self.send_response(201)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                response = {"message": "User added successfully", "user": data}
                self.wfile.write(json.dumps(response).encode())
            except Exception as e:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                response = {"Error": str(e)}
                self.wfile.write(json.dumps(response).encode())


def run(server_class=HTTPServer, handler_class=UserHandler, port=8000):
    server_address = ("", port)
    https = server_class(server_address, handler_class)
    print(f"Server running on port {8000}")
    https.serve_forever()

if __name__ == "__main__":
    run()
