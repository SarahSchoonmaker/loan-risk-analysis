import spacy
from difflib import SequenceMatcher

nlp = spacy.load("en_core_web_sm")

def address_similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def is_address_suspect(addr1, addr2, threshold=0.75):
    return address_similarity(addr1, addr2) < threshold
