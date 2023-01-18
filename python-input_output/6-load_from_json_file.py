#!/usr/bin/python3
"""here module is commited"""
import json


def load_from_json_file(filename):
    '''this is load-from-json-file'''
    with open(filename, 'r') as fp:
        return json.load(fp)
