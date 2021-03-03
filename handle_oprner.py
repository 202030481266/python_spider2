from urllib.request import HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, build_opener, ProxyHandler
from urllib.error import URLError

username = 'xxxxxxx'
password = '123456'
url = 'www.xxx.com'
proxy_handler = ProxyHandler{
    'http':'ip:port',
    'https':'ip:port'
}
#创建一个对象管理用户名和密码
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(url=url, user=username, passwd=password)
#创建一个认证管理的handler对象
auth_handler = HTTPBasicAuthHandler(p)
#创建一个opener对象
opener = build_opener(auth_handler,proxy_handler)

try:
    response = opener.open(url)
    html = response.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
