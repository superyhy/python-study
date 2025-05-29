import re

username = input('请输入用户名：')
qq = input('请输入QQ号：')

# match函数第一个参数是正则表达式字符串
# match函数第二个参数是校验的对象
m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
if not m1:
    print('请输入有效的用户名。')

m2 = re.fullmatch(r'[1-9]\d{4,11}', qq)
if not m2:
    print('请输入有效的QQ号')
if m1 and m2:
    print('你输入的信息是有效的 ')

pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也不是110或119，王大锤的手机号才是15600998765。'''
# 方法一：查询所有匹配并保存一个列表中
tels_list = re.findall(pattern, sentence)
for tel in tels_list:
    print(tel)
print('-----分割线-------')

sentence = 'Oh,shit! 你是傻逼吗？Fuck you.'
purified = re.sub('fuck|shit|[傻煞笔]|[比煞笔查去死奥]', '*', sentence, flags=re.IGNORECASE)
print(purified)

poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentences_list = re.split(r'[，。]', poem)
sentences_list = [sentence for sentence in sentences_list if sentence]
for sentence in sentences_list:
    print(sentence)
