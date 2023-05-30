import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
    HEADER_VALUE = "text/html"
    HEADER_TYPE = "Content-type"
    ROUTES = []
        
    def do_GET(self):
        self.send_response(200)
        self.send_header(self.HEADER_TYPE, self.HEADER_VALUE)
        self.end_headers()

        for route, response in self.ROUTES:
            if self.path == f"/{route}":
                self.wfile.write(response.encode("utf-8"))
                return

        self.wfile.write(b"<h1>Zenith Server</h1>")
    
    def getPath(self, routeName):
        if self.path == f"/{routeName}":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("<b> Hello World !</b>"
                             + "<br><br>Current time: " + str(datetime.datetime.now()))
        
class WApp(Server):

    def __init__(self) -> None:
        self.port = 3000
        self.host = 'localhost'
        self.devServer = False
        self.static_url_path = "static"
        self.name = "Zenith App"
        self.logging = True
        self.webServer = HTTPServer((self.host, self.port), Server)
    
    def get(self, route, response):
        Server.ROUTES.append((route, response))
        
    def serve(self):
        current_time = datetime.datetime.now()
        time_stamp = current_time.timestamp()
        print(f"Starting server at http://{self.host}:{self.port}")
        if self.devServer:
            print(f"\t• Running as development server")
        print(f"\t• Started {datetime.datetime.fromtimestamp(time_stamp)}\n")
        try:
            self.webServer.serve_forever()
        except KeyboardInterrupt:
            pass
        self.webServer.server_close()
        print("Server stopped.")


app = WApp()

app.get("/hello", "hello")
app.serve()
