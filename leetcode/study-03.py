'''
求水仙花数
'''
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100 % 10
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

'''
正整数的反转
'''
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

'''
百钱百鸡问题
'''
for x in range(0, 100):
    for y in range(0, 100):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (x, y, z))

'''
斐波那契数列
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(11):
    print(fibonacci(i))


