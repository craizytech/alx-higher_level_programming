#!/usr/bin/python3
"""This module contains 2 classes that implements a singly linked list."""

import pdb

class Node:
    """This class implements a node structure."""

    def __init__(self, data, next_node=None):
        """This is the node class constructor."""
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """This is the getter method for the data attribute."""
            return self.__data
        @data.setter
        def data(self, value):
            """This is the setter method for the data attribute."""
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """property getter method for the next_node attribute."""
            return self.__next_node
        @next_node.setter
        def next_node(self, value):
            """property setter method for the next_node attribute."""
            if not isinstance(value, None) or not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")
            self.__next_node = value

class SinglyLinkedList:
    """This class implements the linked list."""
    def __init__(self):
        """This is the constructor class of the Singly linked list."""
        self.__head = None
        
    def __str__(self):
        """This method prints an informal representation of list."""
        current = self.__head
        string = ""
        while current:
            string += str(current.data) + '\n'
            current = current.next_node
        return string

    def sorted_insert(self, value):
        new_node = Node(value)
        new_node.data = value

        # Case: Empty List
        if self.__head is None:
            self.__head =  new_node
            return
        # Case: Insert at the beginning
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        
        # Traverse the list to find the insertion point
        current = self.__head
        while current.next_node and current.next_node.data < value:
                current = current.next_node
                
        # Insert the new node
        new_node.next_node = current.next_node
        current.next_node = new_node