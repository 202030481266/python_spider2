from selenium import webdriver
from time import sleep
#导入动作链
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#如果定位的标签是存在于iframe标签之中的则必须通过如下操作在进行标签定位
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')

#使用动作链
action = ActionChains(bro)
action.click_and_hold(div)
#一点一点的移动
for i in range(5):
    #move_by_offset是移动的含义，有两个参数x，y，其中x表示左右移动的数据，y表示上下移动的数据
    #perform（）表示执行的方法
    action.move_by_offset(17,0).perform()
    sleep(0.2)
#释放动作链
action.release()
bro.quit()