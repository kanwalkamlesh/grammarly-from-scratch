import re
from collections import Counter

def words(text):
    return re.findall(r'\w+', text.lower())

def load_dictionary():
    with open("big.txt", encoding="utf-8") as f:
        return Counter(words(f.read()))

WORD_COUNTS = load_dictionary()
WORD_SET = set(WORD_COUNTS)

def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def known(words):
    return set(w for w in words if w in WORD_SET)

def correct(word):
    if word in WORD_SET:
        return word
    candidates = known(edits1(word)) or [word]
    return max(candidates, key=WORD_COUNTS.get)

def correct_text(text):
    tokens = text.split()
    return ' '.join(correct(word.lower()) for word in tokens)
