'''
python函数
'''
import random


def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += random.randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


'''
有一个字典，获取到字典值
'''
product = {
    'name': '小李',
    'age': 13
}


def gys(x, y):
    if x > y:
        x, y = y, x
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def gbs(x, y):
    num = gys(x, y)
    return x * y // num


def sushu(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return num != 1

def foo():
    global a # 使用全局变量a
    a=200
    print(a)



# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('商品对应的年龄是%d' % product['age'])
    print(add())
    print("最大公约数:%d" % gys(16, 20))
    print("最小公倍数:%d" % gbs(16, 20))
    print(sushu(5))
    a=100
    foo()

