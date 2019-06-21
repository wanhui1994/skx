#coding=utf-8

from common.com import Comm
import os,time

class Choujiang(Comm):
     pattern_loc=('xpath',".//*[@id='drawModeType']")
     zjgl_loc=('xpath',".//*[@id='chanceRate']")
     addxuanxiang_loc=('xpath',".//*[@id='addPrizeButton']")
     hbtitle_loc=('xpath',".//*[@id='outlayName']")
     hbname_loc=('xpath',".//*[@id='companyName']")
     hbzf_loc=('xpath',".//*[@id='blessing']")

     def pattern(self,text):
        #抽奖设置--抽奖模式(设置不抽奖)
        self.downmenutext(self.pattern_loc,text)

     def gl(self,text):
        #抽奖设置--抽奖概率
        self.send(self.zjgl_loc,text)

     def addxuanxiang(self):
         #抽奖设置--增加选项
         self.click(self.addxuanxiang_loc)

     def hongbao(self,text,text1,text2):
         #抽奖设置--微信红包需要增加的标签数据
         self.send(self.hbtitle_loc,text)
         self.send(self.hbname_loc,text1)
         self.send(self.hbzf_loc,text2)


     def jiangxiang1(self,loc1,loc2,loc3,text,text1):
        #抽奖设置--奖项设置[实物奖品]
        self.send(loc1,text)  #名称
        self.send(loc2,text1) #数量
        self.uploadfile(loc3,"C:\\testfile\\tp.exe")

     def jiangxiang2(self,loc1,loc2,loc3,loc4,text1,text2,text3):
        #抽奖设置--奖项设置[红包]
        self.send(loc1,text1)  #类型
        self.send(loc2,text2)  #名称
        self.send(loc3,text3)  #数量
        self.uploadfile(loc4,"C:\\testfile\\tp.exe")








