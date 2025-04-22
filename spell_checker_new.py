from spellchecker import SpellChecker

def check_spelling(text):
    spell = SpellChecker()

    words = text.split()
    misspelled = spell.unknown(words)

    corrections = {}
    for word in misspelled:
        correction = spell.correction(word)
        corrections[word] = correction

    return corrections
