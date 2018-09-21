# HttpConnetcion
from http.client import HTTPConnection

# 1 - 연결
connection = HTTPConnection('www.example.com')

# 2 - 요청 / GET방식으로 하겠다
connection.request('GET', '/')

# 3 - 응답받기
response = connection.getresponse()

# 4 - Body 읽어오기
body = response.read()
#print(body)

# 404 에러 받아보기

connection.request('GET','/')
response = connection.getresponse()
print(response.status,response.reason)