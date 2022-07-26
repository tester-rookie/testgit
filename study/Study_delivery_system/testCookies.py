# @Author  : rookie
# @Date    : 2022/5/20 9:50
# @file    : testCookies.py

import json
"""控制台里如何区分字典和json，通过大括号里面的引号区分
   1--单引号是字典
   2--双引号是json
"""
# dict1={"name":"bob"}
# print(dict1)
# print(type(dict1))
#
# print(json.dumps(dict1))

str1='{"name":"bob"}'
print(str1)
print(type(str1))
print(json.loads(str1))