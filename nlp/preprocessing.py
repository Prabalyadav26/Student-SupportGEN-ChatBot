import re
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")


def clean_text(text):
    """
    Clean user input before NLP processing.
    """

    # Convert to lowercase
    text = text.lower()

    # Replace common short forms
    replacements = {
        "pls": "please",
        "plz": "please",
        "u": "you",
        "yr": "year",
        "1st": "first",
        "2nd": "second",
        "3rd": "third",
        "i'm": "i am",
        "you're": "you are",
        "it's": "it is",
        "can't": "cannot",
        "don't": "do not",
        "won't": "will not"
    }

    words = text.split()

    words = [replacements.get(word, word) for word in words]

    text = " ".join(words)

    # Remove punctuation
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    return text



IMPORTANT_WORDS = {
    "first",
    "second",
    "third"
}


def remove_stopwords(text):

    doc = nlp(text)

    words = []

    for token in doc:

        if token.text in IMPORTANT_WORDS:
            words.append(token.text)

        elif not token.is_stop:
            words.append(token.text)

    return " ".join(words)




def lemmatize(text):

    doc = nlp(text)

    words = []

    for token in doc:
        words.append(token.lemma_)

    return " ".join(words)

def extract_keywords(text):

    doc = nlp(text)

    keywords = []

    for token in doc:

        if (
            not token.is_stop
            and
            not token.is_punct
        ):

            keywords.append(token.lemma_)

    return " ".join(keywords)