import json
import spacy
from collections import Counter, defaultdict
from pprint import pprint


nlp = spacy.load("tr_core_news_trf")

all_yorumlar = [json.loads(line) for line in open("../corona_yorumlari-processed.jsonl", "r").read().split("\n")[:-1]]


verb_suffixes = defaultdict(list)

i=0


cases = ["Tense", "Person", "Voice", "Evident", "Aspect", "Mood"]

somev = ['ol', 'et', 'al',  'gel', 'başla', 'git', 'çık', 'yap', 'ver', 'geç', 'iç', 'var', 'uyan', 'hisset', 'kal', 'de', 'kullan', 'yaşa', 'yaptır', 'azal', 'yat', 'geçir', 'bil', 'düşün', 'gör', 'yan', 'söyle', 'öksür', 'dön', 'iste', 'art', 'bit', 'kalk', 'yaz', 'ara', 'uyu', 'göster', 'at', 'dur', 'gir', 'gerek', 'çalış', 'atlat', 'ye', 'sür', 'iyileş', 'bak', 'bırak', 'düş', 'terle', 'bacak', 'inan', 'bekle', 'ağr', 'düzel', 'çek', 'kork', 'öğren', 'aç', 'benze', 'yüksel', 'getir', 'ak', 'yorul', 'tüket', 'in', 'bulaş', 'ağrı', 'kes', 'iyiy', 'yara', 'rahatla', 'ekle', 'vur', 'ilerle', 'ed', 'dayan', 'atla', 'çıkar', 'anla', 'şiş', 'tut', 'oluş', 'uyuy', 'tıkan', 'iyi', 'hapşır', 'duy', 'kaybet', 'tıka', 'sık', 'kokla', 'gıcıkla', 'yıka', 'anlat']

for yorum in all_yorumlar:
    doc = nlp(yorum)
    verbs = [(token.lemma_, str(token.morph)) for token in doc if token.pos_ == "VERB" and token.lemma_ in somev]
    for verb_l, morph in verbs:
        morph_parts = morph.split("|")
        # Tense, Person, Voice, Evident, Aspect, Mood
        newd = {}
        for part in morph_parts:
            left, right = part.split("=")
            if left in cases:
                newd[left] = right
        verb_suffixes[verb_l].append(newd)


allvcounts={}

for verb, mlist in verb_suffixes.items():
  accd  = {}
  finald = {key:[] for key in cases}
  for sdict in mlist:  # [{'Tense': 'Pres', 'Voice': 'Pass'}, {'Tense': 'Past', 'Voice': 'Pass'}]
      for (skey,sval) in sdict.items():
          finald[skey].append(sval)
  for key, vals in finald.items():
      counter = Counter(vals)
      if counter:
        accd[key] = counter

  allvcounts[verb] = accd



pprint(allvcounts)
