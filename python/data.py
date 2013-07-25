#!/usr/bin/env python2

def extract_winner(json_data):
    return json_data["winner"]

def extract_own_id(json_data):
    return json_data["player_id"]

def extract_my_planets(json_data, own_id):
    my_planets = [ planet for planet in json_data["planets"] \
        if planet["owner_id"] == own_id ]

    return my_planets

def extract_enemy_planets(json_data, own_id):
    enemy_planets = [ planet for planet in json_data["planets"] \
        if planet["owner_id"] != own_id and \
        planet["owner_id"] != 0 ]

    return enemy_planets

def extract_my_planet_ids(json_data, own_id):
    my_planets = [ (planet["id"]) for planet in json_data["planets"] \
        if planet["owner_id"] == own_id ]

    return my_planets

def extract_enemy_planet_ids(json_data, own_id):
    enemy_planets = [ (planet["id"]) for planet in json_data["planets"] \
        for planet in json_data["planets"] \
        if planet["owner_id"] == own_id ]

    return enemy_planets

def extract_my_planets_sorted_by_ships(json_data, own_id):
    my_planets_sorted = [(sum(planet["ships"]), planet) \
        for planet in json_data["planets"] \
        if planet["owner_id"] == own_id ]

    my_planets_sorted.sort(reverse=True)

    return my_planets_sorted

def extract_enemy_planets_sorted_by_ships(json_data, own_id):
    enemy_planets_sorted = [(sum(planet["ships"]), planet) \
        for planet in json_data["planets"] \
        if planet["owner_id"] != own_id \
        and planet["owner_id"] != 0 ]

    enemy_planets_sorted.sort(reverse=True)

    return enemy_planets_sorted

def return_ship_value(planet):
    ship_value = []

    type_a = [planet["production"][0], planet["ships"][0]]
    type_a.sort()

    type_b = [planet["production"][1], planet["ships"][1]]
    type_b.sort()

    type_c = [planet["production"][2], planet["ships"][2]]
    type_c.sort()

    ship_value.append(type_a)
    ship_value.append(type_b)
    ship_value.append(type_c)

    return ship_value
