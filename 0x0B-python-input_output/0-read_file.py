#!/usr/bin/python3

"""Defines functions for reading from and writing to text files."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
