"""
如何增强内心的力量
"""
import urllib.request
from urllib import request

response = urllib.request.urlopen("http://www.baidu.com/")
print(response)
html = response.read().decode('utf-8')
print(html)

bytes = response.read()
string = response.read().decode()

url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'
}

req = request.Request(url, headers)

res = request.urlopen(req)

html = res.read()

