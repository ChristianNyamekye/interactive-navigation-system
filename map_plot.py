# Author: Christian
# Date: 11/12/2022
# Purpose: Drawing code for Dartmouth pathfinder

from cs1lib import *
from load_graph import load_graph
from bfs import bfs

WINDOW_X = 1012
WINDOW_Y = 811
RADIUS = 8
start_x, start_y = 0, 0
goal_x, goal_y = 0, 0
start, goal = None, None

graph_vertices = load_graph("dartmouth_graph.txt")
img = load_image("dartmouth_map.png")


#  mouse press function
def pressed(mx, my):
    global start_x, start_y
    start_x = mx
    start_y = my


#  mouse move function
def move(mx, my):
    global goal_x, goal_y
    goal_x = mx  # assigns the current x coordinate of the mouse to goal_x
    goal_y = my  # assigns the current y coordinate of the mouse to goal_y


def draw_vertices(graph):
    for key in graph:
        graph[key].draw_vertex(0, 0, 1)  # draws vertices with method from vertex class in r, g, b color config

        for location in graph[key].adjacent_list:
            graph[key].draw_edge(location, 0, 0, 1)  # draws vertices with method from vertex class in r, g, b config


def mouse_movement():
    global start, goal
    for key in graph_vertices:

        if graph_vertices[key].in_range_start(start_x, start_y):  # checks if mouse press is in range of vertex.
            graph_vertices[key].draw_vertex(1, 0, 0)  # draws start vertex
            start = graph_vertices[key]  # assigns start vertex for bfs

        if graph_vertices[key].in_range_goal(goal_x, goal_y):  # checks if mouse move is in range of vertex.
            graph_vertices[key].draw_vertex(1, 0, 0)  # draws vertex
            goal = graph_vertices[key]  # assigns goal vertex for bfs


# function for route
def route(start, goal):
    if start != None and goal != None:
        path = bfs(start, goal)  # path gets list from bfs

        for i in range(len(path) - 1):
            path[i].draw_vertex(1, 0, 0)  # draws vertex
            path[i].draw_edge(path[i + 1], 1, 0, 0)  # draws edge


# main draw function
def main():
    draw_image(img, 0, 0)
    draw_vertices(graph_vertices)
    mouse_movement()
    route(start, goal)


start_graphics(main, width=WINDOW_X, height=WINDOW_Y, mouse_press=pressed, mouse_move=move, title="Dartmouth Map")
