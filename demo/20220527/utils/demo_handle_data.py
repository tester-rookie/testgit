# @Author  : rookie
# @Date    : 2022/5/28 1:16
# @file    : demo_handle_data.py

import hashlib

def demo_get_mdb5(values):
    mdb5=hashlib.md5()
    mdb5.update(values.encode('utf-8'))
    return mdb5.hexdigest()

if __name__ == '__main__':
    ret=demo_get_mdb5('123')
    print(ret)