# Author: Christian
# Date: 11/12/2022
# Purpose: Drawing code for Dartmouth pathfinder

from cs1lib import *
from load_graph import load_graph
from bfs import bfs, bcs

r, g, b = 0, 1, 0
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
        graph[key].draw_vertex(0, 0, 1)

        for location in graph[key].adjacent_list:
            graph[key].draw_edge(location, 0, 0, 1)


def mouse_movement():
    global start, goal, r, g, b
    for key in graph_vertices:
        if graph_vertices[key].x_coordinate - 10 <= start_x <= graph_vertices[key].x_coordinate + 10:
            if graph_vertices[key].y_coordinate - 10 <= start_y <= graph_vertices[key].y_coordinate + 10:
                graph_vertices[key].draw_vertex(1, 0, 0)
                graph_vertices[key].draw_name(0, 0, 0.5)
                start = graph_vertices[key]

        if graph_vertices[key].x_coordinate - 10 <= goal_x <= graph_vertices[key].x_coordinate + 10:
            if graph_vertices[key].y_coordinate - 10 <= goal_y <= graph_vertices[key].y_coordinate + 10:
                graph_vertices[key].draw_vertex(0, 1, 0)
                graph_vertices[key].draw_name(0, 0, 0.5)
                goal = graph_vertices[key]


def route(start, goal):
    set_stroke_width(6)
    if start != None and goal != None:
        path = bfs(start, goal)

        for i in range(len(path) - 1):
            path[i].draw_vertex(path[i].r, path[i].g, path[i].b)
            path[i].draw_edge(path[i + 1], 0, 1, 1)


def route2(start, goal):
    set_stroke_width(6)
    if start != None and goal != None:
        path = bcs(start, goal)

        for i in range(len(path) - 1):
            path[i].draw_vertex(path[i].r, path[i].g, path[i].b)
            path[i].draw_edge(path[i + 1], 0, 1, 1)


def main():
    draw_image(img, 0, 0)
    draw_vertices(graph_vertices)
    mouse_movement()
    route2(start, goal)


start_graphics(main, width=WINDOW_X, height=WINDOW_Y, mouse_press=pressed, mouse_move=move)
