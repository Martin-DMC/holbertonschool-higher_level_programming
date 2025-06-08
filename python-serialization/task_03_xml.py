#!/usr/bin/python3
"""
this module contains two functions for
serializing and deserializing data in XML format
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    this function serializes a python dictionary to XML file
    args:
        dictionary: dictionary to be serialized
        filename: name of the future file
    """
    new_element = ET.Element('data')
    for key, value in dictionary.items():
        child_element = ET.SubElement(new_element, key)
        child_element.text = str(value)
    arbol = ET.ElementTree(new_element)
    arbol.write(filename)


def deserialize_from_xml(filename):
    """
    this function deserializes an XML file to python dict
    arg:
        filename: name of XML file
    returns:
        the dict deserialized or None for the exceptions
    """
    diccionary = {}
    try:
        arbol = ET.parse(filename)
        raiz = arbol.getroot()
        for child in raiz:
            key = child.tag
            value = child.text
            diccionary[key] = value
    except FileNotFoundError:
        return None
    except ET.ParseError:
        return None
    return diccionary
