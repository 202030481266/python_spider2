from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
#实现无可视化的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#反检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

bro = webdriver.Chrome(executable_path='../selenium/chromedriver.exe',chrome_options=chrome_options,options=option)

bro.get('https://price.pcauto.com.cn/price/nb2/')
page_text = bro.page_source
tree = etree.HTML(page_text)
div_list = tree.xpath('//*[@id="JlistTb"]/div/div[1]')
fp = open('./car_price.txt', 'w', encoding='utf-8')
for div in div_list:
    name = div.xpath('./p[2]/a/text()')[0]
    price = div.xpath('./p[3]/span/text()')[0]
    note = name + ':' + price + '\n'
    fp.write(note)
fp.close()


