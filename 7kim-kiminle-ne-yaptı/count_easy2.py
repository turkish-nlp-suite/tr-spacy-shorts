import json
import spacy
from collections import Counter, defaultdict
from pprint import pprint


nlp = spacy.load("tr_core_news_trf")

all_yorumlar = [json.loads(line) for line in open("../corona_yorumlari-processed.jsonl", "r").read().split("\n")[:-1]]


verb_suffixes = defaultdict(list)

i=0


verb_objs = defaultdict(list)
verb_subjs = defaultdict(list)
verb_advs = defaultdict(list)

somev = ["gel", 'başla', 'git', 'çık', 'azal', 'art', 'bit', 'düş', 'düzel', 'yüksel', 'tüket', 'in', 'bulaş', 'ağrı', 'ilerle', 'şiş', 'kaybet']

for yorum in all_yorumlar:
    doc = nlp(yorum)
    verbs = [token for token in doc if token.pos_ == "VERB" and token.lemma_ in somev]
    if verbs: # obl, nsubj, obj
      for verb in verbs:
        objs, subjs, advs=[], [], []
        for token in doc:
          if token.dep_ == "nsubj" and token.head == verb:
              toks = [tok.text for tok in token.lefts]
              subjs.append(" ".join(toks + [token.text]))
          elif token.dep_ == "obj" and token.head == verb:
              toks = [tok.text for tok in token.lefts]
              objs.append(" ".join(toks+[token.text]))
          elif token.dep_ == "advmod" and token.head == verb:
              advs.append(token)

      if objs or subjs or advs:
          print(subjs, objs, advs, verb)
          verb_objs[verb.lemma_] += objs
          verb_subjs[verb.lemma_] += subjs
          verb_advs[verb.lemma_] += advs

print("--------------------")
pprint(verb_objs)
print("--------------------")
pprint(verb_subjs)
print("--------------------")
pprint(verb_advs)



