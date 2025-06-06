#!/usr/bin/python3
"""
this module define the CustomObject() class.
this class contain 3 method"""
import pickle


class CustomObject():
    """
    this class make a objects, serialize, deserialize and show
    all attributes
    """
    def __init__(self, name, age, is_student):
        """
        instance initialization
        """
        if not isinstance(name, str):
            try:
                name = str(name)
            except ValueError:
                raise ValueError(" :value error: ")
        if not isinstance(age, int):
            try:
                age = int(age)
            except ValueError:
                raise ValueError(" :value error: ")
        if not isinstance(is_student, bool):
            try:
                is_student = bool(is_student)
            except ValueError:
                raise ValueError(" :value error: ")
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        this method show all attibutes of this instance
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        this method serialize this object to binary code
        args:
            filename = new name for the serialized file
        """
        with open(filename, "wb") as archivo:
            pickle.dump(self, archivo)

    @classmethod
    def deserialize(cls, filename):
        """
        this method deserialize binary files
        args:
            filename = name of file to deserialize
        returns:
            the data of object or None if occurs a exception
        """
        try:
            with open(filename, "rb") as archivo:
                return pickle.load(archivo)
        except FileNotFoundError:
            return None
        except pickle.UnpicklingError:
            return None
