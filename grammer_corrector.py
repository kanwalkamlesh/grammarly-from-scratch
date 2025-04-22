def correct_grammar(text):
    words = text.strip().split()

    # Rule-based replacements
    corrections = {
        ("i", "are"): ["i", "am"],
        ("he", "are"): ["he", "is"],
        ("she", "are"): ["she", "is"],
        ("it", "are"): ["it", "is"],
        ("you", "is"): ["you", "are"],
        ("they", "is"): ["they", "are"],
        ("we", "is"): ["we", "are"],
    }

    corrected = []
    i = 0
    while i < len(words):
        if i < len(words) - 1:
            pair = (words[i].lower(), words[i+1].lower())
            if pair in corrections:
                corrected.extend(corrections[pair])
                i += 2
                continue
        corrected.append(words[i])
        i += 1

    # Capitalize "I" if it's the first word or standalone
    for idx, word in enumerate(corrected):
        if word == "i":
            corrected[idx] = "I"

    return " ".join(corrected)