# @Author  : rookie
# @Date    : 2022/5/25 21:38
# @file    : handle_data.py

import hashlib

def get_md5(values:str):
    """
    获取md5加密值
    :param values:
    :return:
    """
    md5=hashlib.md5()
    md5.update(values.encode('utf-8'))
    return md5.hexdigest()

