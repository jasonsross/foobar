# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 10:59:06 2017

@author: jasonros
"""

import itertools


def get_best(current, candidate):
    if len(candidate) > len(current):  # Better state
        return sorted(list(candidate))
    elif len(candidate) == len(candidate):  # Should check the individuals ids
        candidate = sorted(list(candidate))
        for i in range(len(current)):
            if current[i] < candidate[i]:  # We stop at the first id we found
                return current
            elif current[i] > candidate[i]:
                return candidate
    return current

def answer(times, time_limit):
    numpos = len(times)
    numbunnies = numpos-2
    assert numbunnies > 0

    shortestpath = [[None]*numpos for _ in xrange(numpos)]  # initialize array of nones size equal to times

    # first we find all possible paths of length <= len(times) with no repeat visits starting from all nodes
    paths = itertools.chain(*map(
        lambda path_length: itertools.permutations(range(numpos), path_length),
        range(2, numpos+1)
    ))
    
    # find shortest path between all nodes and store it into shortest path matrix
    for path in paths:
#        print path
        origin = path[0]
        destination = path[-1]

        # Compute the time to reach the destination
        cost = 0
        prev_pos = origin
        for pos in path:  # No need to keep track of the visited bunnies here (will be reconstructed at the end)
            cost += times[prev_pos][pos]
            prev_pos = pos

        # Is the cost better than previous path for this node->node move
        if shortestpath[origin][destination] == None or cost < shortestpath[origin][destination]:
            shortestpath[origin][destination] = cost

        # if we go back to origin do we gain time?
        cost += times[destination][origin]
        if cost < 0:  # If we gain some time, it means we could retake this loop indefinitelly to have infinite time => All bunnies saved !!!
            #print 'Loop detected'
            return range(numbunnies)

#     Debugging: show the grid of shortest paths
#    for l in shortestpath:
#         print l

    # Final path reconstruction. Starting with start -> end and see if we
    # can insert bunnies along this path
    # start -> bunny 4 -> bunny 2 -> end
    bunnies_saved = []
    paths = itertools.chain(*map(  # All bunnies combinations in all possibles orders
        lambda path_length: itertools.permutations(range(numbunnies), path_length),
        range(0, numbunnies+1)
    ))
    
    for path in paths:
        origin = 0
        destination = numpos-1 #bulkhead door

        # Compute the time to reach the destination
        time = time_limit
        prev_pos = origin
        for pos in path:
            time -= shortestpath[prev_pos][pos+1] # subtract time to get to current bunny (pos+1)
            prev_pos = pos+1  # new position is now at current bunny
        time -= shortestpath[prev_pos][destination] # subtract time to get to bulkhead

         # If we reached the destination in time, see if this bunny list is best so far
        if time >= 0:
            bunnies_saved = get_best(bunnies_saved, path)

    return bunnies_saved



grid1 = [
        [0,2,2,2,-1],
        [9,0,2,2,-1],
        [9,3,0,2,-1],
        [9,3,2,0,-1],
        [9,3,2,2,0]]

a =  answer(grid1, 1)  # [0, 1, 2]
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