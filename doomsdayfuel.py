# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 11:38:55 2017

@author: jasonros
"""

def answer(m):
    from fractions import Fraction
    size = len(m)
    if size <= 1:
        return [1]
    
    #eliminate selfloops
    for rowi in range(size):
        for coli in range(size):
            if rowi == coli and not m[rowi][coli]:
                m[rowi][coli] = 0
                
    def fractionizeRow(row):
        rowsum = sum(row)
        for coli in range(size):
            if rowsum == 0:
                row[coli] = Fraction(0,1)
            else:
                row[coli]=Fraction(row[coli],rowsum)
        return row
    
    #convert to matrix of probability
    for rowi in range(size):
        m[rowi]=fractionizeRow(m[rowi])

    #check if its all empty
    empty = True
    for rowi in range(size):
        if sum(m[rowi]) != 0:
            empty = False
    if empty:
        return [1]*len(m)
    
    #find loops and eliminate them by recalculating forward propogating row's fraction
    eliminatedrows = [] # list of rows that became all zeros due to recalculated probs but which are not terminals
    for rowi in range(size):
        for coli in range(size):
            if m[rowi][coli] and m[coli][rowi]: # if a two-way transition exists between this row and another
                repeatprob = m[rowi][coli]*m[coli][rowi]
                m[rowi][coli] = (m[rowi][coli]-repeatprob)/(1-repeatprob)
                leftoverprob = 1-m[rowi][coli]
                otherprobtotal = sum(m[rowi])-m[rowi][coli]
                if otherprobtotal > 0:
                    for newcoli in range(size):
                        if not m[rowi][newcoli] or not newcoli == coli:
                            m[rowi][newcoli] = m[rowi][newcoli]/otherprobtotal*leftoverprob
                m[coli][rowi] = 0
                if sum(m[coli]) == 0:
                    eliminatedrows.append(coli)
                m[coli]=fractionizeRow(m[coli]) #renormalize row probs after eliminating backtransition
    print m
    # trace probabilities to their terminals and add to out dict
    def propforward(ri,ci,lastprob,outprobs):
        prob = m[ri][ci]/sum(m[ri])*lastprob
        if sum(m[ci]) == 0:
            if not ci in outprobs.keys():
                outprobs[ci] = prob
            else:
                outprobs[ci] = outprobs[ci] + prob
        else:
            for othercoli in range(size):
                if m[ci][othercoli]:
                    propforward(ci,othercoli,prob,outprobs)    
    outprobs = {}
    rowi=0
    for coli in range(size):
        if m[rowi][coli]:
            propforward(rowi,coli,1,outprobs)
    
    # add 0s for unreachable terminals
    for rowi in range(size):
        if rowi not in outprobs.keys() and rowi not in eliminatedrows and sum(m[rowi]) == 0:
            outprobs[rowi] = 0    
    
    def gcd(a, b):
        while b:      
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    def lcmm(args):
        return reduce(lcm, args)    
    denoms = []
    for key in outprobs.keys():
        if outprobs[key]:
            denoms.append(outprobs[key].denominator)
    denom = lcmm(denoms)
    
    outlist=[]
    for key in outprobs.keys():
        if outprobs[key]:
            outlist.append(outprobs[key].numerator*denom/outprobs[key].denominator)
        else:
            outlist.append(0)
    outlist.append(denom)
    
    return outlist        

m = [[0,1,1,3,0],
     [4,1,2,3,0],
     [2,4,0,3,4],
     [0,0,0,0,0],
     [0,0,0,0,0]]
d = answer(m)
print d
#
#m = [[0,2,1,0,0],
#     [0,0,0,3,4],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0]]
#d = answer(m)
#print d
##answeer = [7,6,8,21]
#
#m = [[0,1],[0,0]]
#d = answer(m)
#print d
#
#m = [[0,1,0,0,0,1],
#     [4,0,0,3,2,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0]]
#
#d2 = answer(m)
#print d2