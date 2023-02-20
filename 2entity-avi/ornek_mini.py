import json
import spacy
from collections import Counter, OrderedDict


nlp = spacy.load("tr_core_news_trf")


cumle= "Burcu ve ben yarın Ankara'ya gidiyoruz."

doc = nlp(cumle)


print(doc.ents)

print(type(doc.ents[0]))

print(doc.ents[0].label_)

print([(ent.text, ent.label_) for ent in doc.ents])


