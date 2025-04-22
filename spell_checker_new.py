from spellchecker import SpellChecker

# Initialize the spell checker
spell = SpellChecker()

def check_spelling(text):
    # Tokenize the input text into words
    words = text.split()

    # Find words that might be misspelled
    misspelled = spell.unknown(words)

    # Store the suggestions for each misspelled word
    suggestions = {}

    for word in misspelled:
        # Get the most likely correction for the misspelled word
        suggestions[word] = spell.correction(word)

    return suggestions
  # Import the spell check module