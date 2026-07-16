GREETINGS = [
    "hi",
    "hello",
    "hey",
    "good morning",
    "good evening"
]

THANKS = [
    "thanks",
    "thank you",
    "thx"
]


def detect_intent(text):

    text = text.lower().strip()

    if text in GREETINGS:
        return "greeting"

    if text in THANKS:
        return "thanks"

    return "information"