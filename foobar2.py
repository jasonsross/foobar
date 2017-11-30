# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 21:42:20 2017

@author: jasonros
"""

def answer(l, t):
    # your code here
    for ind1 in range(len(l)):
        total = l[ind1]
        if total == t:
                return [ind1,ind1]
        for ind2 in range(ind1+1,len(l)):
            total += l[ind2]
            if total == t:
                return [ind1,ind2]
    return [-1,-1]


    
l = [4,3,10,2,8]
t = 12
print answer(l,t)

l = [12,1,3]
t = 12
print answer(l,t)

l = [12,1,3]
t = 16
print answer(l,t)

l = [12,1,3,4]
t = 15
print answer(l,t)