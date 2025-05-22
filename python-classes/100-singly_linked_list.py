#!/usr/bin/python3
"""
define la clase Node
"""


class Node():
    """
    clase Nodo, esta clase representa un nodo
    dentro de una lista enlazada simple
    """
    def __init__(self, data, next_node=None):
        """
        define cada instancia
        Args:
            data: numero que contiene el nodo
            next_node(int, opcional): el enlaze con el siguiente nodo
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node
    
    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList():
    """
    esta clase representa la lista enlazada simple 
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        node = Node(value)
        if self.__head == None:
            self.__head = node
        else:
            tmp = self.__head
            prev = None
            if tmp.data > node.data:
                node.next_node = tmp
                self.__head = node 
            else:
                while tmp is not None and node.data > tmp.data:
                    prev = tmp
                    tmp = tmp.next_node
                prev.next_node = node
                node.next_node = tmp

    def __str__(self):
        cabeza = self.__head
        linkedlist = ""
        while cabeza. next_node != None:
            linkedlist += (str(cabeza.data) + "\n")
            cabeza = cabeza.next_node
        linkedlist += str(cabeza.data)
        return linkedlist
