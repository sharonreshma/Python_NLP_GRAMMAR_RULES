import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
patterns = {
    "SV": [{"POS": "PRON"}, {"POS": "VERB"}],
    "SVO": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}],
    "SVC": [{"POS": {"IN": ["PRON", "NOUN", "PROPN"]}},{"POS": "VERB", "TAG": "VBZ"},{"POS": "DET", "OP": "?"},{"POS": {"IN": ["ADJ", "NOUN", "PROPN"]}}],
    "DirectObject": [{"POS": {"IN": ["VERB", "AUX"]}, "OP": "+"},{"DEP": "dobj"}],
    "IndirectObject": [{"POS": {"IN": ["VERB", "AUX"]}, "OP": "+"},{"DEP": "iobj"},{"DEP": "dobj", "OP": "?"}],
    "SVOO": [{"POS": {"IN": ["PRON"]}}, {"POS": {"IN": ["VERB"]}}, {"POS": {"IN": ["NOUN", "PROPN"]}, "DEP": "dobj"},{"POS": {"IN": ["NOUN", "PROPN"]}, "DEP": "iobj"}],
    "DirectVerb": [{"POS": {"IN": ["NOUN", "PROPN", "PRON"]}}, {"POS": "VERB"}, {"POS":"ART"},{"POS": {"IN": ["NOUN", "PROPN"]}}],
    "IndirectVerb": [{"POS": {"IN": ["NOUN", "PROPN", "PRON"]}}, {"POS": "VERB"}, {"POS": "ADP"}, {"POS": {"IN": ["NOUN", "PROPN"]}}],
    
}

for label, pattern in patterns.items():
    matcher.add(label, [pattern])
sentence = input("Enter a sentence: ")
doc = nlp(sentence)
matches = matcher(doc)

print("Matched Syntactic Patterns:")
for match_id, start, end in matches:
    match_id_str = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(f"{match_id_str}: {span.text}")

