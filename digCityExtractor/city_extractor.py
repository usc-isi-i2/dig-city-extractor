# -*- coding: utf-8 -*-
import copy 
import types
from digDictionaryExtractor.populate_trie import populate_trie
from digExtractor.extractor import Extractor
import city_helper

class CityExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = ['text']
        self.cities = []
        self.stop_words = []

    def get_cities(self):
        return self.cities

    def set_cities(self, cities):
        if not isinstance(cities, list):
            raise ValueError("cities must be a list")
        self.cities = populate_trie(iter(cities))
        return self

    def get_stop_words(self):
        return self.stop_words

    def set_stop_words(self, stop_words):
        if not isinstance(stop_words, list):
            raise ValueError("stop_words must be a list")
        self.stop_words = populate_trie(iter(stop_words))
        return self
        
    def extract(self, doc):
        if 'text' in doc:
            return city_helper.extract(doc['text'], self.cities, self.stop_words)
        return None

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields