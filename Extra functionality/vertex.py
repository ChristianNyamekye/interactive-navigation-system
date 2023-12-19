# Author: Christian
# Date: 11/12/2022
# Purpose: Vertex class

from cs1lib import *
from random import uniform


class Vertex:
    def __init__(self, name, x_coordinate, y_coordinate):
        self.name = name
        self.x_coordinate = int(x_coordinate)
        self.y_coordinate = int(y_coordinate)
        self.adjacent_list = []
        self.radius = 8
        self.width = 3
        self.r = uniform(0.5, 1)
        self.b = uniform(0.5, 1)
        self.g = uniform(0, 1)

    def adjacent_list_string(self):
        aj = ""
        for i in range(len(self.adjacent_list)):
            if i != len(self.adjacent_list) - 1:
                aj += " " + self.adjacent_list[i].name + ","
            else:
                aj += " " + self.adjacent_list[i].name

        return aj

    def draw_vertex(self, r=0, g=0, b=1):
        x, y = self.x_coordinate, self.y_coordinate
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)
        draw_circle(x, y, self.radius)

    def draw_name(self, r, g, b):
        x, y = self.x_coordinate, self.y_coordinate
        set_stroke_color(r, g, b)
        draw_text(self.name.upper(), x + 5, y - 5)

    def draw_edge(self, other_vertex, r, g, b):
        set_font_size(15)
        set_stroke_width(self.width)
        set_stroke_color(r, g, b)
        x1, y1 = other_vertex.x_coordinate, other_vertex.y_coordinate
        x, y = self.x_coordinate, self.y_coordinate
        draw_line(x1, y1, x, y)

    def in_range(self, start_x, start_y, goal_x, goal_y):
        a, b = False, False
        if self.x_coordinate - 10 <= start_x <= self.x_coordinate + 10:
            if self.y_coordinate - 10 <= start_y <= self.y_coordinate + 10:
                self.draw_vertex(1, 0, 0)
                a = True

        if self.x_coordinate - 10 <= goal_x <= self.x_coordinate + 10:
            if self.y_coordinate - 10 <= goal_y <= self.y_coordinate + 10:
                self.draw_vertex(1, 0, 0)
                b = True

        return a and b

    def __str__(self):
        return self.name + ";" + " Location: " + str(self.x_coordinate) + "," + str(self.y_coordinate) + "; " + \
               "Adjacent vertices:" + str(self.adjacent_list_string())
