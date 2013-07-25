#!/usr/bin/env python2

from math import sqrt

def get_dist(my_x, my_y, e_x, e_y):
    xdiff = my_x - e_x
    ydiff = my_y - e_y
    dist = sqrt(xdiff*xdiff + ydiff*ydiff)

    return dist

def create_planets_dict(json_data, num_neighbors, include):
    planet_distance = {}

    for candidate in json_data["planets"]:

        list_distances = []

        for planet in json_data["planets"]:
            if not include:
                if candidate["id"] != planet["id"]:
                    dist = get_dist(candidate["x"], candidate["y"], planet["x"], planet["y"])
                    list_distances.append((dist, planet["id"]))
            else:
                dist = get_dist(candidate["x"], candidate["y"], planet["x"], planet["y"])
                list_distances.append((dist, planet["id"]))


        list_distances.sort()
        list_distances = list_distances[0:num_neighbors]
        planet_distance[candidate["id"]] = list_distances

    return planet_distance

def return_near_target(targets, planet_ids):
    for i in xrange(len(targets)):
        if targets[i][1] not in planet_ids:
            target = targets[i][1]

            return target
