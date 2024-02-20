#!/usr/bin/python3

"""Defines functions for reading from and writing to text files."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    
    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

