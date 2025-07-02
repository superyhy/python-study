# 单行注释
"""
多行注释
"""
import math

year = int(input('请输入年份：'))
is_leap = year % 4 == 0 and year % 100 != 0 and year % 400 == 0
print(is_leap)

username = input('请输入用户名：')
password = input('请输入口令：')
if username == 'admin' and password == '123':
    print("身份验证通过！")
else:
    print("身份验证失败！")

x = float(input('输入x='))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

"""
英制单位英寸和工制单位厘米的相互转换
"""
value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%.2f英寸=%.2f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.2f厘米=%.2f英寸' % (value, value / 2.54))
else:
    print('单位输入错误')

'''
输入三角形的三边长，计算面积和周长
'''
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a + b > c and a + c > b and b + c > a:
    print('周长：%.2f' % (a + b + c))
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('面积:%.2f' % area)
else:
    print("无法组成三角形")