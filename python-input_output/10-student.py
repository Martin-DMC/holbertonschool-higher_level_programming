#!/usr/bin/python3
"""
this module define a class Student() but mejorate.
this class need a 3 arguments(first_name, last_name, age)
"""


class Student():
    """
    this class initializes the argument first_name, last_name and age
    also she've a public method to_json(), this method now, have a two road.
    if atrrs is a list of strings:
        return only they atribbutes includes in the strings
    else:
        return all attributes of that instance
    """
    def __init__(self, first_name, last_name, age):
        """
        instance initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        this method returns a dictionary representation for JSON
        serialization.
        if attrs is None:
            return all attributes
        otherwise
            return only they attributes contained in the list attrs
        """
        if isinstance(attrs, list):
            new_dict = {}
            for name in attrs:
                if name in self.__dict__:
                    value = self.__dict__[name]
                    new_dict[name] = value
            return new_dict
        else:
            return self.__dict__
