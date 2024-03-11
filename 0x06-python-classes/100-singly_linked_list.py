#!/usr/bin/python3
"""This module contains the implementation of a singly linked list."""

class Node:
    """This class defines a structure of a node."""
    def __init__(self, data, next_node=None):
        """This is the init method for the Node."""
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """This is the getter method for data attribute."""
            return self.__data

        @data.setter
        def data(self, value):
            """This is a setter method for the data attribute."""
            if isinstance(value, int):
                self.__data = value
            else:
                raise TypeError("data must be an integer")

        @property
        def next_node(self):
            """Getter method for the current node."""
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            """This method is a setter method for the next_node."""
            if isinstance(next_node, Node) or next_node is None:
                self.__next_node = value
            else:
                raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """This class contains the implementation of a linked list."""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """This method inserts a value into a node sorted."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value <= self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """This method prints a string representation of the node."""
        current = self.head
        result = ""
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
