import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

class CustomServer(BaseHTTPRequestHandler):
    
    HEADER_VALUE = "text/html"
    HEADER_TYPE = "Content-type"
    BUILT_ROUTES = {}

    def do_GET(self):
        self.send_response(200)
        self.send_header(self.HEADER_TYPE, self.HEADER_VALUE)
        self.end_headers()

        path = self.path[1:]  # Remove the leading '/' from the path
        if path == "":
            path = "/"  # Set the path to "/" for the home route
        if path in self.BUILT_ROUTES:
            response = self.BUILT_ROUTES[path]
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.wfile.write(b"<h1>404 Not Found</h1>")


class WApp:
    INITAL_ROUTE = "/"
    def __init__(self):
        self.port = 3000
        self.host = 'localhost'
        self.devServer = False
        self.static_url_path = "static"
        self.name = "Zenith App"
        self.logging = True
        self.webServer = HTTPServer((self.host, self.port), CustomServer)

    @staticmethod
    def register_route(route, response):
        CustomServer.BUILT_ROUTES[route] = response

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


