#!/usr/bin/python3
"""This module is contains an implementation of a singly linked list."""
class Node:
    """This class contains the necessary structure of a node."""
    def __init__(self, data, next_node=None):
        """init method.

        Args:
            data (int): the data of the node
            next_node (obj): node of type Node
        """
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")
        if isinstance(next_node, Node) or next_node==None:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """The data getter.

        Returns (int): the value of data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """The setter method for data.
        Args:
            value (int): The value that the attribute data should contain
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Getter method to obtain the next node of the list.

        Returns (obj): The next node of the list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        """The next_node setter method.

        Args:
            node (obj): The node to be inserted as the next value
        """
        if isinstance(node, Node) or node == None:
            self.__next_node = node
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """This class defines a structure of a singly linked list."""

    def __init__(self):
        """This is the init method for this class"""
        self.__head = None
    
    def sorted_insert(self, value):
        """This method inserts a new node to the linked list(sorted).
        
        Args:
            value (int): the value of the new node to be inserted into the list"""
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
        
    def __str__(self):
        """This defines a string representation of the list.
        
        Returns:
            str (str): The string representation of the object"""
        string = ""
        current = self.__head
        while current is not None:
            string += str(current.data) + "\n"
            current = current.next_node
        
        return string


