#coding=utf-8

from common.com import Comm
import os,time


class Tikuadd(Comm):
    tikuchoice_loc=("xpath",".//*[@id='exam_add']/div[2]/div[1]/div/div/a[1]")
    xuanzetiku_loc=("xpath",".//*[@id='questionBankList']/tbody/tr[1]/td[1]/input")
    tikuimport_loc=("xpath",".//*[@id='exam_add']/div[2]/div[1]/div/div/a[2]")
    xiayibu_loc=("xpath",".//*[@id='exam_add']/div[8]/div/button[3]")
    sumscore_loc=("xpath",".//*[@id='paperTotalScore']")
    xztk_loc=("xpath",".//*[@id='paper_role_add']")
    exertype_loc=("id","innerType0")
    regUser_loc=("id","regUserInfoType")
    startime_loc=("id","startTime")
    endtime_loc=("id","endTime")
    total_loc=("xpath",".//*[@id='anserTime']")
    passingscore_loc=("xpath",".//*[@id='passThePoints']")
    frequency_loc=("xpath",".//*[@id='participateCount']")
    examtitle_loc=("xpath",".//*[@id='activityName']")
    examexplain_loc=('xpath',".//*[@id='activityShowContent']")
    zhutitpweb_loc = ('xpath',".//*[@id='pcImgPath']")
    zhutitpapp_loc = ('xpath',".//*[@id='appImgPath']")
    savebutton_loc=('xpath',".//*[@id='saveButton']")
    fabu_loc=("xpath",".//*[@id='examList']/tbody/tr[1]/td[6]/a[2]/i")
    tianjia_loc=("xpath","/html/body/div[1]/div[2]/span/a")
    shenhe_loc=("xpath",".//*[@id='examList']/tbody/tr[1]/td[6]/a[3]/i")


    def tianjia(self):
        #点击添加按钮
        self.click(self.tianjia_loc)

    def tikuchoice(self):
        #题库--点击题库选择选择题库
        self.click(self.xuanzetiku_loc)  #选择题库
        time.sleep(1)
        iframe =self.driver.find_element_by_id("layui-layer-iframe1")
        self.driver.switch_to_frame(iframe)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='questionBankList']/tbody/tr[1]/td[1]/input").click()
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a[1]").click()

    def tikuimport(self,path):
        #题库--点击题库导入按钮进行题库导入
        self.click(self.tikuimport_loc)
        os.system(path) #选择导入的excel文件

    def xiayibu(self):
        #下一步按钮
        self.click(self.xiayibu_loc)

    def sumscore(self,num):
        #试卷设置--总分
        self.send(self.sumscore_loc,num)

    def xuanzetiku(self):
        #试卷设置--点击添加题库按钮
        self.click(self.xztk_loc)

    def exercisetype(self,loc,text):
        #试卷--习题类型选项
        self.downmenutext(loc,text)

    def exercisesnumber(self,loc,text):
        #试卷--习题数量
        self.send(loc,text)

    def exercisescore(self,loc,text):
        #试卷--习题分数
        self.send(loc,text)

    def starttime(self,text):
        #考试设置--开始时间
        self.datetime("startTime",self.startime_loc,text)

    def endtime(self,text):
        #考试设置--结束时间
        self.datetime("endTime",self.endtime_loc,text)

    def totalduration(self,text):
        #考试设置--答题总时长
        self.send(self.total_loc,text)

    def passingscore(self,text):
        #考试设置--及格分数
        self.send(self.passingscore_loc,text)

    def regUser(self,text):
        #参与人员设置--是否登记信息
        self.downmenutext(self.regUser_loc,text)

    def frequency(self,text):
        #参与人员设置--参与次数
        self.send(self.frequency_loc,text)

    def examtitle(self,text):
        #首页设置--考试标题
        self.send(self.examtitle_loc,text)

    def examexplain(self,text):
        #首页设置--考试说明
        self.send(self.examexplain_loc,text)

    def webtheme(self,path):
        #首页设置--网页主题图片
         self.click(self.zhutitpweb_loc)
         os.system(path) #选择导入的excel文件

    def apptheme(self,path):
        #首页设置--app主题图片
         self.click(self.zhutitpapp_loc)
         os.system(path) #选择导入的excel文件

    def savebutton(self):
        #外观设置--保存按钮
        self.click(self.savebutton_loc)

    def fabu(self):
         #列表--发布(点击确定按钮)
        self.click(self.fabu_loc)
        self.click(("xpath",".//*[@id='layui-layer1']/div[3]/a[1]"))

    def shenhe(self):
        #列表--审核(审核通过)
        self.click(self.shenhe_loc) #点击审核按钮
        iframe =self.driver.find_element_by_id("layui-layer-iframe1")
        self.driver.switch_to_frame(iframe)
        self.driver.find_element_by_xpath(".//*[@id='form-activityquestion-edit']/div[5]/div/button[1]").click()





    def addexam(self,num,ts1,ts2,ts3,fs1,fs2,fs3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4):
        '''除了题库设置外的其他页面元素操作汇总'''
        self.sumscore(num)  #设置答题总分
        time.sleep(2)
        self.xuanzetiku()
        self.xuanzetiku()   #试卷设置--点击添加题库
        self.exercisetype(('xpath',".//*[@id='innerType0']"),'单选题')
        self.exercisetype(('xpath',".//*[@id='innerType1']"),'多选题')
        self.exercisetype(('xpath',".//*[@id='innerType2']"),'判断题')
        self.exercisesnumber(('xpath',".//*[@id='innerNumber0']"),ts1)
        self.exercisesnumber(('xpath',".//*[@id='innerNumber1']"),ts2)
        self.exercisesnumber(('xpath',".//*[@id='innerNumber2']"),ts3)
        self.exercisescore(('xpath',".//*[@id='innerScore0']"),fs1)
        self.exercisescore(('xpath',".//*[@id='innerScore1']"),fs2)
        self.exercisescore(('xpath',".//*[@id='innerScore2']"),fs3)
        self.xiayibu()
        time.sleep(2)
        self.starttime(startimes) #考试设置--开始时间
        self.endtime(endtimes)    #考试设置--结束时间
        self.totalduration(totalnum) #答题总时间（单位分）
        self.passingscore(jige)      #及格分限制
        self.xiayibu()
        time.sleep(2)
        self.regUser('不登记')
        self.frequency(text1) #参与次数
        self.send(('xpath',".//*[@id='concurrentRsCeilingPrompt']"),text2) #并发人数上限
        self.xiayibu()
        self.examtitle(text3)  #考试标题
        self.examexplain(text4)  #考试说明
        self.webtheme('C:\\testfile\\tp.exe')
        self.apptheme('C:\\testfile\\tp.exe')
        self.xiayibu()
        self.savebutton()
        time.sleep(5)
        self.fabu()
        time.sleep(5)
        self.shenhe()

    def imporexame(self,num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4):
        '''导入题库'''
        time.sleep(3)
        self.tianjia()
        time.sleep(5)
        self.tikuimport('C:\\testfile\\excel.exe') #添加导入的文件路径
        time.sleep(10)
        self.xiayibu() #点击下一步按钮
        self.addexam(num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4)


    def choiceexame(self,num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4):
        '''选择题库执行这个操作，必须有一个已经存在的题库'''
        time.sleep(3)
        self.tianjia()
        time.sleep(5)
        self.tikuchoice()
        self.xiayibu() #点击下一步按钮
        self.addexam(num,fs1,fs2,fs3,ts1,ts2,ts3,startimes,endtimes,totalnum,jige,text1,text2,text3,text4)