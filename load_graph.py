# Author: Christian
# Date: 11/12/2022
# Purpose: Graph-loading function

from vertex import Vertex


# function that adds references to the adjacent list of every location in the filename
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


# function that returns a dictionary of location names and their vertex objects.
def load_graph(filename):
    dictionary = {}

    open_file = open(filename, "r")

    for line in open_file:
        sections = line.split(";")
        vertex_name = sections[0].strip()

        coordinates = sections[2].strip().split(",")

        vertex = Vertex(vertex_name, coordinates[0], coordinates[1])

        dictionary[vertex_name] = vertex

    open_file.close()
    adjacency_list(filename, dictionary)

    return dictionary


load_graph("dartmouth_graph.txt")
