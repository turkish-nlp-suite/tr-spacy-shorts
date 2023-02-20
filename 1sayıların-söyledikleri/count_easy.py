import json
import spacy
from collections import Counter, OrderedDict


nlp = spacy.load("tr_core_news_trf")

all_yorumlar = [json.loads(line) for line in open("corona_yorumlari-processed.jsonl", "r").read().split("\n")[:-1]]


adjs=[]
nouns=[]
verbs=[]

i=0

for yorum in all_yorumlar:
    doc = nlp(yorum)
    adj = [token.text for token in doc if token.pos_ == "ADJ"]
    verb = [token.text for token in doc if token.pos_ == "VERB"]
    noun = [token.text for token in doc if token.pos_ == "NOUN"]
    adjs += adj
    verbs += verb
    nouns += noun
    print(adj)
    print(i)
    i = i+1

for yorum in all_yorumlar:
    doc = nlp(yorum)
    adj = [token.lemma_ for token in doc if token.pos_ == "ADJ"]
    verb = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    noun = [token.lemma_ for token in doc if token.pos_ == "NOUN"]
    adjs += adj
    verbs += verb
    nouns += noun
    print(i)
    i = i+1

adjs= Counter(adjs)

verbs= Counter(verbs)

nouns= Counter(nouns)



print(adjs)
print("----------------------------")
print(verbs)
print("----------------------------")
print(nouns)
print("----------------------------")



