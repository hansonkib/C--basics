# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:57:25 2019

@author: HANSON
"""

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nExamples of recurion results")
tri_recursion(6)