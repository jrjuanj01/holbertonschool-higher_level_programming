#!/usr/bin/python3
"""Method for serialization and deserialization using XML instead of JSON"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary to an XML file."""

    root = ET.Element("root")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)
    ET.dump(root)


def deserialize_from_xml(filename):
    """Deserializes an XML file to a dictionary."""

    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        if child.tag == 'age':
            dictionary[child.tag] = int(child.text)
        elif child.tag == 'is_student':
            dictionary[child.tag] = child.text.lower() == 'true'
        else:
            dictionary[child.tag] = child.text

    return dictionary
