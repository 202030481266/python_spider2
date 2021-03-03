import requests
from requests.auth import HTTPBasicAuth
# 第一种方式可以使用HTTPBasic类来进行身份认证
response = requests.get('http://www.taobao.com/', auth=HTTPBasicAuth('username', 'password'))
# 第二种方式可以直接在
new_response = requests.get('http://www.taobao.com/', auth=('username', 'password'))