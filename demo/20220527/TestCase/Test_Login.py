# @Author  : rookie
# @Date    : 2022/5/29 11:39
# @file    : Test_Login.py
from lib.login import Login
from utils.demo_handle_data import demo_get_mdb5
from utils.get_yaml_data import demo_get_yaml_data
import pytest,allure,os

@allure.feature('登陆模块')
class Test_login():
    def test_login_001(self):
        account=demo_get_yaml_data('../data/apiconf.yaml')['Login']['account']
        account['password'] = demo_get_mdb5(account['password'])
        ret=Login().login(account)
        assert '成功' in ret.text

if __name__ == '__main__':
    pytest.main(['Test_Login.py','-s','--alluredir','../report/temp','--clean-alluredir'])
    os.system('allure generate ../report/temp -o ../report/report --clean')