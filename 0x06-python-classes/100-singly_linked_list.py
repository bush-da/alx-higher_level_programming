#!/usr/bin/python3
"""Defines singly linked list"""

class Node:
    """Defines a node of a signly linked list"""

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
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):

        new_node = Node(value)
        if (self.__head is None):
            self.__head = new_node
            new_node.next_node = None
        elif self.__head.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            n = self.__head
            while (n.next_node is not None and n.next_node.data < new_node.data):
                n = n.next_node
            new_node.next_node = n.next_node
            n.next_node = new_node

    def __str__(self):
        ret = []
        temp = self.__head
        while (temp is not None):
            ret.append(str(temp.data))
            temp = temp.next_node

        return ('\n'.join(ret))
