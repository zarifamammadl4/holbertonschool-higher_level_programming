#!/usr/bin/python3
"""
A simple API using Python's http.server module.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "0.0.0.0"
PORT = 8000


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom request handler for a simple API."""

    def _set_headers(self, status_code=200, content_type="text/plain"):
        """Helper to set HTTP headers."""
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self._set_headers(content_type="application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self._set_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self._set_headers(content_type="application/json")
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self._set_headers(status_code=404)
            self.wfile.write(b"Endpoint not found")


def run_server():
    """Start the HTTP server."""
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running at http://{HOST}:{PORT}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()


if __name__ == "__main__":
    run_server()

