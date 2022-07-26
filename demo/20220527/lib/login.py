# @Author  : rookie
# @Date    : 2022/5/28 0:36
# @file    : login.py
from common.demo_baseApi import BaseApi
from utils.demo_handle_data import demo_get_mdb5
from utils.get_yaml_data import demo_get_yaml_data


class Login(BaseApi):
    def login(self,indata):
        return self.send_resquest(indata)

if __name__ == '__main__':
    account=demo_get_yaml_data('../data/apiconf.yaml')['Login']['account']
    account['password']=demo_get_mdb5(account['password'])
    ret=Login().login(account)
    print(ret.text)
