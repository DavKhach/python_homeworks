from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        query_start = path.find("?")

        if query_start == -1:
            query_string = ""
        else:
            query_string = path[query_start + 1:]

        query_params = {}
        if query_string:
            pairs = query_string.split("&")
            for pair in pairs:
                if "=" in pair:
                    key, value = pair.split("=")
                    query_params[key] = value

        email = query_params.get("email", None)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        if email:
            self.wfile.write(f"Extracted email: {email}".encode())
        else:
            self.wfile.write(b"Email parameter not found")


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {8000}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
