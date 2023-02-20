import json
import spacy
from spacy.matcher import Matcher
from collections import Counter, defaultdict
from pprint import pprint


nlp = spacy.load("tr_core_news_trf")


matcher = Matcher(nlp.vocab)
pattern = [{"LIKE_NUM": True}, {"LEMMA": "gün"}]
matcher.add("kacGun", [pattern])

all_yorumlar = [json.loads(line) for line in open("../corona_yorumlari-processed.jsonl", "r").read().split("\n")[:-1]]


adjs=[]
nouns=[]
verbs=[]

i=0


sayilar = {
  "bir": "1",
  "iki": "2",
  "üç" : "3",
  "dört": "4",
  "beş": "5",
  "altı": "6",
  "yedi": "7",
  "sekiz": "8",
  "dokuz": "9",
  "on": "10",
  "yirmi": "20",
  "birinci": "1",
  "ikinci": "2",
  "üçüncü": "3",
  "dördüncü": "4",
  "beşinci": "5",
  "altıncı": "6",
  "yedinci": "7",
  "sekizinci": "8",
  "dokuzuncu": "9",
  "onuncu": "10",
  "yirminci": "20"
  }

ent_counter = defaultdict(list)

all_nums = []


for yorum in all_yorumlar:
    doc = nlp(yorum)
    matches = matcher(doc)
    match_texts = [doc[start:end].text for (match_id, start, end) in matches]
    match_nums = [mtext.split()[0] for mtext in match_texts]
    match_nums = [sayilar.get(mtext, mtext) for mtext in match_nums]
    match_nums  = [mtext.rstrip(".") for mtext in match_nums]
    try:
      match_nums.sort(key=int)
      if match_nums: print(match_nums)
      all_nums.append(match_nums[-1])
    except:
      pass


print(Counter(all_nums))


