#coding=utf-8
from pageElement.pageoperation.sumhtpage import Sumpage

class Cc(Sumpage):
    def tt(self):
        self.htdrks('admin','abc123','100','1','1','1','30','30','40','2019-07-06 09:57:33','2019-07-07 09:57:33','1','60','1','1','自动化数据','testwh')
    def vo(self):
        self.htnodrawvote('admin','abc123','自动化wh','33','2019-06-17 15:16:19','2019-06-25 15:16:19','1','自动化投票wh','自动化说明')
    def js(self):
        self.htxzjs('admin','abc123','100','1','1','1','30','30','40','2019-07-06 09:57:33','2019-07-07 09:57:33','1','60','1','2','1','自动化数据','testwh',)
wh=Cc()
wh.js()