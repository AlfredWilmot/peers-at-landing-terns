import json
import xml.etree.ElementTree as etree


class JSONDataExtractor:
    """ Extracts and parses data from *.json files """

    def __init__(self,filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
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


def data_extraction_factory(filepath):
    """
    Factory method determines which extractor class to use
    by looking at the file extension
    """
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError(f'cannot extract data from {filepath}')
    return extractor(filepath)


def extract_data_from(filepath):
    """
    Exception-handling wrapper for the factory method.
    (this is to be used by client code)
    """
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)

    return factory_obj
