'''
python面向对象编程
'''
import math
import study_05


class Student(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name} 正在学习 {course_name}')

    def watch_movie(self):
        if self.age < 18:
            print(f'{self.name}来看一下小猪佩奇')
        else:
            print(f'{self.name}可以看其他的视频')


'''
如何在类中声明私有参数和私有方法，默认是公有的
'''


class Test(object):
    def __int__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test_)


'''
定义一个描述平面上的点和计算的类
'''


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        '''
        移动到指定的位置上
        :param x:
        :param y:
        :return:
        '''
        self.x = x
        self.y = y

    def move_by(self, x, y):
        '''
        移动指定的增量
        :param x:
        :param y:
        :return:
        '''
        self.x += x
        self.y += y

    def distance_to(self, other):
        '''
        计算和另一个点的距离
        :param other:
        :return:
        '''
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return f'({self.x},{self.y})'


if __name__ == '__main__':
    student1 = Student('小瘪三', 39)
    student1.study('英语')
    student1.watch_movie()
    print('---------------------------')
    point1 = Point(1,2)
    print(point1)
    point1.move_to(3,4)
    print(point1)
    point2 = Point(4,5)
    print(point2)
    print(point1.distance_to(point2))
    print(study_05.generate_code(4))

