# @Author  : rookie
# @Date    : 2022/5/25 21:38
# @file    : handle_data.py

import hashlib
import base64

def get_md5(values:str):
    """
    获取md5加密值
    :param values:
    :return:
    """
    md5=hashlib.md5()
    md5.update(values.encode('utf-8'))
    return md5.hexdigest()

def get_base64(values:str):
    '''

    :param values:
    :return:
    '''
    # a = input("base64加密：")  # input()函数接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
    encode = base64.b64encode(values.encode('utf-8'))  # 因为3.x中字符都为unicode编码，而b64encode函数的参数为byte类型，所以必须先转码
    print(("**********encryption complete**********\n:"), str(encode, 'utf-8'))  # 将byte转换回去就好了，如果不转的化，输出结果会被字符串b包围
    return str(encode,'utf-8')


if __name__ == '__main__':
    ret=get_base64('billapp')
    print(ret)

