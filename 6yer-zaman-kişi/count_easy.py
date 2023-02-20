import json
import spacy
from collections import Counter, defaultdict
from pprint import pprint


nlp = spacy.load("tr_core_news_trf")

all_yorumlar = [json.loads(line) for line in open("../corona_yorumlari-processed.jsonl", "r").read().split("\n")[:-1]]


verb_suffixes = []

for yorum in all_yorumlar:
    doc = nlp(yorum)
    verb = [(token.lemma_, token.text, token.morph) for token in doc if token.pos_ == "VERB"]
    morphs = [str(token.morph).split("|") for token in doc]
    flat_m = [item for sublist in morphs for item in sublist]
    verb_suffixes += flat_m


pprint(Counter(verb_suffixes))
