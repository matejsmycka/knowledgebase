from http.server import BaseHTTPRequestHandler, HTTPServer
class VerboseRequestHandler(BaseHTTPRequestHandler):
    def _print_request(self):
        client_ip = self.client_address[0]
        print("\n" + "=" * 80)
        print(f"{self.command} FROM {client_ip} {self.path}")
        print("-" * 80)
        print("Headers:")
        for header, value in self.headers.items():
            print(f"  {header}: {value}")
        content_length = self.headers.get("Content-Length")
        if content_length:
            body = self.rfile.read(int(content_length))
            print("\nBody (raw bytes):")
            print(body)
            try:
                print("\nBody (decoded as UTF-8):")
                print(body.decode("utf-8"))
            except UnicodeDecodeError:
                print("Body is not valid UTF-8")
        else:
            print("\nNo request body")
        print("=" * 80 + "\n")
    def do_GET(self): self._handle()
    def do_POST(self): self._handle()
    def do_PUT(self): self._handle()
    def do_DELETE(self): self._handle()
    def do_PATCH(self): self._handle()
    def _handle(self):
        self._print_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")
if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), VerboseRequestHandler)
    print("Verbose HTTP server running on port 8000")
    server.serve_forever()
