from enum import Enum
class Student:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def study(self, course_name):
        print(f'{self._name}正在学习{course_name}')


class Student1:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Triangle(object):
    '''三角型'''
    __slots__ = ('_a', '_b', '_c')

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        '''判断能否组成三角型'''
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self._a) * (p - self._b) * (p - self._c)) ** 0.5


class Person:
    '''人'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student3(Person):
    def __init__(self, name, age):
        super.__init__(name, age)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')


class Teacher3(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')



if __name__ == '__main__':
    stu = Student('王大锤', 27)
    stu.study('Python程序')
    print(stu._name)

    stu1 = Student1('李大炮', 31)
    print(stu1.name)

    triangle = Triangle(1, 3, 4)
    print(f'是否能组成三角型{Triangle.is_valid(1, 2, 3)}')
    print(f'三角型的周长是{triangle.perimeter()}')
    print(f'三角型的面积是{triangle.area():.2f}')

    teacher = Teacher3('程序员', 24, '教授')
    teacher.teach('C++程序设计')
    teacher2 = Teacher3('程序员', 24, '教授')

