import spacy

nlp = spacy.load("en_core_web_sm")



COURSES = [
    "mca",
    "bca",
    "btech",
    "mba"
]

TOPICS = [
    "fee",
    "fees",
    "hostel",
    "library",
    "attendance",
    "scholarship"
]


def extract_entities(text):

    text = text.lower()

    entities = {}

    for course in COURSES:

        if course in text:

            entities["course"] = course

    for topic in TOPICS:

        if topic in text:

            entities["topic"] = topic

    return entities