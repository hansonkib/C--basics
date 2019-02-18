# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:00:38 2019

@author: HANSON
"""

class Person:
    def _init_(self, name,age):
        self.name=name
        self.age=age
p1=Person("john",23)
print(p1.name)
print(p1.age)