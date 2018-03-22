# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: zhuce_pub.py
@time: 2017/4/27 12:49
"""
import yaml,time,os
from untils.huoqu_xingneng import getnencun,caijicpu
from config.config import TestappPackage
from untils.log import LOG
from untils.recording_txt import write_recording
'''注册相关的逻辑'''
class Regust:
    def __init__(self,deriver):
        self.deriver=deriver
        patth = os.getcwd()
        self.file = open(patth + '\\data\\data_dingwei.yaml', 'r', encoding='utf-8')
        self.data=yaml.load(self.file)
        self.file.close()
        self.regest_for=self.data['zhuce']['zhuce_ye_id']
        self.regest_deng=self.data['zhuce']['z_denglu_id']
        self.regest_zhu=self.data['zhuce']['zhuce_id']
        self.user=self.data['zhuce']['zhu_user_id']
        self.passw = self.data['zhuce']['zhuce_pass_id']
        self.yanzhengma=self.data['zhuce']['yanzhengma_id']
        self.yanzhengmahuo=self.data['zhuce']['huoquyanzhengma_id']
        self.regist_fail=self.data['zhuce']['fail_id']
        self.regest_btn=self.data['zhuce']['zhuce_btn']
    def register1(self,suc,user,password,yanzhengma):
        self.deriver.find_elements_by_id(self.regest_for)[2].click()
        self.deriver.find_element_by_id(self.regest_deng).click()
        self.deriver.find_element_by_id(self.regest_zhu).click()
        use=self.deriver.find_element_by_id(self.user)
        use.clear()
        use.send_keys(user)
        passwor=self.deriver.find_element_by_id(self.passw)
        passwor.clear()
        passwor.send_keys(password)
        yanzheng=self.deriver.find_element_by_id(self.yanzhengma)
        yanzheng.clear()
        yanzheng.send_keys(yanzhengma)
        path = os.getcwd()
        pathw = path + '\\testpang\\%s.jpg' % (str(time.time())[:10])
        if suc =='1' or suc==1:
            self.deriver.find_element_by_id(self.regest_btn).click()
            neicun = getnencun(TestappPackage)
            cpu = caijicpu(TestappPackage)
            write_recording(cpu=cpu, neicun=neicun)
            LOG.info('注册占内存:%s,cpu：%s' % (neicun, cpu))
            self.deriver.get_screenshot_as_file(pathw)
            time.sleep(2)
            self.text_fail=self.deriver.find_element_by_id(self.regist_fail)
            self.rerun_test=self.text_fail.text
            return self.rerun_test
        if suc ==0:
            self.deriver.get_screenshot_as_file(pathw)
    def register2(self,suc,user,password,yanzhengma):
        self.deriver.find_elements_by_id(self.regest_for)[2].click()
        self.deriver.find_element_by_id(self.regest_deng).click()
        self.deriver.find_element_by_id(self.regest_zhu).click()
        use=self.deriver.find_element_by_id(self.user)
        use.clear()
        use.send_keys(user)
        passwor=self.deriver.find_element_by_id(self.passw)
        passwor.clear()
        passwor.send_keys(password)
        if suc ==1:
            self.deriver.find_element_by_id(self.yanzhengmahuo).click()
            neicun = getnencun(TestappPackage)
            cpu = caijicpu(TestappPackage)
            LOG.info('注册占内存:%s,cpu：%s' % (neicun, cpu))
            self.text_fail=self.deriver.find_element_by_id(self.regist_fail).text
        if suc ==0:
            yanzheng = self.deriver.find_element_by_id(self.yanzhengma)
            yanzheng.clear()
            yanzheng.send_keys(yanzhengma)
            self.deriver.find_element_by_id(self.regest_btn).click()
            neicun = getnencun(TestappPackage)
            cpu = caijicpu(TestappPackage)
            write_recording(cpu=cpu, neicun=neicun)
            LOG.info('注册占内存:%s,cpu：%s' % (neicun, cpu))