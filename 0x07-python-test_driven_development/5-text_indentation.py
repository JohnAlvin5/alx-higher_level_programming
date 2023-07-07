#!/usr/bin/python3
"""Prints a text with 2 new lines after each given characters."""


def text_indentation(text):
    """Print text with two new lines after each character '.', '?', ':'.

    Args:
        text : The text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
