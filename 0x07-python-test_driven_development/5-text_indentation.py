#!/usr/bin/python3
"""This module prints a sample test"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these
    characters: .,?,:

    Args:
        text (str): The text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = []
    sentence = ""

    for char in text:
        if char in ['.', '?', ':']:
            sentence += char
            sentences.append(sentence.strip())
            sentence = ""
        else:
            sentence += char
    if sentence:
        sentences.append(sentence.strip())

    indented_text = "\n\n".join(sentences)
    print(indented_text, end="")
