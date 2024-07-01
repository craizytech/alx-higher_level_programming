#!/usr/bin/python3
"""This a linked list data structure"""

class Node:
    """This class represents the structure of the node"""

    def __init__(self, data, next_node=None):
        """This is the constructor method"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This is the data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Data setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Next node getter."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if not (isinstance(value, Node) or value is None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """This data structure defines a single linked list"""
    
    def __init__(self):
        """constructor"""
        self.__head = None

    def __str__(self):
        current = self.__head
        nodes = []

        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """This method inserts the value inside the linked list"""

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
