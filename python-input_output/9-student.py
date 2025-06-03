#!/usr/bin/python3
"""
this module define a class Student().
this class need a 3 arguments(first_name, last_name, age)
"""


class Student():
    """
    this class initializes the argument first_name, last_name and age
    also she've a public method to_json(), this method make the
    convertion be instance of class to dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        instance initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        this method returns a dictionary representation for JSON serialization
        """
        return self.__dict__
