# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 21:17:17 2017

@author: jasonros
"""

def answers(s):
    try:
        return max([s.count(s[:x]) for x in range(len(s)) if s[:x]*s.count(s[:x]) == s])
    except:
        return 1

print answers('ababababababababa')