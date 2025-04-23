# Rule-Based Grammar Checker
import re
import spacy
nlp = spacy.load("en_core_web_sm")
def grammar_check(text):
    issues = []
    
    # Run-on sentences (Simple regex to detect commas or semicolons joining two independent clauses without a conjunction)
    run_on_pattern = r"([a-zA-Z0-9]+[,;])([a-zA-Z0-9]+)"
    run_on_matches = re.findall(run_on_pattern, text)
    
    for match in run_on_matches:
        issues.append({
            "type": "Grammar",
            "text": f"Possible run-on sentence: '{match[0]}{match[1]}'",
            "explanation": "Consider splitting this into two sentences or adding a conjunction.",
            "position": text.find(match[0])
        })

    # Double negatives (e.g., "not never", "not nothing")
    double_negative_pattern = r"\bnot\s+\b.*\bnot\b"
    double_neg_matches = re.findall(double_negative_pattern, text, re.IGNORECASE)
    
    for match in double_neg_matches:
        issues.append({
            "type": "Grammar",
            "text": f"Double negative detected: '{match}'",
            "explanation": "Double negatives can confuse meaning. Consider rephrasing.",
            "position": text.find(match)
        })

    # Subject-verb agreement (Simple check for singular/plural mismatches using spaCy's POS tagging)
    doc = nlp(text)
    for sent in doc.sents:
        subject = None
        verb = None
        for token in sent:
            if token.dep_ == "nsubj":
                subject = token
            if token.pos_ == "VERB" and token.dep_ == "ROOT":
                verb = token

        if subject and verb:
            # Simple check: singular subject should match with singular verb
            if subject.tag_ in ["NN", "NNP"] and verb.tag_ == "VBP":
                issues.append({
                    "type": "Grammar",
                    "text": f"Subject-verb agreement issue: '{subject.text} {verb.text}'",
                    "explanation": "Singular subjects should use singular verbs (e.g., 'He goes', not 'He go').",
                    "position": subject.idx
                })

    # Punctuation errors using regex (extra space before punctuation, missing punctuation at sentence end)
    punctuation_issues = check_punctuation(text)
    issues.extend(punctuation_issues)
    
    return issues

# Function to check punctuation errors (Extra spaces before punctuation, Missing punctuation at end)
def check_punctuation(text):
    issues = []

    # Check for missing punctuation at sentence end
    if not re.search(r"[.!?]$", text):
        issues.append({
            "type": "Punctuation",
            "text": "Missing punctuation at the end of the sentence.",
            "explanation": "Sentences should end with '.', '!', or '?'",
            "position": len(text) - 1
        })
    
    # Check for extra spaces before punctuation
    extra_space_before_punctuation = re.findall(r"\s+[.,!?;]", text)
    for match in extra_space_before_punctuation:
        issues.append({
            "type": "Punctuation",
            "text": f"Extra space before punctuation: '{match}'",
            "explanation": "There should be no space before punctuation.",
            "position": text.find(match)
        })

    return issues
