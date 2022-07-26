# @Author  : rookie
# @Date    : 2022/5/25 22:15
# @file    : baseApi.py

import requests,inspect,sys

from study.Study_delivery_system.Utils.handle_yaml import get_yaml_data
from study.Study_delivery_system.conf.public_conf import host


class BaseApi:
    def __init__(self): #初始化方法
        """
        根据子类类名，获取接口的url和请求方式
        """
        #__class__.__name__ 获取子类名称
        self.data=get_yaml_data('../conf/apiConfig.yaml')[self.__class__.__name__]

    def request_send(self,indata):
        """
        公共请求方法
        :param indata: 请求体
        :return: 调用接口的响应值
        """
        funcName=inspect.stack()[1][3]
        path,method=self.data[funcName].values()
        resp=requests.request(method=method,url=f'{host}{path}',data=indata)
        return resp

def a():
    print('执行函数---a')
    print('谁调用了函数a--->',inspect.stack()[1][3])

def b():
    print('执行函数---b')
    a()
    print('b函数当前自己的函数名--->',sys._getframe().f_code.co_name)


# b()
if __name__ == '__main__':
    a()