#!/usr/bin/python3
"""
this module define a class Student() but mejorate.
this class need a 3 arguments(first_name, last_name, age)
"""


class Student():
    """
    this class initializes the argument first_name, last_name and age
    also she've a public method to_json() with two road and other
    public method, reload_from_json()
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

    def reload_from_json(self, json):
        """
        this method that replace all attributes of the Student instance.
        the dict key will be the public attribute name and the dict value
        also will be the value of the public attribute
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
