# -*- coding: utf-8 -*-
import json
import string
import pygtrie as trie
from digDictionaryExtractor.populate_trie import populate_trie
from digDictionaryExtractor.name_dictionary_extractor import get_name_dictionary_extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digCrfTokenizer.crf_tokenizer import CrfTokenizer

def tokenize(raw):
    t = CrfTokenizer()
    t.setRecognizeHtmlEntities(True)
    t.setRecognizeHtmlTags(True)
    t.setSkipHtmlTags(True)
    t.setRecognizePunctuation(True)
    tokens = t.tokenize(raw)
    return tokens

def extract(doc, cities, stop_words, input_fields='text', output_field='cities'):
    doc = {'text': tokenize(doc)}
    e = get_name_dictionary_extractor(cities).set_pre_filter(lambda x:x not in stop_words)
    e.set_ngrams(3)
    e.set_joiner(' ')
    ep = ExtractorProcessor().set_input_fields('text').set_output_field('cities').set_extractor(e)
    updated_doc = ep.extract(doc)

    try:
        cities_list = updated_doc['cities'][0]['value']
    except Exception:
        cities_list = []

    return cities_list
