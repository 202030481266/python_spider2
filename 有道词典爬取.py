import requests
import time
from hashlib import md5
from random import randint

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
     'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '241',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'X-Requested-With': 'XMLHttpRequest'
}
word = input('请输入要翻译的单词：')
lts = str(int(time.time()*1000))
salt = lts + str(randint(0,9))
str_ = "fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
md = md5()
md.update(str_.encode())
sign = md.hexdigest()
data = {
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'lts': lts,
    'bv': 'a68be4fa7a0372e7ae83662b495a6f4c',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}

html = requests.post(url=url, data=data, headers=headers).json()
print(html)