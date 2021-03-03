from selenium import webdriver
from lxml import etree
from time import sleep
#创建一个浏览器对象
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
#向url发送请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
#获取页面源码数据，这时的数据包含有动态加载的数据
page_text = bro.page_source
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
sleep(5)
bro.quit()

