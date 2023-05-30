import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class Server(BaseHTTPRequestHandler):
    HEADER_VALUE = "text/html"
    HEADER_TYPE = "Content-type"
    
    def do_GET(self):
        self.send_response(200)
        self.send_header(self.HEADER_TYPE, self.HEADER_VALUE)
        self.end_headers()
        self.wfile.write(bytes("<h1>Zenith Server</h1>", "utf-8"))
        
class WApp(Server):
    def __init__(self) -> None:
        self.port = 3000
        self.host = "127.0.0.1"
        self.devServer = False
        self.static_url_path = "static"
        self.name = "Zenith App"
        self.icon = "favicon.ico"
        self.logging = True
    
    class set:
        def headers(TYPE, VALUE):
            Server.do_GET()
            
    def serve(self):
        current_time = datetime.datetime.now()
        time_stamp = current_time.timestamp()

        webServer = HTTPServer((self.host, self.port), Server)
        if self.logging:
            print(f"Starting server at {self.host}:{self.port}")
            if self.devServer:
                print(f"\t• Running as development server")
            print(f"\t• Started {datetime.datetime.fromtimestamp(time_stamp)}")
        try:
            webServer.serve_forever()
        except  KeyboardInterrupt:
            pass

app = WApp()
app.devServer = True
app.serve()
