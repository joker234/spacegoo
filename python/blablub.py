#!/usr/bin/env python2

from sys import argv, exit
import distance
import network
import config
import random
import args
import data
import json

def main(config, s):
    s.connect((config["ip"], config["port"]))
    io = s.makefile('rw')
    network.write('login %s %s' % (config["user"], config["password"]), io)

    planet_distance = ""

    while True:
        json_data = network.get_data(io)

        if json_data:
            if data.extract_winner(json_data):
                exit(0)

            if not planet_distance:
                planet_distance = distance.create_planets_dict(json_data, 4, False)

            own_id = data.extract_own_id(json_data)
            my_planets = data.extract_my_planets(json_data, own_id)
            enemy_planets = data.extract_enemy_planets(json_data, own_id)

            my_planet_id = data.extract_my_planet_ids(json_data, own_id)

            if not my_planets:
                network.write(("nop"), io)
            elif not enemy_planets:
                network.write(("nop"), io)
            else:
                planet = random.choice(my_planets)
                targets = planet_distance[planet["id"]]

                ship_values = data.return_ship_value(planet)

                for i in xrange(len(targets)):
                    if targets[i][1] not in my_planet_id:
                        target = targets[i][1]
                        break

                network.write("send %s %s %s %s %s" % (planet["id"],
                    target,
                    random.randint(ship_values[0][0], ship_values[0][1]),
                    random.randint(ship_values[1][0], ship_values[1][1]),
                    random.randint(ship_values[2][0], ship_values[2][1])), io)

if __name__ == "__main__":
    file_name = args.receive_argument(argv)
    config = config.parse_and_return_config(file_name)

    config["user"] = "foooooo"
    config["password"] = "weepgeydgoc5"

    s = network.establish_connection(config)

    main(config, s)
