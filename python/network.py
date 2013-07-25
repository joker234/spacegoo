#!/usr/bin/env python2

from json import loads
import socket

def establish_connection(json_data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    return s

def write(data, io):
    io.write('%s\n' % (data,))
    io.flush()

def get_data(io):
    data = io.readline().strip()

    if not data:
        exit(1)
    elif data and data[0] == "{":
        return loads(data)
