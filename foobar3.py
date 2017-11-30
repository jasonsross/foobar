# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 22:20:53 2017

@author: jasonros
"""

def answer(total_lambs):
    # your code here
    # the generous method is a geometric series of factor 2
    if total_lambs >= 10 and total_lambs <= 10**9:
        gen = [1]
        ind = 1
        while True:        
            if sum(gen) > total_lambs:
                gen.pop()
                ind -= 1
                if (total_lambs - sum(gen)) >= (gen[ind-1]+gen[ind-2]):
                    gen.append(total_lambs-sum(gen))
                break
            else:
                gen.append(2**ind)
                ind += 1 
        print gen, sum(gen), total_lambs - sum(gen)        
        # the stingy method is the fibonocci sequence
        stingey = [1,1]
        ind = 2
        while True:
            stingey.append(stingey[ind-1]+stingey[ind-2])
            if sum(stingey) > total_lambs:
                stingey.pop()
                break
            ind += 1        
        print stingey, sum(stingey), total_lambs - sum(stingey)        
        return (len(stingey)-len(gen))
    else:
        return 0

#t = 10
#while True:
#    answer(t)
#    t+=1
        
print answer(33)

print answer(143)