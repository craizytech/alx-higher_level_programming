#!/usr/bin/python3
"""This module implements a singly linked list"""

class Node:
    """This class defines a single node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        
        self.__data = value

    # next node
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class creates a singly linked list"""

    def __init__(self):
        """This is the constructor method"""
        self.__head = None

    def __repr__(self):
        """Prints the object representation"""
        nodes = []
        dummy_node = self.__head

        while dummy_node:
            nodes.append(str(dummy_node.data))
            dummy_node = dummy_node.next_node
        
        return "\n".join(nodes)
    
    def sorted_insert(self, value):
        """
        This method inserts a value into the correct position in the linked list
        """
        if not self.__head:
            new_node = Node(value)
            self.__head = new_node
            return
        
        if self.__head.data > value:
            new_node = Node(value)
            new_node.next_node = self.__head

            self.__head = new_node
            return

        current_node = self.__head
        prev_node = None

        while current_node and current_node.data < value:
            prev_node = current_node
            current_node = current_node.next_node

        new_node = Node(value)
        new_node.data = value
        new_node.next_node = current_node
        prev_node.next_node = new_node
