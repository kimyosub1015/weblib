from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

port = 7777;


# 핸들러 안에 특정 요청이 들어올 경우를 처리함을 정의
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def get_params(self, name):
        qs = self.path[self.path.find('?') + 1:]
        params = parse_qs(qs)
        values = params.get(name)
        return '' if values is None else values.pop()
        # 파라미터는 데이터 값을 스트링으로 처리한다.(어떤 형태의 데이터던 간에)
        # return을 할 경우 String하고 None 타입을 더해서 출력할 순 없다.
        # 그러니 None 대신 공백 스트링을 나타내서 처리한다.
        # 파이썬의 삼항연산 수행, 원래는 아래의 주석이다.
        # 파이썬은 null 대신 None을 쓴다.

    '''
        if values is None:
            return None
        else:
            return values.pop()
    '''

    def ex1(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html : charset=UTF-8')
        self.end_headers()
        self.wfile.write('<h1>안녕하세요</h1>'.encode('UTF-8'))

    def ex2(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html : charset=UTF-8')
        self.end_headers()
        self.wfile.write('<h1>안녕하세요?</h1>'.encode('UTF-8'))

    def do_GET(self):
        index = self.path.find('?')
        req_url = self.path if index == -1 else self.path[:index]
        # 슬라이싱으로 특정 키워드를 잘라낸다.
        # INDEX는 찾는 문자가 없는건 에러를 내고, FIND는 -1을 출력한다.
        # 그러니 여기선 FIND를 쓴다.
        # url mapping
        if req_url == '/iot':
            handler_name = 'ex' + self.get_params('ex')
            # print(handler_name)
            # 요청을 처리해주는 함수인 핸들러에다 ex를 붙인 값이 들어오면 콘솔창에 출력해준다.
            if handler_name not in MyHTTPRequestHandler.__dict__:
                self.send_error(404, 'File is Not Found')
                return
            MyHTTPRequestHandler.__dict__[handler_name](self)

        elif req_url == '/board':
            pass

        else:
            self.send_error(404, 'File is not Found')


httpd = HTTPServer(('', port), MyHTTPRequestHandler)
print('Server running on port', port)
httpd.serve_forever()
