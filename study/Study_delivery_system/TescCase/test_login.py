# @Author  : rookie
# @Date    : 2022/5/20 10:56
# @file    : test_login.py

import pytest,allure,os

from study.Study_delivery_system.Utils.handle_data import get_md5
from study.Study_delivery_system.conf.public_conf import login_account
from study.Study_delivery_system.lib.login import Login


@allure.feature('登录模块')
class Test_Login():
    def setup_class(self):
        pass
    def test_login(self):
        login_account['password'] = get_md5(login_account['password'])
        ret=Login().login(login_account)
        assert '成功' in ret.text


if __name__ == '__main__':
    pytest.main(['test_login.py','-s','--alluredir','../data/report/tmp','--clean-alluredir'])
    os.system('allure generate ../data/report/tmp -o ../data/report/report --clean')




