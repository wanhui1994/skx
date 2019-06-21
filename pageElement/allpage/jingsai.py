#coding=utf-8

from common.com import Comm
from pageElement.compage.choujiangpage import Choujiang
import os,time


class Jsadd(Choujiang,Comm):
    tikuchoice_loc=("xpath",".//*[@id='exam_add']/div[2]/div[1]/div/div/a[1]")
    jsxuanzetiku_loc=("xpath",".//*[@id='competition_add']/div[2]/div[1]/div/div/a[1]")
    jstikuimport_loc=("xpath",".//*[@id='competition_add']/div[2]/div[1]/div/div/a[2]")
    jsxiayibu_loc=("xpath",".//*[@id='competition_add']/div[9]/div/button[3]")
    jssumscore_loc=("xpath",".//*[@id='paperTotalScore']")
    jsxztk_loc=("xpath",".//*[@id='paper_role_add']")
    jsexertype_loc=("id","innerType0")
    jsregUser_loc=("id","regUserInfoType")
    jsstartime_loc=("id","startTime")
    jsendtime_loc=("id","endTime")
    jstotal_loc=("xpath",".//*[@id='anserTime']")
    jsfrequency_loc=("xpath",".//*[@id='participateCount']")
    jstitle_loc=("xpath",".//*[@id='activityName']")
    jsplain_loc=('xpath',".//*[@id='activityShowContent']")
    jszhutitpweb_loc = ('xpath',".//*[@id='pcImgPath']")
    jszhutitpapp_loc = ('xpath',".//*[@id='appImgPath']")
    jssavebutton_loc=('xpath',".//*[@id='saveButton']")
    jsfabu_loc=("xpath",".//*[@id='competitionList']/tbody/tr[1]/td[6]/a[2]/i")
    jstianjia_loc=("xpath","/html/body/div[1]/div[2]/span/a")
    jsshenhe_loc=("xpath",".//*[@id='competitionList']/tbody/tr[1]/td[6]/a[3]/i")
    jsshare_loc=("xpath",".//*[@id='shareCount']")
    jsconcur_loc=("xpath",".//*[@id='concurrentRsCeilingPrompt']")


    def jstianjia(self):
        #点击添加按钮
        self.click(self.jstianjia_loc)

    def jstikuchoice(self):
        #题库--点击题库选择选择题库
        self.click(self.jsxuanzetiku_loc)  #选择题库
        time.sleep(1)
        iframe =self.driver.find_element_by_id("layui-layer-iframe1")
        self.driver.switch_to_frame(iframe)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='questionBankList']/tbody/tr[1]/td[1]/input").click()
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a[1]").click()
        time.sleep(3)
        js = "window.scrollTo(0,1000);"
        self.driver.execute_script(js)


    def jstikuimport(self,path):
        #题库--点击题库导入按钮进行题库导入
        self.click(self.jstikuimport_loc)
        os.system(path) #选择导入的excel文件

    def jsxiayibu(self):
        #下一步按钮
        self.click(self.jsxiayibu_loc)

    def jssumscore(self,num):
        #试卷设置--总分
        self.send(self.jssumscore_loc,num)

    def jsxuanzetiku(self):
        #试卷设置--点击添加题库按钮
        self.click(self.jsxztk_loc)

    def jsexercisetype(self,loc,text):
        #试卷--习题类型选项
        self.downmenutext(loc,text)

    def jsexercisesnumber(self,loc,text):
        #试卷--习题数量
        self.send(loc,text)

    def jsexercisescore(self,loc,text):
        #试卷--习题分数
        self.send(loc,text)

    def jsstarttime(self,text):
        #考试设置--开始时间
        self.datetime("startTime",self.jsstartime_loc,text)

    def jsendtime(self,text):
        #考试设置--结束时间
        self.datetime("endTime",self.jsendtime_loc,text)

    def jstotalduration(self,text):
        #考试设置--答题总时长
        self.send(self.jstotal_loc,text)

    def jsregUser(self,text):
        #参与人员设置--是否登记信息
        self.downmenutext(self.jsregUser_loc,text)


    def jsfrequency(self,text):
        #参与人员设置--参与次数
        self.send(self.jsfrequency_loc,text)

    def jsshare(self,text):
        #参与人员设置--分享次数
        self.send(self.jsshare_loc,text)

    def jsconcur(self,text):
        #参与人员设置--并发上限
        self.send(self.jsconcur_loc,text)

    def jstitle(self,text):
        #首页设置--竞赛标题
        self.send(self.jstitle_loc,text)


    def jsexamexplain(self,text):
        #首页设置--竞赛说明
        self.send(self.jsplain_loc,text)

    def jswebtheme(self,path):
        #首页设置--网页主题图片
         self.click(self.jszhutitpweb_loc)
         os.system(path) #选择导入的excel文件

    def jsapptheme(self,path):
        #首页设置--app主题图片
         self.click(self.jszhutitpapp_loc)
         os.system(path) #选择导入的excel文件

    def jssavebutton(self):
        #外观设置--保存按钮
        self.click(self.jssavebutton_loc)

    def jsfabu(self):
         #列表--发布(点击确定按钮)
        self.click(self.jsfabu_loc)
        self.click(("xpath",".//*[@id='layui-layer1']/div[3]/a[1]"))


    def jsshenhe(self):
        #列表--审核(审核通过)
        self.click(self.jsshenhe_loc) #点击审核按钮
        self.driver.switch_to.parent_frame()
        iframe1 = self.driver.find_elements_by_tag_name('iframe')[0]
        self.driver.switch_to_frame(iframe1)
        iframe =self.driver.find_element_by_id("layui-layer-iframe2")
        self.driver.switch_to_frame(iframe)
        self.driver.find_element_by_xpath(".//*[@id='competitionDetail']/div[5]/button[1]").click()


    def jsaddexam(self,num,ts1,ts2,ts3,fs1,fs2,fs3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4,text5):
        '''除了题库设置外的其他页面元素操作汇总'''
        self.jssumscore(num)  #设置答题总分
        time.sleep(2)
        self.jsxuanzetiku()
        self.jsxuanzetiku()   #试卷设置--点击添加题库
        self.jsexercisetype(('xpath',".//*[@id='innerType0']"),'单选题')
        self.jsexercisetype(('xpath',".//*[@id='innerType1']"),'多选题')
        self.jsexercisetype(('xpath',".//*[@id='innerType2']"),'判断题')
        self.jsexercisesnumber(('xpath',".//*[@id='innerNumber0']"),ts1)
        self.jsexercisesnumber(('xpath',".//*[@id='innerNumber1']"),ts2)
        self.jsexercisesnumber(('xpath',".//*[@id='innerNumber2']"),ts3)
        self.jsexercisescore(('xpath',".//*[@id='innerScore0']"),fs1)
        self.jsexercisescore(('xpath',".//*[@id='innerScore1']"),fs2)
        self.jsexercisescore(('xpath',".//*[@id='innerScore2']"),fs3)
        self.jsxiayibu()
        time.sleep(2)
        self.jsstarttime(startimes) #考试设置--开始时间
        self.jsendtime(endtimes)    #考试设置--结束时间
        self.jstotalduration(totalnum) #答题总时间（单位分）
        self.jsxiayibu()
        time.sleep(2)
        self.jsregUser('不登记')
        self.jsfrequency(text1) #参与次数
        self.jsshare(text2) #分享次数
        self.send(('xpath',".//*[@id='concurrentRsCeilingPrompt']"),text3) #并发人数上限
        self.jsxiayibu()
        self.pattern('不抽奖')  #抽奖不抽奖
        self.jsxiayibu()
        self.jstitle(text4)  #竞赛标题
        self.jsexamexplain(text5)  #竞赛说明
        self.jswebtheme('C:\\testfile\\tp.exe')
        self.jsapptheme('C:\\testfile\\tp.exe')
        time.sleep(5)
        self.jsxiayibu()
        self.jssavebutton()
        time.sleep(5)
        self.jsfabu()
        time.sleep(5)
        self.jsshenhe()

    def jsimporexame(self,num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4,text5):
        '''导入题库，不抽奖'''
        time.sleep(3)
        self.jstianjia()
        time.sleep(5)
        self.jstikuimport('C:\\testfile\\excel.exe') #添加导入的文件路径
        time.sleep(10)
        self.jsxiayibu() #点击下一步按钮
        self.jsaddexam(num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4,text5)


    def jschoiceexame(self,num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4,text5):
        '''选择题库执行这个操作，必须有一个已经存在的题库，不抽奖'''
        time.sleep(3)
        self.jstianjia()
        time.sleep(5)
        self.jstikuchoice()
        self.jsxiayibu() #点击下一步按钮
        self.jsaddexam(num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4,text5)