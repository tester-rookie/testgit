import pytest
import os
import allure

#1、定义函数类型--测试用例
def test_01():
    assert 1 + 1 == 2

def test_02():
    assert 2 +2 == 4

def test_03():
    assert 2 +1 == 4
#2、封装测试类
@allure.feature('登录模块')#一级标题
class TestLogin():
    def setup_class(self):
        print('执行测试类之前，的初始化动作')
    def teardown_class(self):
        print('该测试类的环境清除')

    @allure.story('登录login01')#二级标签下
    @allure.title('login01')#标题
    @pytest.mark.parametrize('a,b',[(1,2),(2,3),(3,9)])  #('变量名',[1,2,3])
    def test_login01(self,a,b):
        print('----test_login01-----')
        assert a + 1 == b

    @allure.story('登录login02')
    def test_login02(self):
        print('----test_login02-----')
        assert 1 + 1 == 2

@allure.feature('购物模块')#一级标题
class TestShopping():
    def setup_class(self):
        print('执行测试类之前，的初始化动作')
    def teardown_class(self):
        print('该测试类的环境清除')

    @allure.story('购物shopping01')
    @allure.title('shopping_tile')
    def test_shopping01(self):
        print('----test_shopping01-----')
        assert 1 + 1 == 2

if __name__ == '__main__':
    #需要打印对应的信息  -s
    #1  --alluredir 存放目录
    pytest.main(['test_func01.py','-s','--alluredir','../report/tmp','--clean-alluredir'])
    # 2  allure generate allure报告
    #os.system('allure generate 报告需要的数据 -o 报告存放的目录 --clean')    指令不需要逗号
    os.system('allure generate ../report/tmp -o ../report/report --clean')

