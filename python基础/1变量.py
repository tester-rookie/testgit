import math
a=1/3
b=2/3
c=1/4

#向下取整
print('向下取整',int(a))
#向上取整
print('向上取整',math.ceil(a))
print('向上取整',math.ceil(b))
#四舍五入
print('四舍五入',round(b))
print('四舍五入',round(a))
#分别去整数和小数部分
print('分别去整数和小数部分',math.modf(c))
d=math.modf(c)




e=d[0]
f=d[1]
print('e=',e)
print('f=',f)
