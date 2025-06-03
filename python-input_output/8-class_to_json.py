#!/usr/bin/python3
"""
this module define that function class_to_json(obj).
this function can returns the dictionary description with simple data
structure for json serialization of an object
"""


def class_to_json(obj):
    """
    the function capture the object and she come in
    to the dict object for after returns the
    content
    """
    return obj.__dict__
