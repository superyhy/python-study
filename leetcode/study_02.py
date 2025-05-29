'''
python存在两种循环结构 一种是for in循环，一种是while循环
'''
import math
import random

sum = int(0)
for i in range(100):
    sum += i
print(sum)

'''
循环解答问题
'''
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('答对了')
        break
print('总共回答了%s次' % counter)
if counter > 7:
    print("你是个傻逼")

'''
判断一个正整数是不是素数
'''
num = int(input("请输入正数："))
end = int(math.sqrt(num))
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print("num是个素数")
else:
    print("num不是素数")

'''
计算最大公约数和最小公倍数
'''
x = int(input('x='))
y = int(input('y='))
if x > y:
    x, y = y, x
for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print('%d和%d的最大公约数是%d', (x, y, i))
        print('%d和%d的最大公倍数是%d', (x, y, int((x * y) / i)))
        break
