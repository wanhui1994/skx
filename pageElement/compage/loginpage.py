#coding=utf-8

from common.com import Comm
from selenium.webdriver.support.ui import WebDriverWait
import time


class Login(Comm):
    '''前后台登录元素汇总'''
    urlht="http://bms.t.saikao100.com"
    urlqt="http://www.t.saikao100.com/jswps/user/t/login.html"
    name_loc=("xpath",".//*[@id='adminAccount']")
    paw_loc=("xpath",".//*[@id='adminPassword']")
    tj_loc=("xpath",".//*[@id='loginForm']/div[4]/div/input")
    qtname_loc=('xpath',".//*[@id='userAccount']")
    qtpas_loc=('xpath',".//*[@id='userPassword']")
    qttj_loc=('xpath',".//*[@id='login_btn']")

    def name(self,text):
        self.send(self.name_loc,text)

    def pas(self,text):
        self.send(self.paw_loc,text)

    def tijiao(self):
        self.click(self.tj_loc)

    def qtname(self,text):
        self.send(self.qtname_loc,text)

    def qtpas(self,text):
        self.send(self.qtpas_loc,text)

    def qttj(self):
        self.click(self.qttj_loc)

    def htlogin(self,name,pas):
        #后台登录
        self.name(name)
        self.pas(pas)
        self.tijiao()

    def qtlogin(self,name,pas):
        #前台登录
        self.qtname(name)
        self.qtpas(pas)
        self.qttj()



