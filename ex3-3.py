#POST 방식 요청
from urllib.parse import urlencode
from urllib.request import Request, urlopen

data = urlencode({'name':'둘리','email':10,'pwd':20})
data = data.encode('UTF-8')
#print(data)
request = Request('http://www.example.com',data)
request.add_header('Content-Type','text/html')

f=urlopen(request)
response = f.read()

print(response)