'''
python面向对象编程
'''
import string


class Student(object):
    def _init_(self,name:string,age:int):
        self.name = name
        self.age = age