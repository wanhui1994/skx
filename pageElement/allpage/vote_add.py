#coding=utf-8

from common.com import Comm
from pageElement.compage.choujiangpage import Choujiang
import os,time

class Voteadd(Choujiang,Comm):

    addplayer_loc=('xpath',".//*[@id='addOptionBtn']/div/input")
    playername_loc=('xpath',".//*[@id='activity_add']/div/div[2]/div/input")
    playerdes_loc=('xpath',".//*[@id='activity_add']/div/div[3]/div/textarea")
    playerthem_loc=('xpath',".//*[@id='activity_add']/div/div[4]/div/a[1]")
    saveannv_loc=('css_selector',".layui-layer-btn0")
    xiayibu1_loc=('xpath',".//*[@id='nextButton']")
    startime_loc=('xpath',".//*[@id='startTime']")
    endtime_loc=('xpath',".//*[@id='endTime']")
    shareCount_loc=('xpath',".//*[@id='shareCount']")
    pattern_loc=('xpath',".//*[@id='drawModeType']")
    tptitle_loc=('xpath',".//*[@id='activityName']")
    tpplain_loc=('xpath',".//*[@id='activityShowContent']")
    savebutton_loc=('xpath',".//*[@id='saveButton']")
    djtype_loc=('xpath',".//*[@id='regUserInfoType']")
    djxx1_loc=('xpath',".//*[@id='regUserInfoPrompt']")
    tianjia_loc=('xpath',"/html/body/div[1]/div[2]/span/a")

    def tianjia(self):
        self.click(self.tianjia_loc)

    def addplayer(self):
        #选手设置--添加选手按钮
        self.click(self.addplayer_loc)

    def playername(self,text):
        #选手设置--选手名称
        self.send(self.playername_loc,text)

    def playerdes(self,text):
        #选手设置--选手说明
        self.send(self.playerdes_loc,text)

    def playertheme(self,path):
        #选手设置--选手图片
        self.click(self.playerthem_loc)
        os.system(path) #选择导入的图片文件

    def saveannv(self):
        self.click(self.saveannv_loc)

    def xiayibu1(self):
        self.click(self.xiayibu1_loc)


    def starttime(self,text):
        #规则设置--开始时间
        self.datetime("startTime",self.startime_loc,text)

    def endtime(self,text):
        #规则设置--结束时间
        self.datetime("endTime",self.endtime_loc,text)

    def sharecount(self,text):
        #规则设置--分享次数
        self.send(self.shareCount_loc,text)

    def rysettings(self,text):
        #参与人员设置--是否登记信息
        self.downmenutext(self.djtype_loc,text)

    def djzd(self,loc):
        #参与人员设置--登记字段勾选
        self.click(loc)

    def djxx(self,text):
        #参与人员设置--信息登记提示
        self.send(self.djxx1_loc,text)

    def pattern(self,text):
        #抽奖设置--抽奖模式(设置不抽奖)
        self.downmenutext(self.pattern_loc,text)

    def tptitle(self,text):
        #首页设置--投票名称
        self.send(self.tptitle_loc,text)

    def tpplain(self,text):
        #首页设置--投票说明
        self.send(self.tpplain_loc,text)

    def savebutton(self):
        #外观设置--保存按钮
        self.click(self.savebutton_loc)

    def addtp(self,name,sm,sttime,entime,text):
        '''选手和规则设置页面汇总'''
        time.sleep(3)
        self.tianjia()
        time.sleep(5)
        self.addplayer()
        time.sleep(3)
        iframe =self.driver.find_element_by_id("layui-layer-iframe1")
        self.driver.switch_to_frame(iframe)
        self.playername(name)
        self.playerdes(sm)
        self.playertheme('C:\\testfile\\tp.exe')
        js = "window.scrollTo(0,1000);"
        self.driver.execute_script(js)
        time.sleep(2)
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_partial_link_text("保存").click()
        time.sleep(1)
        self.xiayibu1()
        self.starttime(sttime)
        self.endtime(entime)
        self.sharecount(text)
        self.xiayibu1()

    def cjindex(self,hdname,djxxtext):
        #登记（登记信息全勾选）
        self.rysettings(hdname)
        self.djzd(('xpath',".//*[@id='regUserInfoPromptDiv']/div/label[1]/input"))
        self.djzd(('xpath',".//*[@id='regUserInfoPromptDiv']/div/label[2]/input"))
        self.djzd(('xpath',".//*[@id='regUserInfoPromptDiv']/div/label[3]/input"))
        self.djzd(('xpath',".//*[@id='regUserInfoPromptDiv']/div/label[4]/input"))
        self.djzd(('xpath',".//*[@id='regUserInfoPromptDiv']/div/label[5]/input"))
        self.djzd(('xpath',".//*[@id='regUserInfoPromptDiv']/div/label[6]/input"))
        self.djxx(djxxtext)


    def noDraw(self,name,sm,sttime,entime,text,tpname,tpsm):
        #不登记\不抽奖
        self.addtp(name,sm,sttime,entime,text)
        self.rysettings('不登记')
        self.xiayibu1()
        self.pattern('不抽奖')
        self.xiayibu1()
        self.tptitle(tpname)
        self.tpplain(tpsm)
        self.xiayibu1()
        self.savebutton()


    def djcj(self,name,sm,sttime,entime,text,hdname,djxxtext,patternname,gltext,text1,text2,tpname,tpsm):
        #登记（登记信息全勾选）、抽奖(奖项：奖品[1个奖项])
        self.addtp(name,sm,sttime,entime,text)
        self.cjindex(hdname,djxxtext)
        self.pattern(patternname)
        self.gl(gltext)
        self.jiangxiang1(('xpath',".//*[@id='prizeName0']"),('xpath',".//*[@id='prizeCount0']"),('xpaht',".//*[@id='prizeCount0']"),text1,text2)
        self.xiayibu1()
        self.tptitle(tpname)
        self.tpplain(tpsm)
        self.xiayibu1()
        self.savebutton()


    def djcj1(self,name,sm,sttime,entime,text,hdname,patternname,djxxtext,hbtext,hbtext1,hbtext2,gltext,jx,jxnum,jx1,jxnum1,jx2,jxnum2,jx3,jxnum3,tpname,tpsm):
        #登记（登记信息全勾选）、抽奖(奖项：1个红包3个奖品[4个奖项])
        self.addtp(name,sm,sttime,entime,text)
        self.cjindex(hdname,djxxtext)
        self.pattern(patternname)
        self.gl(gltext)
        self.downmenutext(('xpath',".//*[@id='prizeType0']"),'微信红包')
        self.hongbao(hbtext,hbtext1,hbtext2)
        self.jiangxiang2(('xpath',".//*[@id='outlayAmount0']"),('xpath',".//*[@id='prizeName0']"),('xpath',".//*[@id='prizeCount0']"),('xpaht',".//*[@id='prizeCount0']"),jx,jxnum)
        self.addxuanxiang()
        self.jiangxiang1(('xpath',".//*[@id='prizeName1']"),('xpath',".//*[@id='prizeCount1']"),('xpaht',".//*[@id='prizeCount1']"),jx1,jxnum1)
        self.addxuanxiang()
        self.jiangxiang1(('xpath',".//*[@id='prizeName2']"),('xpath',".//*[@id='prizeCount2']"),('xpaht',".//*[@id='prizeCount2']"),jx2,jxnum2)
        self.addxuanxiang()
        self.jiangxiang1(('xpath',".//*[@id='prizeName3']"),('xpath',".//*[@id='prizeCount3']"),('xpaht',".//*[@id='prizeCount3']"),jx3,jxnum3)
        self.xiayibu1()
        self.tptitle(tpname)
        self.tpplain(tpsm)
        self.xiayibu1()
        self.savebutton()


















