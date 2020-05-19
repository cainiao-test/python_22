import base64
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import sleep
import xlrd

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# 打开链接
driver.get(
    "https://www.etax-gd.gov.cn/xxmh/html/index_origin.html?gopage=true&m1=gzcx&m2=&fromWhere=&qxkzsx=0&tabTitle=null"
    "&cdId=dlqcd-1&gnDm=gndm-dlqcd-1#none")

driver.find_element_by_xpath("//a[@mflag='swdjxxcx']").click()
# 切换iframe
driver.switch_to.frame('ifrMain')

file_path = 'C:/Users/Administrator/Desktop/天河黄埔催缴名单分配已查.xlsx'
# 获取文件数据
data = xlrd.open_workbook(file_path)
# 获取sheet
sheet_data = data.sheet_by_name('托收名单')
# 读取第1行数据
rows1 = sheet_data.row_values(0)
# 读取第4列数据
cols1 = sheet_data.col_values(3)


i = 0
driver.find_element_by_xpath("//input[@id='nsrsbh']").send_keys(cols1[i])


# 右键单击图片
img_id = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.ID, 'yzmImg')))
img = driver.find_element_by_id('yzmImg')

# 执行鼠标动作
actions = ActionChains(driver)
# 找到图片后右键单击图片
actions.context_click(img)
actions.perform()
# 发送键盘按键，根据不同的网页，
# 右键之后按对应次数向下键，
# 找到图片另存为菜单
pyautogui.typewrite(['down', 'down', 'enter'])
# 单击图片另存之后等1s敲回车
sleep(1)
pyautogui.typewrite(['enter'])
sleep(3)

# 验证码转base64
with open("C:/Users/Administrator/Downloads/builderCaptcha.png", 'rb') as f:
    base64_data = base64.b64encode(f.read())
    yzm_base64 = base64_data.decode()
    print('%s' % yzm_base64)

# 百度AI识别验证码
url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token=24.f208f5919bff6e583774c1f7076cbd89.2592000" \
      ".1592454379.282335-19948213 "
payload = {"image": yzm_base64}
headers = {"Content-Type": "application/x-www-form-urlencoded"}
response = requests.request("POST", url, data=payload, headers=headers)
code = response.json()['words']
print(code)

# 删除验证码
os.remove("E:/yzm/builderCaptcha.png")

driver.find_element_by_xpath("//input[@type='button']").click()
