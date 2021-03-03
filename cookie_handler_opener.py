from urllib.request import HTTPCookieProcessor, build_opener
from urllib.error import URLError
import http.cookiejar

#先创建一个Cookiejar对象，然后使用HTTPCookieProcessor()创建一个handler对象
cookie = http.cookiejar.CookieJar()
handler = HTTPCookieProcessor(cookie)
#获取cookie
opener = build_opener(handler)
opener.open('https://www.baidu.com/')
for item in cookie:
    print(item.name + "=" + item.value)
