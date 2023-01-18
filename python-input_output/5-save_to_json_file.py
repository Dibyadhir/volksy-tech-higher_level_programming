#!/usr/bin/python3
"""here module is commited"""
import json


def save_to_json_file(my_obj, filename):
    '''this is save to json file'''
    with open(filename, 'w') as fp:
        json.dump(my_obj, fp)
