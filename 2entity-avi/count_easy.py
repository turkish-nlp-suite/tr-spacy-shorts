import json
import spacy
from collections import Counter, defaultdict
from pprint import pprint


nlp = spacy.load("tr_core_news_trf")

all_yorumlar = [json.loads(line) for line in open("../corona_yorumlari-processed.jsonl", "r").read().split("\n")[:-1]]


i=0


ent_counter = defaultdict(list)

for yorum in all_yorumlar:
    doc = nlp(yorum)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    for text,label in ents:
      ent_counter[label].append(text)
    i = i+1
    print(i)

pprint(ent_counter)



