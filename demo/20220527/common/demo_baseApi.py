# @Author  : rookie
# @Date    : 2022/5/28 0:45
# @file    : demo_baseApi.py
from utils.get_yaml_data import demo_get_yaml_data
import inspect,requests


class BaseApi():
    def __init__(self):
        self.data=demo_get_yaml_data('../data/apiconf.yaml')[self.__class__.__name__]

    def send_resquest(self,indata):
        host=self.data['host']
        url,method=self.data[inspect.stack()[1][3]].values()
        ret=requests.request(url=f'{host}{url}',method=method,data=indata)
        return ret
