# Author: Christian
# Date: 11/12/2022
# Purpose: Breadth-first search algorithm

from collections import deque


# Breadth-First search function
def bfs(start, goal):
    backpointer_d = {}
    path = []
    frontier = deque()

    frontier.append(start)
    backpointer_d[start] = None

    while frontier != ():  # while frontier is not empty
        current_value = frontier.popleft()  # current value gets first value in frontier and removes value from it.
        for adjacent_value in current_value.adjacent_list:
            if adjacent_value not in backpointer_d:
                frontier.append(adjacent_value)
                backpointer_d[adjacent_value] = current_value
        if goal in backpointer_d:
            break

    pointer = goal
    while pointer != None:
        path.append(pointer)
        pointer = backpointer_d[pointer]

    return path
