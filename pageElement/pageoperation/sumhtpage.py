#coding=utf-8

from pageElement.compage.loginpage import Login
from pageElement.compage.lableselection import Lable
from pageElement.allpage.exam_add import Tikuadd
from pageElement.allpage.vote_add import Voteadd
from pageElement.allpage.jingsai import Jsadd
# from common.com import Comm
from selenium.webdriver.support.ui import WebDriverWait
import time

class Sumpage(Lable,Tikuadd,Voteadd,Jsadd,Login):
    # 页面操作汇总

   def htuserlogin(self,name,pas):
       '''后台用户登录'''
       self.openurl("http://bms.t.saikao100.com")
       try:
            WebDriverWait(self.driver,5,5).until(lambda x: x.find_element_by_xpath(u"html/body/div[1]/div[1]/span"))
            self.htlogin(name,pas)  #后台账号登录
       except Exception as msg:
            print("元素未找到")


   def htdrks(self,name,pas,num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4):
        '''后台考试---导入题库'''
        self.htuserlogin(name,pas)
        time.sleep(5)
        self.activity_exam()
        self.imporexame(num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4)

   def htxzks(self,name,pas,num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4):
        '''后台考试---选择题库'''
        self.htuserlogin(name,pas)
        time.sleep(5)
        self.activity_exam()
        self.choiceexame(num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4)

   def htdrjs(self,name,pas,num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4,text5):
        '''后台竞赛---导入题库【不抽奖】'''
        self.htuserlogin(name,pas)
        time.sleep(5)
        self.activity_competition()
        self.jsimporexame(num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4,text5)

   def htxzjs(self,name,pas,num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4,text5):
        '''后台竞赛---选择题库【不抽奖】'''
        self.htuserlogin(name,pas)
        time.sleep(5)
        self.activity_competition()
        self.jschoiceexame(num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4,text5)

   def htnodrawvote(self,name,pas,name1,sm,sttime,entime,text,tpname,tpsm):
       '''后台投票--不登记\不抽奖'''
       self.htuserlogin(name,pas)
       time.sleep(5)
       self.activity_vote()
       self.noDraw(name1,sm,sttime,entime,text,tpname,tpsm)

   def htdjcjvote(self,name,pas,name1,sm,sttime,entime,text,hdname,djxxtext,patternname,gltext,text1,text2,tpname,tpsm):
       '''后台投票--登记（登记信息全勾选）、抽奖(奖项：奖品[1个奖项])'''
       self.htuserlogin(name,pas)
       time.sleep(5)
       self.activity_vote()
       self.djcj(name1,sm,sttime,entime,text,hdname,djxxtext,patternname,gltext,text1,text2,tpname,tpsm)

   def htdjcj1vote(self,name,pas,name1,sm,sttime,entime,text,hdname,patternname,djxxtext,hbtext,hbtext1,hbtext2,gltext,jx,jxnum,jx1,jxnum1,jx2,jxnum2,jx3,jxnum3,tpname,tpsm):
       '''后台投票--登记（登记信息全勾选）、抽奖(奖项：1个红包3个奖品[4个奖项])'''
       self.htuserlogin(name,pas)
       time.sleep(5)
       self.activity_vote()
       self.djcj1(name1,sm,sttime,entime,text,hdname,patternname,djxxtext,hbtext,hbtext1,hbtext2,gltext,jx,jxnum,jx1,jxnum1,jx2,jxnum2,jx3,jxnum3,tpname,tpsm)

