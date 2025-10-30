#!/usr/bin/env python3
"""
Simple HTTP server for local development of the AR/VR project.
Serves files with proper MIME types for WebXR compatibility.
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers for WebXR compatibility
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🐙 Kev the Annoyer server starting...")
        print(f"📡 Serving at http://localhost:{PORT}")
        print(f"🎮 Open http://localhost:{PORT} in your browser")
        print(f"🥽 For VR: Use a WebXR compatible browser (Chrome/Edge with VR headset)")
        print(f"📱 For AR: Use Chrome on Android with ARCore support")
        print("Press Ctrl+C to stop the server")
        
        # Auto-open browser
        webbrowser.open(f'http://localhost:{PORT}')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")

if __name__ == "__main__":
    main()