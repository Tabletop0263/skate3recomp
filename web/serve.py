#!/usr/bin/env python3
"""Serve this folder with the headers SharedArrayBuffer needs. Run: python3 serve.py
Then open http://localhost:8000/skate3.html in Chrome."""
import http.server, socketserver

class H(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      '.wasm': 'application/wasm', '.js': 'text/javascript'}
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(('127.0.0.1', 8000), H) as s:
    print('http://localhost:8000/skate3.html')
    s.serve_forever()
