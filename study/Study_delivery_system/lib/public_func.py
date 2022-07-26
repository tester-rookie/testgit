# @Author  : rookie
# @Date    : 2022/5/20 11:12
# @file    : public_func.py

import hashlib
import requests
from study.Study_delivery_system.conf.public_conf import login_account, host


def get_md5(value:str):
    '''
    md5加密
    :param value:
    :return: md5加密值
    '''
    md5=hashlib.md5()
    md5.update(value.encode('utf-8'))
    return md5.hexdigest()

def login():
    '''
    登录接口
    :return: 登录响应响应消息体
    '''
    name = login_account['name']
    psd = login_account['password']
    psd = get_md5(psd)
    url=f'{host}/account/sLogin'
    palyoad = {'username': name, 'password': psd}
    resp = requests.post(url=url, data=palyoad)
    print(resp.text)
    return resp.text


def list_shop():
    headers={"Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTMyMTUzNDcsInVzZXJJZCI6MTM4MTYsInVzZXJuYW1lIjoid2EwMzEyIn0.PNqYYX8k918f01qo3alWHqU02RaXSF7PSOvGBI087Mo"}
    playload='page=1&limit=20'
    url=f'{host}/shopping/myShop'+playload
    resp=requests.get(url=url,headers=headers)

    print(resp.text)

if __name__ == '__main__':
    list_shop()
