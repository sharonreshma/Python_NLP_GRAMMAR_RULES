import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
patterns = {
    "NP": [{"POS": {"IN": ["DET", "ADJ"]}, "OP": "*"}, {"POS": "NOUN"}],
    "VP": [{"POS": {"IN": ["VERB", "AUX"]}, "OP": "+"}, {"POS": {"IN": ["ADV", "PART"]}, "OP": "*"}],
    "PP": [{"POS": "ADP"}, {"POS": {"IN": ["DET", "ADJ"]}, "OP": "*"}, {"POS": "NOUN"}],
    "SBAR": [{"LOWER": "if", "OP": "?"}, {"POS": {"IN": ["ADV", "ADP", "DET", "PRON"]}, "OP": "*"},
             {"POS": {"IN": ["VERB", "AUX"]}, "OP": "*"}],
    "CONJP": [{"POS": "CONJ"}, {"POS": {"IN": ["ADV", "VERB", "NOUN", "ADJ", "PART"]}, "OP": "*"}],
    "INTJ": [{"POS": "INTJ"}],
    "ADJP": [{"POS": "ADJ", "OP": "+"}, {"POS": {"IN": ["NOUN", "PROPN"]}}],
    "ADVP": [{"POS": "ADV", "OP": "+"}, {"POS": {"IN": ["ADJ"]}, "OP": "?"}],
    "RELCL": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": {"IN": ["ADV", "NOUN", "ADJ"]}, "OP": "*"}],
    "SQ": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": {"IN": ["ADV", "AUX", "NOUN", "ADJ"]}, "OP": "*"}],
    "ACT": [{"POS": {"IN": ["NOUN", "PROPN", "PRON"]}}, {"POS": "VERB"}],
    "PASS": [{"POS": {"IN": ["AUX", "VERB"]}, "DEP": {"IN": ["auxpass", "ROOT"]}}, {"POS": {"IN": ["VERB"]}}],
    "CONJ": [{"POS": "CCONJ"}, {"POS": {"IN": ["ADV", "ADP", "DET", "PRON"]}, "OP": "*"},
             {"POS": {"IN": ["VERB", "NOUN", "ADJ", "PART"]}, "OP": "*"}],
    "ART": [{"POS": "DET"}],
    "NUM": [{"POS": "NUM"}],
    "TENSE": [{"POS": "AUX"}, {"POS": "VERB"}],
    "MODAL": [{"POS": "AUX"}, {"POS": {"IN": ["VERB"]}}],
    "SVA": [{"POS": {"IN": ["NOUN", "PROPN", "PRON"]}}, {"POS": "VERB"}],
    "PC": [{"POS": "ADV"}, {"POS": "VERB"}],
    "SC": [{"POS": "PRON"}, {"POS": "VERB"}],
    "D&S": [{"POS": "DET"}, {"POS": "NOUN"}],
    "C": [{"POS": "CCONJ"}, {"POS": {"IN": ["ADV", "ADP", "DET", "PRON"]}, "OP": "*"},
          {"POS": {"IN": ["VERB", "NOUN", "ADJ", "PART"]}, "OP": "*"}],
    "SV": [{"POS": "PRON"}, {"POS": "VERB"}],
    "SVO": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}],
    "SVC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": {"IN": ["ADJ", "NOUN"]}}],
    "SVOO": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "NOUN"}],
    "SVOC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}],
    "SAdv": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "ADV"}],
    "SVA": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "ADJ"}],
    "SVAC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "ADJ"}, {"POS": "NOUN"}],
    "SVOAdv": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADV"}],
    "SVOA": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}],
    "SVOAdvC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADV"}, {"POS": "ADJ"}],
    "SVOO": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "NOUN"}],
    "SVOOC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "NOUN"}, {"POS": "ADJ"}],
    "SVOIC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "NOUN"}, {"POS": "ADJ"}],
    "SVDIO": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "NOUN"}],
    "SVOOA": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADV"}],
    "SVOAC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}],
    "SVCA": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADV"}],
    "SVAO": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}],
    "SVOAA": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADV"}, {"POS": "ADJ"}],
    "SVOACA": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADV"}],
    "SVAOAC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADV"}],
    "SVOAC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADV"}],
    "SVOCA": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADV"}],
    "SVOOC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "NOUN"}, {"POS": "ADJ"}],
    "SVAOA": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADV"}],
    "SVAOC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADV"}],
    "SVOAA": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADV"}, {"POS": "ADJ"}],
    "SVOACA": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADV"}],
    "SVAOAC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADV"}],
    "SVOAC": [{"POS": "PRON"}, {"POS": "VERB"}, {"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADV"}],
    "DirectVerb": [{"POS": {"IN": ["NOUN", "PROPN", "PRON"]}}, {"POS": "VERB"}, {"POS":"ART"},{"POS": {"IN": ["NOUN", "PROPN"]}}],
    "IndirectVerb": [{"POS": {"IN": ["NOUN", "PROPN", "PRON"]}}, {"POS": "VERB"}, {"POS": "ADP"}, {"POS": {"IN": ["NOUN", "PROPN"]}}]
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

