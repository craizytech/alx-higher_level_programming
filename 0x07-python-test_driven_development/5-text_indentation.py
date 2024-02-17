#!/usr/bin/python3
"""This module defines a function that indents a string"""

def text_indentation(text):
    """This function takes in a string and indents it based
    on the characters '., ?, :' by adding two lines after each
    of the characters
    
    Args:
        text (str): The string to be indented"""

    if isinstance(text, str):
        text = text.strip()
        sentences = []
        sentence = ""
        for char in text:
            if char in ".?:":
                sentences.append(sentence + char)
                sentence = ""
            else:
                sentence += char
        
        if sentence:
            sentences.append(sentence)
        
        for sentence in sentences:
            print(sentence.strip())
            print()
    else:
        raise TypeError("text must be a string")