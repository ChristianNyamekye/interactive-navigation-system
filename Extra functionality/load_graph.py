# Author: Christian
# Date: 11/12/2022
# Purpose: Graph-loading function

from vertex import Vertex


def adjacency_list(filename, dictionary):
    open_file = open(filename, "r")

    for line in open_file:
        sections = line.split(";")
        vertex_name = sections[0].strip()
        adjacent_vertices = sections[1].strip().split(",")
        for location in adjacent_vertices:
            location = location.strip()

            if location in dictionary:
                dictionary[vertex_name].adjacent_list.append(dictionary[location])

    open_file.close()


def load_graph(filename):
    dictionary = {}

    open_file = open(filename, "r")

    for line in open_file:
        sections = line.split(";")
        vertex_name = sections[0].strip()

        coordinates = sections[2].strip().split(",")

        vertex = Vertex(vertex_name, coordinates[0], coordinates[1])

        dictionary[vertex_name] = vertex

    adjacency_list(filename, dictionary)

    return dictionary

    open_file.close()


load_graph("dartmouth_graph.txt")
