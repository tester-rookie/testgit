# @Author  : rookie
# @Date    : 2022/5/28 0:16
# @file    : get_yaml_data.py

import yaml

def demo_get_yaml_data(fileDir):
    with open(fileDir,'r',encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())

if __name__ == '__main__':
    ret_data=demo_get_yaml_data('../data/apiconf.yaml')
    print(ret_data)
    print(ret_data['Login']['host'])
    print(ret_data['Login']['account'])
