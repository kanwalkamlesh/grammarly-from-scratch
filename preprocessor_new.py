import tkinter as tk
import string
import spacy
from spell_checker_new import correct  # Import the spell checker
from grammar_corrector import correct_grammar
from tone_analyzer import analyze_tone_custom, get_tone_summary_custom

# Load spaCy's small English model
nlp = spacy.load("en_core_web_sm")

# ----------------------
# Spell checker function
# ----------------------
def check_spelling(text):
    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    suggestions = {}
    for word in words:
        corrected = correct(word)
        if corrected != word:
            suggestions[word] = corrected
    return suggestions

# ----------------------
# Text Preprocessing
# ----------------------
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_space]
    pos_tags = [(token.text, token.pos_) for token in doc]
    preprocessed_text = " ".join(tokens)
    return preprocessed_text, tokens, pos_tags

# ----------------------
# GUI Function
# ----------------------
def launch_text_input_gui():
    root = tk.Tk()
    root.title("AI Writing Assistant")

    input_label = tk.Label(root, text="Enter text for processing:")
    input_label.pack(padx=10, pady=5)

    text_box = tk.Text(root, height=10, width=60)
    text_box.pack(padx=10, pady=10)

    output_label = tk.Label(root, text="Processed output:")
    output_label.pack(padx=10, pady=5)

    output_box = tk.Text(root, height=10, width=60)
    output_box.pack(padx=10, pady=10)

    spelling_label = tk.Label(root, text="Spelling Errors:")
    spelling_label.pack(padx=10, pady=5)

    spelling_listbox = tk.Listbox(root, height=5, width=60)
    spelling_listbox.pack(padx=10, pady=10)

    tone_label = tk.Label(root, text="Tone Analysis:")
    tone_label.pack(padx=10, pady=5)

    tone_textbox = tk.Text(root, height=5, width=60)
    tone_textbox.pack(padx=10, pady=10)

    def on_submit():
        user_text = text_box.get("1.0", tk.END).strip()

        # Step 1: Process for spelling errors
        spelling_errors = check_spelling(user_text)

        # Correct text based on spelling errors
        corrected_text = user_text
        for word, suggestion in spelling_errors.items():
            corrected_text = corrected_text.replace(word, suggestion)

        # Step 2: Apply grammar correction on the corrected text
        corrected_text = correct_grammar(corrected_text)

        # Step 3: Preprocess text (tokenization, POS tagging, etc.)
        preprocessed_text, tokens, pos_tags = preprocess_text(corrected_text)

        result = f"Original Text:\n{user_text}\n\n"
        result += f"Preprocessed Text:\n{preprocessed_text}\n\n"
        result += f"Tokens: {tokens}\n\nPOS Tags: {pos_tags}\n"

        # Spelling Errors
        spelling_listbox.delete(0, tk.END)
        if spelling_errors:
            for word, suggestion in spelling_errors.items():
                spelling_listbox.insert(tk.END, f"{word} → {suggestion}")
        else:
            spelling_listbox.insert(tk.END, "No spelling errors found.")

        # Display grammar-corrected text
        result += f"\n\nGrammar-Corrected Text:\n{corrected_text}\n"
        display_output(output_box, result)

        # Tone Analysis
        tone_result = analyze_tone_custom(user_text)
        tone_summary = get_tone_summary_custom(tone_result)
        tone_textbox.delete(1.0, tk.END)
        tone_textbox.insert(tk.END, tone_summary)

    def display_output(output_box, result):
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

    def on_clear_output():
        output_box.delete("1.0", tk.END)
        spelling_listbox.delete(0, tk.END)
        tone_textbox.delete(1.0, tk.END)
        text_box.delete("1.0", tk.END)

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=5)

    clear_button = tk.Button(root, text="Clear Output", command=on_clear_output)
    clear_button.pack(pady=5)

    root.mainloop()

# ----------------------
# Start GUI
# ----------------------
launch_text_input_gui()

