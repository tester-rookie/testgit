import json

import requests
import hashlib
# psd='xintian'
# #实例化一个md5对象
# md5=hashlib.md5()
# #调用update方法进行加密
# md5.update(psd.encode('utf-8'))
# # 调用hexdigest方法获取加密结果
# login_psw=md5.hexdigest()
# print(login_psw)

host='http://121.41.14.39:8082'
# NAME_PSW = {'username':'ka0518','password':login_psw}
# url=f'{host}/account/sLogin'
# resp=requests.post(url,data=NAME_PSW)
# print(resp.text)

def login(name,psd):
    palyload={'username':name,'password':get_md5(psd)}
    url=f'{host}/account/sLogin'
    resp=requests.post(url,data=palyload)
    # print('请求头--headers>>>',resp.request.headers)
    # print('响应头--header>>>',resp.headers)
    return resp

def get_md5(psd:str):
    md5=hashlib.md5()
    md5.update(psd.encode('utf-8'))
    return md5.hexdigest()
if __name__ == '__main__':
    a=login('wa0312','61412')
    #print('a.content-->',a.content)
    print('a.text-->',a.text)

# b=a.text
# json.loads(b)
# print('b-->',b)

