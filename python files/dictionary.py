# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:15:19 2019

@author: HANSON
"""

thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
print(thisdict)
#accessing items
x = thisdict["model"]
print(x)
y = thisdict.get("year")
print(y)
#Loop Through the dictionary
for y in thisdict:
    print(y)
for z in thisdict.values():
    print(z)
#Checking if the key exists    
if "model" in thisdict:
    print("yes 'model' is one of the keys in the thisdict dictionary")
#Dictionary Length    
print(len(thisdict))    