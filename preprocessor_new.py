import tkinter as tk
import string
import spacy
from spell_checker_new import check_spelling  # Import spell check module

# Load spaCy's small English model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Lowercase text
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Process text using spaCy
    doc = nlp(text)

    # Tokenization and Lemmatization
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_space]

    # POS tagging (optional)
    pos_tags = [(token.text, token.pos_) for token in doc]

    # Remove stopwords and return preprocessed text
    preprocessed_text = " ".join(tokens)
    
    # Return preprocessed text and POS tagging for reference
    return preprocessed_text, tokens, pos_tags

# GUI Function
def launch_text_input_gui():
    root = tk.Tk()
    root.title("AI Writing Assistant")

    # Input text box
    input_label = tk.Label(root, text="Enter text for processing:")
    input_label.pack(padx=10, pady=5)
    text_box = tk.Text(root, height=10, width=60)
    text_box.pack(padx=10, pady=10)

    # Output text box
    output_label = tk.Label(root, text="Processed output:")
    output_label.pack(padx=10, pady=5)
    output_box = tk.Text(root, height=10, width=60)
    output_box.pack(padx=10, pady=10)

    def on_submit():
        user_text = text_box.get("1.0", tk.END).strip()

        # Call the preprocess function
        preprocessed_text, tokens, pos_tags = preprocess_text(user_text)

        # Check for spelling errors and suggestions
        spelling_errors = check_spelling(user_text)

        # Prepare result text for displaying in the output box
        result = f"Original Text:\n{user_text}\n\n"
        result += f"Preprocessed Text:\n{preprocessed_text}\n\n"
        result += f"Tokens: {tokens}\n\nPOS Tags: {pos_tags}\n"

        # Add spelling errors and suggestions to the result
        if spelling_errors:
            result += "\nSpelling Errors and Suggestions:\n"
            for word, suggestion in spelling_errors.items():
                result += f"Word: {word}, Correction: {suggestion}\n"
        else:
            result += "\nNo spelling errors found."

        # Display the result in the output box
        display_output(output_box, result)

        # Clear the input text box for the next entry
        text_box.delete("1.0", tk.END)

    # Clear button
    def on_clear_output():
        output_box.delete("1.0", tk.END)

    # Submit button
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=5)

    # Clear output button
    clear_button = tk.Button(root, text="Clear Output", command=on_clear_output)
    clear_button.pack(pady=5)

    # Start the GUI loop
    root.mainloop()

# Function to display the processed result in the output box
def display_output(output_box, result):
    output_box.delete("1.0", tk.END)  # Clear the current content
    output_box.insert(tk.END, result)  # Insert the new result text

# Run the GUI
launch_text_input_gui()
