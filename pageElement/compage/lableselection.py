#coding=utf-8
from common.com import Comm
from selenium.webdriver.support.ui import WebDriverWait



class Lable(Comm):
    '''后台标签选择元素汇总'''
    management_loc=('xpath',".//*[@id='areTop']/li[2]/a")
    competition_loc=('xpath',".//*[@id='areleft']/div[2]/dl[1]/dt/a")
    vote_loc=('xpath',".//*[@id='areleft']/div[2]/dl[2]/dt/a")
    exam_loc=('xpath',".//*[@id='areleft']/div[2]/dl[3]/dt/a")
    questionnaire_loc=("xpath",".//*[@id='areleft']/div[2]/dl[4]/dt/a")
    bank_loc=("xpath",".//*[@id='areTop']/li[3]/a")
    question_loc=('xpath',".//*[@id='areleft']/div[3]/dl[1]/dt/a")
    exercises_loc=("xpath",".//*[@id='areleft']/div[3]/dl[2]/dt/a")

    def ifcaozuo(self):
         iframe = self.driver.find_elements_by_tag_name('iframe')[1]
         self.driver.switch_to_frame(iframe)

    def activity_competition(self):
        '''点击标签--活动管理【竞赛】'''
        self.click(self.management_loc)
        try:
            WebDriverWait(self.driver,5,5).until(lambda x: x.find_element_by_xpath(u".//*[@id='areleft']/div[2]/dl[1]/dt/a"))
            self.click(self.competition_loc)
        except Exception as msg:
            print("元素未找到")
        self.ifcaozuo()

    def activity_vote(self):
        '''点击标签--活动管理【投票】'''
        self.click(self.management_loc)
        try:
            WebDriverWait(self.driver,5,5).until(lambda x: x.find_element_by_xpath(u".//*[@id='areleft']/div[2]/dl[2]/dt/a"))
            self.click(self.vote_loc)
        except Exception as msg:
            print("元素未找到")
        self.ifcaozuo()

    def  activity_exam(self):
         '''点击标签--活动管理【考试】'''
         self.click(self.management_loc)
         try:
             WebDriverWait(self.driver,5,5).until(lambda x: x.find_element_by_xpath(u".//*[@id='areleft']/div[2]/dl[3]/dt/a"))
             self.click(self.exam_loc)
         except Exception as msg:
             print("元素未找到")
         self.ifcaozuo()

    def  activity_questionnaire(self):
         '''点击标签--活动管理【问卷】'''
         self.click(self.management_loc)
         try:
             WebDriverWait(self.driver,5,5).until(lambda x: x.find_element_by_xpath(u".//*[@id='areleft']/div[2]/dl[4]/dt/a"))
             self.click(self.questionnaire_loc)
         except Exception as msg:
             print("元素未找到")
         self.ifcaozuo()

    def question_bank(self):
        '''点击标签--内容管理【题库】'''
        self.click(self.bank_loc)
        try:
            WebDriverWait(self.driver,5,5).until(lambda x: x.find_element_by_xpath(u".//*[@id='areleft']/div[3]/dl[1]/dt/a"))
            self.click(self.question_loc)
        except Exception as msg:
              print("元素未找到")
        self.ifcaozuo()

    def exercises_bank(self):
        '''点击标签--内容管理【习题】'''
        self.click(self.bank_loc)
        try:
            WebDriverWait(self.driver,5,5).until(lambda x: x.find_element_by_xpath(u".//*[@id='areleft']/div[3]/dl[2]/dt/a"))
            self.click(self.question_loc)
        except Exception as msg:
              print("元素未找到")
        self.ifcaozuo()

