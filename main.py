import tkinter as tk
import spacy
import string
from spacy.tokens import Doc
import re
from input_new import launch_text_input_gui
from preprocessor_new import preprocess_text, launch_text_input_gui
from rule_based import grammar_check, check_punctuation

from spell_checker_new import check_spelling

# Load spaCy's small English model



# Run the GUI
launch_text_input_gui()
