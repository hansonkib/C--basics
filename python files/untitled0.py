# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 23:08:57 2018

@author: HANSON
"""
from time import clock
print("enter your name")
start_time=clock()
name = input()
curren=clock()
elapse=curren-start_time
print("hello",name,"imagine you took",elapse,"to remember your name")