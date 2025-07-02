'''
异常处理机制
'''
import csv
import json
from random import random

import requests as requests

file = None
try:
    file = open('致橡树.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件')
except LookupError:
    print('指定了未知的编码')
except UnicodeDecodeError:
    print('读取文件时解码错误')
finally:
    if file:
        file.close()

try:
    with open('guido.jpg', 'rb') as file1, open('吉多.jpg', 'wb') as file2:
        data = file1.read(512)
        while data:
            file2.write(data)
            data = file1.read()
except FileNotFoundError:
    print('指定的文件无法打开')
except IOError:
    print('读取文件时出现错误')
print('程序执行结束')

'''
对象的序列化和反序列化
'''
my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))

with open('data.json', 'w') as file:
    json.dump(my_dict, file)

with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)

'''
http请求获取数据
'''
resp = requests.get("https://apis.tianapi.com/toutiaohot/index?key=ed97347e0e1fef470e01f1863f0f44a7")
if resp.status_code == 200:
    data_json = resp.json()
    result = data_json['result']
    index = 1
    for data in result['list']:
        print(f'{index}.{data["word"]}')
        index += 1

with open('scores.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)

with open('scores.csv', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for data_list in reader:
        print(reader.line_num, end='\t')
        for elem in data_list:
            print(elem, end='\t')
        print()