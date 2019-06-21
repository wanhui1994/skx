#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from pyvirtualdisplay import Display
from selenium.webdriver.support.select import Select
import os


class Comm():
    def __init__(self,browser='ff'):
        try:
            if browser == 'ff' or browser == 'Firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'ch' or browser == 'Chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'ie'  or browser == 'IE':
                self.driver = webdriver.Ie()
        except ValueError:
            print('Please enter the correct browser name!(Supported browsers are: Firefox、Chrome and Ie)')

   # url打开
    def openurl(self,url):
        self.driver.get(url)
        self.driver.maximize_window() #最大化浏览器

   # 定义元素获取
    def element(self,locator):
        # element = WebDriverWait(self.driver, 30, 1).until(lambda x: x.find_element(*locator)) #方案1
        try:
            element=self.driver.find_element(*locator) # *号是把两个参数分开传值  方案2
            return element
        except NoSuchElementException as msg:
            print('元素查找异常：%s'%msg)

    # 点击功能
    def click(self,locator):
       element = self.element(locator)
       element.click()

    # 清空功能
    def clear(self,locator):
        element = self.element(locator)
        element.clear()

   # 输入信息
    def send(self,locator,txt):
        element = self.element(locator)
        #element.clear()
        element.send_keys(txt)

    #下拉菜单元素获取-value
    def downmenuvalue (self,locator,num):
        Select(self.element(locator)).select_by_value(num)

    #下拉菜单元素获取-option(text文本)
    def downmenutext (self,locator,text):
        Select(self.element(locator)).select_by_visible_text(text)

    #日期控件
    def datetime(self,date,locator,text):
        # 去掉元素的readonly属性,date就是日期控件的id
        js='document.getElementById("'+date+'").removeAttribute("readonly");'
        self.driver.execute_script(js)
        self.clear(locator)
        self.send(locator,text) #输入日期

    #上传文件（通过控件上传）
    def uploadfile(self,loc,path):
        self.click(loc)
        os.system(path) #选择导入的excel文件

    # 获取元素上的文字
    def text(self,locator):
        element = self.element(locator).text
        return element

   # 显示等待元素出现
    def WebDriver(self,timeout,method):
        try:
          WebDriverWait(self.driver,timeout,5).until(method)
          print('查找到元素了')
        except Exception as msg:
            print("元素未找到")


    # 隐示等待出现
    def implicitly(self,value):
        self.driver.implicitly_wait(value)


    #截图
    def screenshot1(self,path):
         self.driver.get_screenshot_as_file(path)

    # 停止页面加载,并且刷新页面
    def page_timeout(self,num):
        self.driver.set_page_load_timeout(num)



    # 关闭当前页面
    def clos(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    #浏览器后台运行--静默模式
    def silent (self):
         display = Display(visible=0, size=(800, 600))
         display.start()



    #-----------------判断-------------------
    #title判断
    def title(self,name):
        title = EC.title_is(name)  #判断title完全等于

    def title_contains(self,name):
        title_contains = EC.title_contains(name)  #判断title包含
