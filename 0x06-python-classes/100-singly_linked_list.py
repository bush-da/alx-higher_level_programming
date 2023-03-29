#!/usr/bin/python3
"""Defines classes for a singly linked list"""


class Node:
    """Defines a node for linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a node

        args:
            data: data of a node
            next_node: link to next node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/setter for node data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/Setter for next node in linked list"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list class"""

    def __init__(self):
        """Initilize singly likend list"""
        self.__head = None

    def sorted_insert(self, value):
        """sort signly linked list

        args:
            value(int): data of a node

        """

        new_node = Node(value)
        if (self.__head is None):
            self.__head = new_node
            new_node.next_node = None
        elif self.__head.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            n = self.__head
            while (n.next_node is not None
                   and n.next_node.data < new_node.data):
                n = n.next_node
            new_node.next_node = n.next_node
            n.next_node = new_node

    def __str__(self):
        """funtion to output linked list data when instance of class called"""
        ret = []
        temp = self.__head
        while (temp is not None):
            ret.append(str(temp.data))
            temp = temp.next_node

        return ('\n'.join(ret))
