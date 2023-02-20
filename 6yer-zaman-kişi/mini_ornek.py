import json
import spacy
from collections import Counter, defaultdict
from pprint import pprint


nlp = spacy.load("tr_core_news_trf")


doc = nlp("Evde oturuyorum.")

print(doc[0].morph)

doc = nlp("Evime yeni boya yaptırdım")
print(doc[0].morph)

doc = nlp("Büyük ev kimin?")
print(list(doc.noun_chunks))
doc = nlp("Büyük evin sahibi kim?")
print(list(doc.noun_chunks))
doc = nlp("Büyük evdeki siyah kediyi bugün ben de sevdim.")
print(list(doc.noun_chunks))
doc = nlp("Tombul ve siyah kedi evden kaçmış.")
print(list(doc.noun_chunks))


