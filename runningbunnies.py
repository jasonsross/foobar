# -*- coding: utf-8 -*-
"""
Created on Mon Aug 07 15:16:49 2017

@author: jasonros
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 11:38:55 2017

@author: jasonros
"""


import itertools  
import heapq, math
def answer(times, time_limit):
#    from collections import deque  
    numpos = len(times)
    numbunnies = numpos-2
    assert numbunnies > 0
    nodes = range(numpos)
#    print (numpos-1)*math.factorial(numpos-1)
    def getShortestPath(start,end):        
        timeloop = False
        endtimes = []
        queue = [(0,start,[start])] # (cumulative time, node position, path)
        heapq.heapify(queue)
        while queue:
            time, current_node, node_path= heapq.heappop(queue) 
#            print time, current_node, node_path
#            raw_input()
            if current_node == end:
                if time + times[end][start] < 0:
                    return 'timeloop'
                else:
                    return time
#                    endtimes = endtimes + [time]
            else:            
                for child_node in nodes:
                    if child_node not in node_path:                        
                        new_path = node_path + [child_node]
                        newtime = time + times[current_node][child_node]
#                        print child_node, new_path, newtime                        
                        heapq.heappush(queue,(newtime,child_node,new_path))
        if timeloop:
            return 'timeloop'
        else:
            return min(endtimes)
    
#    return getShortestPath(0,4)

    def update_best(current, test):
        test = sorted(list(test))
        if len(test)>len(current):
            return test
        elif len(test)==len(current):
            for i in range(len(test)):
                if test[i]<current[i]:
                    return test
        return current
    
    bunnies_saved = []
    paths = itertools.chain(*map(  # All bunny combinations in all possibles orders
        lambda path_length: itertools.permutations(range(numbunnies), path_length),
        range(0, numbunnies+1)
    ))
    
    for path in paths:
        
        origin = 0
        destination = numpos-1 #bulkhead door

        # Compute the time to reach the destination
        time = time_limit
        prev_index = origin
        for pos in path:
            shortest = getShortestPath(prev_index,pos+1)
            if shortest == 'timeloop':
                print shortest
                return range(numbunnies)
            time -= shortest # subtract time to get to current bunny (pos+1)
            prev_index = pos+1  # new position is now at current bunny
        
        shortest = getShortestPath(prev_index,destination)
        if shortest == 'timeloop':
            print shortest
            return range(numbunnies)
        time -= shortest # subtract time to get to bulkhead
         # If we reached the destination in time, see if this bunny list is best so far
        if time >= 0:
            bunnies_saved = update_best(bunnies_saved, path)
    return bunnies_saved
    
#python -m cProfile fuelinjection.py

#times = [
#[0,1,1,1,1],
#[1,0,1,1,1],
#[1,1,0,1,1],
#[1,1,1,0,1],
#[1,1,1,1,0]]
#
#time_limit = 3
#print answer(times,time_limit)
#answer is [0,1]

times = [
[0,2,2,2,-1],
[9,0,2,2,-1],
[9,3,0,2,-1],
[9,3,2,0,-1],
[9,3,2,2,0]]
time_limit = 1
a = answer(times,time_limit)
print a

grid2 = [
    [0, 2, 2, 2, -1],
    [9, 0, 2, 2, -1],
    [9, 3, 0, 2, -1],
    [9, 3, 2, 0, -1],
    [9, 3, 2, 2, 0]
]
print answer(grid2, 1)  # [1, 2]

grid3 = [
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1]
]
print answer(grid3, 1)  # Infinite loop [0, 1, 2, 3, 4]

grid21 = [
    [0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0]
]
print answer(grid21, 1)  # Only exit possible []

grid23 = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 9, 9, 9, 9, 9],
    [1, 9, 0, 9, 9, 9, 9],
    [1, 9, 9, 0, 9, 9, 9],
    [1, 9, 9, 9, 0, 9, 9],
    [1, 9, 9, 9, 9, 0, 9],
    [1, 9, 9, 9, 9, 9, 0]
]
print answer(grid23, 3)  # Should go by the start case each time

grid4 = [
    [0, 1, 1, 1, 1, 99, 1],
    [1, 0, 1, 1, 1, 99, 1],
    [1, 1, 0, 1, 1, 99, 1],
    [1, 1, 1, 0, 1, 99, -3],
    [1, 1, 1, 1, 0, 99, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 99, 0]
]
print answer(grid4, 1)  # Should loop end->bunny2->end->... to gain enough time to reach bunny4 [0, 1, 2, 3, 4]

grid23 = [
    [0, 9, 1, 9, 9, 9, 9],
    [9, 0, 9, 9, 9, 9, 1],
    [9, 9, 0, 9, -1, 9, 9],
    [9, 9, 9, 0, 9, 9, 9],
    [9, 1, 9, 9, 0, 9, 9],
    [9, 9, 9, 9, 9, 0, 9],
    [9, 9, 9, 9, 9, 9, 0]
]
print answer(grid23, 3)  # Should loop end->bunny2->end->... to gain enough time to reach bunny4 [0, 1, 2, 3, 4]