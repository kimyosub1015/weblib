from http.server import BaseHTTPRequestHandler, HTTPServer

port = 9999;
# 핸들러 안에 특정 요청이 들어올 경우를 처리함을 정의
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html : charset=UTF-8')
        self.end_headers()
        self.wfile.write('<h1>안녕하세요</h1>'.encode('UTF-8'))

httpd = HTTPServer(('',port),MyHTTPRequestHandler)
print('Server running on port',port)
httpd.serve_forever()