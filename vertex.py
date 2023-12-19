# Author: Christian
# Date: 11/12/2022
# Purpose: Vertex class

from cs1lib import *


class Vertex:
    def __init__(self, name, x_coordinate, y_coordinate):
        self.name = name
        self.x_coordinate = int(x_coordinate)
        self.y_coordinate = int(y_coordinate)
        self.adjacent_list = []
        self.radius = 8
        self.width = 3

    # returns a string of adjacent vertices
    def adjacent_list_string(self):
        aj = ""
        for i in range(len(self.adjacent_list)):
            if i != len(self.adjacent_list) - 1:
                aj += " " + self.adjacent_list[i].name + ","
            else:
                aj += " " + self.adjacent_list[i].name

        return aj

    # draws vertices
    def draw_vertex(self, r, g, b):
        x, y = self.x_coordinate, self.y_coordinate
        set_fill_color(r, g, b)
        draw_circle(x, y, self.radius)

    # draws edges between two vertices
    def draw_edge(self, other_vertex, r, g, b):
        set_font_size(15)
        set_stroke_width(self.width)
        set_stroke_color(r, g, b)
        x1, y1 = other_vertex.x_coordinate, other_vertex.y_coordinate
        x, y = self.x_coordinate, self.y_coordinate
        draw_line(x1, y1, x, y)

    # checks if start coordinates are in range.
    def in_range_start(self, x1, y1):
        start = False
        if self.x_coordinate - self.radius <= x1 <= self.x_coordinate + self.radius:
            if self.y_coordinate - self.radius <= y1 <= self.y_coordinate + self.radius:
                self.draw_vertex(1, 0, 0)
                start = True
        return start

    # checks if goal coordinates are in range.
    def in_range_goal(self, x2, y2):
        goal = False
        if self.x_coordinate - self.radius <= x2 <= self.x_coordinate + self.radius:
            if self.y_coordinate - self.radius <= y2 <= self.y_coordinate + self.radius:
                self.draw_vertex(1, 0, 0)
                goal = True

        return goal

    def __str__(self):
        return self.name + ";" + " Location: " + str(self.x_coordinate) + ", " + str(self.y_coordinate) + "; " + \
               "Adjacent vertices:" + str(self.adjacent_list_string())
