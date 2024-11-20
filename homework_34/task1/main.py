from http.server import BaseHTTPRequestHandler, HTTPServer
import json


users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
        ]


products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
           ]

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/users":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(users).encode())
        elif self.path.startswith("/users/"):
            user_id = int(self.path.split("/")[-1])
            user = next((u for u in users if u["id"] == user_id), None)
            if user:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(user).encode())
            else:
                self.send_response(404)
                self.end_headers()
        elif self.path == "/products":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(products).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/users":
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            user = json.loads(body)
            user["id"] = max(u["id"] for u in users) + 1
            users.append(user)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(user).encode())
        elif self.path == "/products":
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            product = json.loads(body)
            product["id"] = max(p["id"] for p in products) + 1
            products.append(product)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(product).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_PUT(self):
        if self.path.startswith("/users/"):
            user_id = int(self.path.split("/")[-1])
            user = next((u for u in users if u["id"] == user_id), None)
            if user:
                content_length = int(self.headers["Content-Length"])
                body = self.rfile.read(content_length)
                updated_user = json.loads(body)
                user.update(updated_user)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(user).encode())
            else:
                self.send_response(404)
                self.end_headers()
        elif self.path.startswith("/products/"):
            product_id = int(self.path.split("/")[-1])
            product = next((p for p in products if p["id"] == product_id), None)
            if product:
                content_length = int(self.headers["Content-Length"])
                body = self.rfile.read(content_length)
                updated_product = json.loads(body)
                product.update(updated_product)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(product).encode())
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):
        if self.path.startswith("/users/"):
            user_id = int(self.path.split("/")[-1])
            user = next((u for u in users if u["id"] == user_id), None)
            if user:
                users.remove(user)
                self.send_response(204)
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
        elif self.path.startswith("/products/"):
            product_id = int(self.path.split("/")[-1])
            product = next((p for p in products if p["id"] == product_id), None)
            if product:
                products.remove(product)
                self.send_response(204)
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("localhost", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server started on http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
