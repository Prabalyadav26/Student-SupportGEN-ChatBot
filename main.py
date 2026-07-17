from retrieval.vector_store import search
from genai.grok import ask_groq
from genai.promt import build_prompt
from utils.chat_history import add_message
from nlp.intent import detect_intent
from nlp.entities import extract_entities


while True:

    query = input("\nYou : ")

    if query.lower() == "exit":
        break

    intent = detect_intent(query)
    entities = extract_entities(query)


    if intent == "greeting":
        print("\nBot : Hello! How can I help you today?")
        continue

    if intent == "thanks":
        print("\nBot : You're welcome! 😊")
        continue

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

    response = ask_gemini(prompt)

    print("\nBot :", response)

    add_message("user", query)

    add_message("assistant", response)