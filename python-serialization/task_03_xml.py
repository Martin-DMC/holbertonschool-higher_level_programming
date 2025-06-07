#!/usr/bin/python3
"""
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    new_element = ET.Element('data')
    for key, value in dictionary.items():
        new_element.set(str(key), str(value))
    arbol = ET.ElementTree(new_element)
    arbol.write(filename)

def deserialize_from_xml(filename):
    diccionary = {}
    arbol = ET.parse(filename)
    data = arbol.getroot()
    for sons in data:
        diccionary[sons.tag] = sons.text + sons.attrib
    return diccionary
