from http.server import HTTPServer, BaseHTTPRequestHandler

class hellohandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.write.writer(self.path.encode())



def main():
    PORT = 8080
    server = HTTPServer(('',PORT), hellohandler)
    print('Server running on port %s' % PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()


if __name__ == '_main_':
    main()

 

