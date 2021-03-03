from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get('https://www.jd.com/')
#标签定位搜索框
search_input = bro.find_element_by_xpath('//*[@id="key"]')
search_input.send_keys('macbook')
# 点击搜索按钮
btn = bro.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
btn.click()
sleep(5)
bro.quit()


