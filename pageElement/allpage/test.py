#coding=utf-8

from pageElement.allpage.exam_add import Tikuadd
from selenium.webdriver.support.ui import WebDriverWait
import time

class mm(Tikuadd):
    def c(self):
        self.openurl("http://bms.t.saikao100.com")
        try:
            WebDriverWait(self.driver,5,5).until(lambda x: x.find_element_by_xpath(u"html/body/div[1]/div[1]/span"))
            self.driver.find_element_by_xpath(".//*[@id='adminAccount']").send_keys('admin')
            self.driver.find_element_by_xpath(".//*[@id='adminPassword']").send_keys('abc123')
            self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[4]/div/input").click()
        except Exception as msg:
            print("元素未找到")
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='areTop']/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='areleft']/div[2]/dl[3]/dt/a").click()
        m=self.driver.find_element_by_xpath(".//*[@id='min_title_list']/li[2]/span").text
        print(m)
        time.sleep(5)
        iframe = self.driver.find_elements_by_tag_name('iframe')[1]
        self.driver.switch_to_frame(iframe)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/span/a").click()
        time.sleep(10)
        self.imporexame('100','1','1','1','30','30','40','2019-07-06 09:57:33','2019-07-07 09:57:33','1','60','1','1','testwh','testwh')
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='examList']/tbody/tr[1]/td[6]/a[2]/i").click()
        self.driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='examList']/tbody/tr[1]/td[6]/a[3]/i").click()
        iframe =self.driver.find_element_by_id("layui-layer-iframe1")
        self.driver.switch_to_frame(iframe)
        self.driver.find_element_by_xpath(".//*[@id='form-activityquestion-edit']/div[5]/div/button[1]").click()

k=mm()
k.c()


