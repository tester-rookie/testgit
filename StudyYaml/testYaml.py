# -*- coding:utf-8 -*-
import yaml

# y = yaml.load(file())
file = open('AllType.yaml', 'r', encoding='utf-8')
data=yaml.load(file,Loader=yaml.FullLoader)
print(data)
