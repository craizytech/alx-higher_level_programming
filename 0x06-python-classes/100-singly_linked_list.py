#!/usr/bin/python3

class Node:
    """This class defines a structure of a node."""
    def __init__(self, data, next_node=None):
        """This is the init method for the Node."""
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if isinstance(next_node, (Node, None)):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

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
            if isinstance(next_node, (Node, None)):
                self.__next_node = next_node
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
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def __str__(self):
        """This method prints a string representation of the node."""
        pass

