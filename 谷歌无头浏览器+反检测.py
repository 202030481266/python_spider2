from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
#实现无可视化的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#反检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

bro = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options,options=option)
#无可视化界面（无头部浏览器）
bro.get('https://www.baidu.com/')
print(bro.page_source)

sleep(2)
bro.quit()