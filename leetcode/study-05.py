'''
字符串、常用的数据结构写法
'''
import random
import string
from typing import List

s1 = '\'hello,world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

'''
格式化字符串的写法
'''
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print(f'{a} * {b} = {a * b}')

'''
列表定义
'''
list1 = [1, 3, 5, 7, 100]
list2 = ['hello'] * 3
print(list2)
print(len(list1))
print(list1[0])
print(list1[4])
print(list1[-1])
print(list1[-3])
list1[2] = 300

for elem in list1:
    print(f'数组遍历结果：{elem}')
for index, elem in enumerate(list1):
    print(f'数组遍历结果：{index} {elem}')

'''
列表定义
'''
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1, key=len, reverse=True)
list1.sort(reverse=True)
print(list2)
print(list1)

'''
列表构造
'''
f = [x for x in range(1, 10)]
print(f)

f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

f = [x ** 2 for x in range(1, 1000)]
print(f)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


for val in fib(20):
    print(val)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, elem in enumerate(nums):
            if target - elem in hashmap:
                return [hashmap[target - elem], index]
            hashmap[elem] = index
        return []


'''
把几个元素组合到一起，形成元组
元组中的元素是无法修改的，是线程安全的
一个方法返回多个值，推荐使用元组
'''
t = ('骆昊', 38, True, '四川成都')
print(t)
print(t[0])
print(t[3])
for member in t:
    print(member)
# 元组转列表
t = ('王大锤', 20, True, '云南昆明')
peopleList = list(t)
print(peopleList)
# 列表转元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

'''
集合，不允许有重复元素
'''
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
# 创建集合的推导式语法
set4 = {num for num in range(1, 100) if num % 3 == 0 and num % 5 == 0}
print(set4)

'''
向集合中添加元素，和从集合删除元素
'''
set1.add(4)
set1.add(5)
set4.update([11, 12])
set4.discard(5)
if 4 in set4:
    set4.remove(4)
print(set1)
print(set4)

print('集合不为空' if not set1 & set4 else '集合为空')
print(set1 | set4)
print(set1 - set4)
print(set1 ^ set4)

'''
使用字典，字典存储的数据是键值对
'''
scores = {'骆昊': 98, '白元芳': 78, '狄仁杰': 82}
print(scores)
items1 = dict(one=1, two=2, three=3, four=4)
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)

for key in scores:
    print(f'{key}:{scores[key]}')

'''
生成一个指定长度的随机字符串
'''


def generate_code(code: int) -> string:
    all_chars = 'aoaidjkak139197120101'
    length = int(len(all_chars) - 1)
    ans = ''
    for i in range(code):
        index = random.randint(0, length)
        ans += all_chars[index]
    return ans


'''
杨辉三角
'''


def yanghui():
    num = int(input('Number of rows:'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)  # 构建一个全是None的列表
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()  # 一轮循环结束换行


'''
幸运的基督徒
'''


def jdt():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print("基" if person else "非",end='')


if __name__ == '__main__':
    print(generate_code(5))
    yanghui()
    jdt()
