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

def find_head(doc, pos):
  polarity = None

  path = []
  stops = ["yok", "var", "değil", "geri", "yoktu", "vardı", "eksik", "gitti", "gitmedi", "geldi", "yaşadım", "yaşamadım", "yerinde"]
  head_token = doc[pos]

  while head_token.text == "alma" or ( (head_token.text not in stops) and head_token.pos_ != "VERB" and head_token.dep_ != "ROOT"):
    head_token = head_token.head
    path.append(head_token)
  return head_token, path

def eval(path):
  polarity=None

  verb = path[-1]
  verb_lemma = verb.lemma_
  verb_morph = verb.morph

  neg_verbs = ["yok", "eksik", "değil"]
  pos_verbs = ["var", "yerinde", "geri", "devam"]

  neg_verbs2 = ["git", "yitirme", "bit", "sıfırlan", "kaybet", "kaybol", "ol", "yaşa"]
  pos_verbs2 = ["gel", "şiddetlen", "başlama",  "düzeldi", "ilerle", "bit", "geç", "al"]

  if verb.text in neg_verbs or verb_lemma in neg_verbs2:
    polarity = "neg"
  elif verb.text in pos_verbs or verb_lemma in pos_verbs2:
    polarity = "pos"
  
  if "Polarity=Neg" in verb.morph:
    if polarity:
      polarity = "pos" if polarity == "neg" else "neg"
    else:
      polarity = "neg"
  '''
  elif "Mood=Pot" in verb.morph:
      if not polarity:
          polarity = "pos"
  '''

  all_lemmas = [token.lemma_ for token in path]

  if "kayb" in all_lemmas:
    if polarity:
      polarity = "pos" if polarity == "neg" else "neg"
    else:
      pass

  return polarity

pozitifler =0

aa = ["neyse, hic atesim çıkmadı, öksürmedim, hic tat koku kaybı yaşamadım"]

for yorum in all_yorumlar:
    doc = nlp(yorum)
    sents = doc.sents
    for sent in sents:
      tokens = [token.text for token in sent] 
      if "koku" in tokens:
         index = tokens.index("koku")
         headt, path = find_head(sent, index)
         polarity = eval(path)
         if polarity == "pos":
           pozitifler +=1
           print(polarity, "//", path, "//", sent)

    print("-----------------")




print(pozitifler)
