from retrieval.vector_store import search
from genai.promt import build_prompt
from genai.grok import ask_groq
from nlp.intent import detect_intent
from nlp.entities import extract_entities
from utils.chat_history import add_message


def ask_chatbot(query):

    intent = detect_intent(query)
    entities = extract_entities(query)

    if intent == "greeting":
        return "Hello! 👋 How can I help you today?"

    if intent == "thanks":
        return "You're welcome! 😊"

    results = search(query)

    context = ""

    for item in results:

        context += f"""
Question:
{item['question']}

Answer:
{item['answer']}
"""

    prompt = build_prompt(query, context)

    response = ask_groq(prompt)

    add_message("user", query)
    add_message("assistant", response)

    return response