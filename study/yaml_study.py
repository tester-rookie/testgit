import yaml

yaml_str="""
name:rookie
age:20
job:Tester
"""
res_dict1=yaml.load(yaml_str,Loader=yaml.FullLoader)
print(yaml_str)
print(res_dict1)
print(type(res_dict1))

yaml_str = """ 
name: 灰蓝 
age: 0 
job: Tester 
"""
y = yaml.load(yaml_str)
print(y)
#
# python_obj={"name":u"老王",
#             "age":18,
#             "job":"king"}
# y = yaml.dump(python_obj)
# print(y)
# print(type(y))
