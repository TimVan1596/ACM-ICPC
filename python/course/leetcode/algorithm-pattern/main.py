# -*- coding:utf-8 -*-
# @Time:2021/5/8 13:19
# @Author:TimVan
# @File:main.py
# @Software:PyCharm

class Parent:
    a = 1


person = Parent()
human = Parent()
print("Parent.a=" + str(Parent.a))
print("person.a=" + str(person.a)+"\n")
person.a = 999
print("Parent.a=" + str(Parent.a))
print("person.a=" + str(person.a))
print("human.a=" + str(human.a)+"\n")
Parent.a = 999
print("Parent.a=" + str(Parent.a))
print("person.a=" + str(person.a))
