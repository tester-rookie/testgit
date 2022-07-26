#-*- coding: utf-8 -*-
#@File    : xttoken.py
#@Time    : 2021/5/24 21:21
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/5/24 
import requests,hashlib
HOST = "http://121.41.14.39:8082"
def get_md5(psw):#加密函数
    #1- 实例化  一个md5对象
    md5 = hashlib.md5()
    #2- 调用加密方法
    md5.update(psw.encode("utf-8"))
    #3- 返回加密后结果
    return md5.hexdigest()#16进制


def login(inData):
    #1- url
    url = f"{HOST}/account/sLogin"
    #2- 请求头--可以省略
    #3- 请求体
    inData["password"] = get_md5(inData["password"])#字典修改值
    payload = inData
    #4- 发送请求
    resp = requests.post(url,data=payload)
    #5- 获取响应数据--响应体数据
    #print(resp.text)#字符串数据
    print(resp.json())#字典数据

if __name__ == '__main__':
    login({"username":"sq0777","password":"xintian"})