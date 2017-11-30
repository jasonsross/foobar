# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 11:38:55 2017

@author: jasonros
"""

def answer(n):
    from collections import deque
    
    class Node:

        def __init__(self, value,down,up):
            self.value = value
            self.down = down
            self.up = up
    
        def __hash__(self):
            return self.value
    
        def __eq__(self, other):
            return self.value == other.value
    
        def get_neighbors(self):
            neighbors = []
            value = self.value
            up = self.up
            down = self.down
            
            if not (value % 2):
                neighbors.append(Node(value >> 1,1,1))
            else:
                if up:
                    neighbors.append(Node(value+1,0,1))
                if down:
                    neighbors.append(Node(value-1,1,0))
            
            return neighbors    
    if int(n) == 0:
        return 1
    if int(n) == 1:
        return 0
    source = Node(int(n),1,1)
    queue = deque([source])
    step_map = {source.value: 0}
    while queue:
        current_node = queue.popleft()
        for child_node in current_node.get_neighbors():
            if child_node.value not in step_map.keys():                        
                step_map[child_node.value] = step_map[current_node.value] + 1
                if child_node.value == 1:
                    return step_map[child_node.value]
                else:
                    queue.append(child_node)

print(answer("9"*309))

#python -m cProfile fuelinjection.py

#maze = [
#[0,1,1,0],
#[0,0,0,1],
#[1,1,0,0],
#[1,1,1,0]
#]
#print answer(maze)
#maze = [
#[0, 0, 0, 0, 0, 0], 
#[1, 1, 1, 1, 1, 0], 
#[0, 0, 0, 0, 0, 0], 
#[0, 1, 1, 1, 1, 1], 
#[0, 1, 1, 1, 1, 1], 
#[0, 0, 0, 0, 0, 0]
#]
#print answer(maze)
#maze = [
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
# [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
# [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
#
#print answer(maze)
#maze = [
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
# [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
# [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
#print answer(maze)