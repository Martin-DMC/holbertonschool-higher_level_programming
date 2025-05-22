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
        """inicializa una nueva instancia"""
        self.__head = None

    def sorted_insert(self, value):
        """inserta un nuevo nodo siempre en pos ascendente
        arg:
            value: data del nodo
        """
        node = Node(value)
        if self.__head is None or node.data <= self.__head.data:
            node.next_node = self.__head
            self.__head = node
            return

        tmp = self.__head
        while tmp.next_node is not None and tmp.next_node.data < node.data:
            tmp = tmp.next_node
        node.next_node = tmp.next_node
        tmp.next_node = node

    def __str__(self):
        cabeza = self.__head
        linkedlist = ""
        if cabeza is None:
            return linkedlist
        while cabeza. next_node is not None:
            linkedlist += (str(cabeza.data) + "\n")
            cabeza = cabeza.next_node
        linkedlist += str(cabeza.data)
        return linkedlist
