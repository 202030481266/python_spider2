from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
tag = bro.find_element_by_id('switcher_plogin')
tag.click()

username = bro.find_element_by_id('u')
password = bro.find_element_by_id('p')
btn = bro.find_element_by_id('login_button')

username.send_keys('1258493030')
sleep(1)
password.send_keys('789456123lsl')
sleep(1)
btn.click()

sleep(3)
bro.quit()
