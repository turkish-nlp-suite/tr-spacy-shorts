import json
import spacy
from spacy.matcher import Matcher
from collections import Counter, defaultdict
from pprint import pprint


nlp = spacy.load("tr_core_news_trf")


matcher = Matcher(nlp.vocab)
pattern = [{"LIKE_NUM": True}, {"LEMMA": "gün"}]
matcher.add("kacGun", [pattern])

doc = nlp("3. günden sonra iyileştim.")
matches = matcher(doc)
print(matches)
match_texts = [doc[start:end].text for (match_id, start, end) in matches]

print(match_texts)


