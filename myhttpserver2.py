from http.server import BaseHTTPRequestHandler, HTTPServer

port = 7777;
# 핸들러 안에 특정 요청이 들어올 경우를 처리함을 정의
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    pass

httpd = HTTPServer(('',port),MyHTTPRequestHandler)
print('Server running on port',port)
httpd.serve_forever()