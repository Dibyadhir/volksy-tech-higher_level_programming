#!/usr/bin/python3
"""here module is documented"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        values = load_from_json_file('add_item.json')
    except FileNotFoundError:
        values = []
    for i in sys.argv[1:]:
        values.append(i)
    save_to_json_file(values, 'add_item.json')
