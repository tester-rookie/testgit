# @Author  : rookie
# @Date    : 2022/5/25 22:56
# @file    : handle_yaml.py
import yaml

def get_yaml_data(fileDir):
    with open(fileDir,encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())

if __name__ == '__main__':
    ret=get_yaml_data('../conf/apiConfig.yaml')
    print(ret)
