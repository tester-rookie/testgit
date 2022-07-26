# @Author  : rookie
# @Date    : 2022/5/25 22:49
# @file    : login.py
from study.Study_delivery_system.Common.baseApi import BaseApi
from study.Study_delivery_system.Utils.handle_data import get_md5
from study.Study_delivery_system.conf.public_conf import login_account

class Login(BaseApi):
    def login(self,indata):
        resp=self.request_send(indata)
        return resp

if __name__ == '__main__':
    login_account['password']=get_md5(login_account['password'])
    ret=Login().login(login_account)
    print(login_account)
    print(type(login_account))
    print(ret.text)
