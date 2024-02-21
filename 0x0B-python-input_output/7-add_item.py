#!/usr/bin/python3
"""This module adds all arguments to a Python list and save them to a file."""

import sys
from json import dump, load

if __name__ == "__main__":
    filename = "add_item.json"
    try:
        with open(filename, "r") as file:
            items = load(file)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    with open(filename, "w") as file:
        dump(items, file)

