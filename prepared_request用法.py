from requests import Session, Request
from requests.packages import urllib3
# 关闭警告
urllib3.disable_warnings()
# 构造所需要的请求的一些参数
url = 'http://httpbin.org/post'
data = {
    'name': 'Liushulin'
}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
# 创建一个session对象
session = Session()
# 构造一个请求对象
request = Request(url=url, headers=headers, data=data, method='POST')
# 使用prepared_request的方法去构造一个prepared_request对象
prereq = session.prepare_request(request)
# 发送请求
response = session.send(prereq)

print(response.text)