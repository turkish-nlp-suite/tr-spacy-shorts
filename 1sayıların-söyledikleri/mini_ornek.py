import json
import spacy
from collections import Counter, OrderedDict


nlp = spacy.load("tr_core_news_trf")


cumle= "Ben de yarın Ankara'ya gidiyorum."

doc = nlp(cumle)

for token in doc:
    print(token, token.pos_, token.lemma_)


