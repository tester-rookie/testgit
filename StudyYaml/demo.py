import yaml

data=open('test.yaml','r',encoding='utf-8')
y=yaml.load(data,Loader=yaml.FullLoader)
print(y)