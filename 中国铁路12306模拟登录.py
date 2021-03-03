from selenium import webdriver
from time import sleep
from PIL import Image
from chaojiying import Chaojiying_Client
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains

#反检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

bro = webdriver.Chrome(executable_path='./chromedriver.exe',options=option)
sleep(1)

bro.get('https://kyfw.12306.cn/otn/resources/login.html')
#使用最大窗口界面
bro.maximize_window()
#使用账号进行登录
area = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]')
area.click()
sleep(2)
#对整张页面进行截图
bro.save_screenshot('./all.png')
#找到验证码所在的区域
code_img_ele = bro.find_element_by_id('J-loginImg')
#得到了验证码区域的左上角的店点的坐标
location = code_img_ele.location
#计算图片的宽和高
size = code_img_ele.size
#得到一个矩形区域的元组,记得数据要乘以1.25适应大小
rangle = (int(location['x'])*1.25,
          int(location['y'])*1.25,
          int(location['x']+size['width'])*1.25,
          int(location['y']+size['height'])*1.25
          )
#创建一个图片对象
i = Image.open('./all.png')
#使用crop（）来进行截图
frame = i.crop(rangle)
frame.save('./code.png')
#使用超级鹰来进行验证
chaojiying = Chaojiying_Client('liushulin', '789456123lsl', '912902')
im = open('./code.png', 'rb').read()
print(chaojiying.PostPic(im, 9004)['pic_str'])
result = chaojiying.PostPic(im, 9004)['pic_str']
#解析超级鹰返回得到的结果
all_list = []
if '|' in result:
    str = result.split('|')
    for i in range(len(str)):
        detail_list = str[i].split(',')
        x = int(detail_list[0])
        y = int(detail_list[1])
        xy_list = []
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    xy_list = []
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(all_list)

#输入用户名和密码
username = bro.find_element_by_id('J-userName')
password = bro.find_element_by_id('J-password')
btn = bro.find_element_by_id('J-login')
username.send_keys('liushulin')
sleep(0.2)
password.send_keys('789456123lsl')
sleep(0.2)

#创建动作链对象
action = ActionChains(bro)
#执行点击相对应的验证码的图片
for li in all_list:
    x = li[0]
    y = li[1]
    #点击并且开始执行动作链，这里以验证码的图片进行参照，使用move_to_element_with_offset()
    action.move_to_element_with_offset(code_img_ele,int(x/1.25),int(y/1.25)).click().perform()
    sleep(0.5)

#点击登录按钮
btn.click()
sleep(2)
#寻找滑块

swiper = bro.find_element_by_xpath('//*[@id="nc_1_n1z"]')
#按住滑块不动
action.click_and_hold(swiper).perform()
#进行滑动
action.move_by_offset(300 , 0)
action.release().perform()

sleep(10)
bro.quit()
#这成功的概率完全取决于超级鹰的识别！！！




