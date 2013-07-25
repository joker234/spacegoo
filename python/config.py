#!/usr/bin/env python2

from json import loads

def parse_and_return_config(file_name):
    data = []

    with open (file_name, "r") as f:
        data = loads(f.read())

    return data
