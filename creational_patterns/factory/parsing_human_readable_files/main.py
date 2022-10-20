import json
import xml.etree.ElementTree as etree


class JSONDataExtractor:
    """ Extracts and parses data from *.json files """

    def __init__(self,filepath):
        self.data = dict()
        with openfile(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XMLDataExtractor:
    """ Extracts and parses data from *.xml files """

    def __init__(self,filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree

