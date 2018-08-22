import urllib.request
from fake_useragent import UserAgent
ua = UserAgent()

url = "http://www.baidu.com"
headers = {"User-Agent":ua.random}
request = urllib.request.Request(url,headers=headers)
html = urllib.request.urlopen(request)
with open("baidu.txt","ab") as file:
    file.write(html.read())
print(html.read())
