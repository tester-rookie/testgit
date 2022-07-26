# @Author  : rookie
# @Date    : 2022/5/20 13:36
# @file    : demo.py
import json

str1="""{
	"code":20000,
	"data":{
		"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTMwMjg0NDgsInVzZXJJZCI6MTM4MTYsInVzZXJuYW1lIjoid2EwMzEyIn0.J-LgIDaTT5HXUtNt3k-gGUpxICK10MTxtWBQJf6qQlo"
	},
	"flag":"松勤教育",
	"msg":"成功",
	"success":false
}"""

print(str1)
json.loads(str1)
print(type(str1))