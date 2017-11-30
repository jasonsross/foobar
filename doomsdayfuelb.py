# -*- coding: utf-8 -*-
"""
Created on Mon Aug 07 09:48:10 2017

@author: jasonros
"""
from fractions import Fraction
def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def fractionizeMatrix(m):
    size = len(m)
    for rowi in range(size):
        rowsum = sum(m[rowi])
        for coli in range(size):
            if rowsum == 0:
                m[rowi][coli] = Fraction(0,1)
            else:
                m[rowi][coli]=Fraction(m[rowi][coli],rowsum)
    return m

def identityMatrix(size):
    I = []
    for rowi in range(size):        
        I.append([])
        for coli in range(size):
            if rowi == coli:
                I[rowi].append(1)
            else:
                I[rowi].append(0)
    return I

def subtractMatrix(m1,m2):
    size = len(m1)
    mout = list(m1) #copy it to get the same-size matrix, all elements will be replaced below
    for rowi in range(size):
        for coli in range(size):
            mout[rowi][coli]=m1[rowi][coli]-m2[rowi][coli]
    return mout

def multiplyMatrix(L,R):
    out = list(R) # copy just to get sizing right before assigning values
    sizeL = len(L)
    widthR = len(R[0])
    for rowli in range(sizeL):
        for colRi in range(widthR):
            currentSum = 0
            for colLi in range(sizeL):
                currentSum += L[rowli][colLi]*R[colLi][colRi]
            out[rowli][colRi] = currentSum
    return out

def gcd(a, b):
        while b:      
            a, b = b, a % b
        return a
    
def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(args):
    return reduce(lcm, args)

def answer(m):
    size = len(m)
    if size == 1:
        return [1,1]
    
    rules = []
    for rowi in range(size):
        if sum(m[rowi]) != 0:
            rules.append(rowi)
    m = fractionizeMatrix(m)
    
    if len(rules) > 1:
        #build R and Q matrices
        R = []
        Q = []
        i = -1
        for rowi in range(size):
            if sum(m[rowi]) != 0:
                i+=1
                Q.append([])
                R.append([])
                for coli in range(size):
                    if coli in rules:
                        Q[i].append(m[rowi][coli])
                    else:
                        R[i].append(m[rowi][coli])
        I = identityMatrix(len(Q))
        dif = subtractMatrix(I,Q)
        F = getMatrixInverse(dif)
        FR = multiplyMatrix(F,R)
        
        outprobs = FR[0]        
    else:
        outprobs = m[0][1:]
    
    denoms = []
    for i in range(len(outprobs)):
        denoms.append(outprobs[i].denominator)
    lcd = lcmm(denoms)
    for i in range(len(outprobs)):
        outprobs[i] = outprobs[i].numerator*lcd/outprobs[i].denominator
    outprobs.append(lcd)
    return outprobs
    
    
maze = [[1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
d = answer(maze)
print d

#maze = [[0,2,1,0,0],
#     [0,0,0,3,4],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0]]
#d = answer(maze)
#print d
##answeer = [7,6,8,21]
#
#maze = [
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#    ]
#d = answer(maze)
#print d
#
#matrix = [[0,1,0,0,0,1],
#     [4,0,0,3,2,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0]]
#
#d2 = answer(matrix)
#print d2