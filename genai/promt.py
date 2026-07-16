from utils.chat_history import get_history


def build_prompt(user_question, context):

    history = get_history()

    conversation = ""

    for item in history:

        conversation += f"""

{item['role']}:

{item['message']}
"""

    prompt = f"""

You are an AI Student Support Assistant.

Use ONLY the context below.

Conversation History

{conversation}

Knowledge Base

{context}

Current User Question

{user_question}

Answer naturally.

If answer is unavailable, say

"I couldn't find that information."

"""

    return prompt