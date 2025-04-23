# tone_analyzer.py

def analyze_tone_custom(text):
    emotional_keywords = {
        'joy': ['happy', 'joy', 'delighted', 'pleased', 'glad', 'excited'],
        'anger': ['angry', 'furious', 'outraged', 'annoyed', 'irritated'],
        'sadness': ['sad', 'unhappy', 'depressed', 'miserable', 'gloomy'],
        'fear': ['afraid', 'scared', 'worried', 'anxious'],
        'surprise': ['surprised', 'amazed', 'astonished', 'shocked'],
        'disgust': ['disgusted', 'revolted', 'appalled'],
        'formal': ['therefore', 'furthermore', 'thus', 'hence'],
        'informal': ['gonna', 'wanna', 'yeah', 'lol', 'btw', 'cool']
    }

    tone_attributes = []
    emotional_indicators = {}
    text_lower = text.lower()

    for emotion, keywords in emotional_keywords.items():
        for keyword in keywords:
            if keyword in text_lower:
                emotional_indicators[emotion] = emotional_indicators.get(emotion, 0) + 1

    if '?' in text:
        tone_attributes.append("Questioning")
    if '!' in text:
        tone_attributes.append("Emphatic")

    # Basic tone assumption
    if 'not' in text_lower or "n't" in text_lower or 'bad' in text_lower:
        overall_tone = "Negative"
    elif any(word in text_lower for word in emotional_keywords['joy']):
        overall_tone = "Positive"
    else:
        overall_tone = "Neutral"

    return {
        'text': text,
        'overall_tone': overall_tone,
        'tone_attributes': tone_attributes,
        'emotional_indicators': emotional_indicators
    }

def get_tone_summary_custom(result):
    summary = f"Overall tone: {result['overall_tone']}\n"
    summary += "Tone attributes: " + ", ".join(result['tone_attributes']) + "\n"
    if result['emotional_indicators']:
        emotions = [f"{k}({v})" for k, v in result['emotional_indicators'].items()]
        summary += "Emotions: " + ", ".join(emotions)
    else:
        summary += "No strong emotional indicators found."
    return summary
