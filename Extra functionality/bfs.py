# Author: Christian
# Date: 11/12/2022
# Purpose: Breadth-crumb search algorithm

from collections import deque


def bcs(start, goal):  # breadcrumb search
    backpointer_d = {}
    path = []
    frontier = deque()

    frontier.append(start)
    backpointer_d[start] = None

    while frontier != ():
        current_value = frontier.popleft()
        i, j = 0, len(current_value.adjacent_list) - 1
        while i < len(current_value.adjacent_list):
            frontier.append(current_value.adjacent_list[i])
            frontier.append(current_value.adjacent_list[j])

            if current_value.adjacent_list[i] not in backpointer_d:
                backpointer_d[current_value.adjacent_list[i]] = current_value

            if current_value.adjacent_list[j] not in backpointer_d:
                backpointer_d[current_value.adjacent_list[j]] = current_value

            i += 1
            j -= 1

        # if i > j:
        if goal in backpointer_d:
            break

    pointer = goal
    while pointer != None:
        path.append(pointer)
        pointer = backpointer_d[pointer]

    return path


def bfs(start, goal):
    backpointer_d = {}
    path = []
    frontier = deque()

    frontier.append(start)
    backpointer_d[start] = None

    while frontier != ():
        current_value = frontier.popleft()
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
