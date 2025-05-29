'''
面向对象进阶,如何更好地构建
'''

'''
类中的属性都是私有的，通过@property包装器来包装getter和setter方法，
访问具体的参数
'''


class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'姓名={self._name}，年龄={self._age},正在玩飞行棋')
        else:
            print(f'姓名={self._name},年龄={self._age},正在玩斗地主')


class Clock(object):
    '''数字时钟'''

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second



if __name__ == '__main__':
    p1 = Person(22, '小赤佬')
    print(p1.name)
    print(p1.age)
    p1.age = 17
    p1.name = '小瘪三'
    print(p1.name)
    print(p1.age)
    p1.play()
