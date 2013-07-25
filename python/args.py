#!/usr/bin/env python2

from sys import argv, exit
import config

def receive_argument(argument):
    if len(argument) == 1:
        exit(1)
    else:
        try:
            file_name = str(argument[1])
        except ValueError as e:
            print e
            exit(1)
        else:
            return file_name
