# 打包exe文件需要安装库pyinstaller, 指令为：pip install pyinstaller
# 获取模拟状态需要库文件Appium-Python-Client,指令：pip install Appium-Python-Client

# 步骤1，填写夜神模拟器路径，并启动设备



from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {'platformName': "Android",
                'platformVersion': '5.1',
                'deviceName': '127.0.0.1:62001',
                'appPackage': 'com.igg.android.huntersandpuzzles',
                'appActivity': 'com.unity.androidplugin.UnityPlayerActivity'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)          # 建立 session
driver.implicitly_wait(9)


time.sleep(5)


# driver.find_element_by_id("************").click()         # 点击元素
#
# driver.find_element_by_xpath("************").click()      # 点击元素
#
# driver.find_element_by_xpath("************").send_keys(u'123456')   # 发送键值
#
# driver.quit()      # 退出 session


