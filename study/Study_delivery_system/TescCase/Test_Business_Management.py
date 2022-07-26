# @Author  : rookie
# @Date    : 2022/5/21 0:08
# @file    : Test_Business_Management.py
import pytest,allure

from study.Study_delivery_system.conf.public_conf import host


@allure.feature('业务管理模块')
class Test_B_M():
    def test_list_shop(self):
        url=host+'/shopping/myShop'


