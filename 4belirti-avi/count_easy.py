import json
import spacy
from collections import Counter, defaultdict
from pprint import pprint


nlp = spacy.load("tr_core_news_trf")

all_yorumlar = [json.loads(line) for line in open("../corona_yorumlari-processed.jsonl", "r").read().split("\n")[:-1]]


adjs=[]
nouns=[]
verbs=[]

i=0


nchunks =[]

for yorum in all_yorumlar:
    doc = nlp(yorum)
    try:
      nc = list(doc.noun_chunks)
      nc = [chunk.text for chunk in nc if len(chunk) in [3,4]]
    except:
      nc = []
    if nc: print(nc)
    nchunks += nc

pprint(Counter(nchunks))



