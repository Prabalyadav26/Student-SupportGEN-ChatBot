# 🎓 Student Support AI Chatbot

An AI-powered Student Support Chatbot built using **Python**, **Streamlit**, **RAG (Retrieval-Augmented Generation)**, **Groq LLM**, and **Natural Language Processing (NLP)**.

The chatbot helps students by answering questions related to academics, admissions, courses, fees, placements, college information, and other student services using a knowledge base.

---

# 🚀 Features

- 🤖 AI-powered chatbot
- 📚 Knowledge Base Search (RAG)
- 🔍 Semantic Search using Embeddings
- 🧠 Intent Detection
- 🏷️ Entity Extraction
- 💬 Chat History
- ⚡ Fast LLM Responses using Groq
- 🎨 Interactive Streamlit UI

---

# 📁 Project Structure

```
Student-SupportGEN-ChatBot/
│
├── genai/
│   ├── __init__.py
│   ├── grok.py
│   └── prompt.py
│
├── retrieval/
│   ├── embedding.py
│   ├── search.py
│   └── vector_store.py
│
├── nlp/
│   ├── entities.py
│   ├── intent.py
│   └── preprocessing.py
│
├── utils/
│   ├── chat_history.py
│   └── helper.py
│
├── knowledge/
│   └── knowledge_base.json
│
├── chatbot.py
├── streamlit_app.py
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

# 🛠 Technologies Used

- Python 3.11+
- Streamlit
- Groq API
- Sentence Transformers
- NumPy
- Scikit-learn
- python-dotenv

---

# 📋 Prerequisites

Before running the project, install:

- Python 3.11 or later
- Git
- VS Code (Recommended)

---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone <repository-url>
```

Example

```bash
git clone https://github.com/yourusername/Student-SupportGEN-ChatBot.git
```

---

## Step 2: Open Project

```bash
cd Student-SupportGEN-ChatBot
```

---

## Step 3: Create Virtual Environment

Windows

```bash
python -m venv venv
```

---

## Step 4: Activate Virtual Environment

Command Prompt

```bash
venv\Scripts\activate
```

PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Environment Variables

Create a file named

```
.env
```

Add your Groq API key

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can get a free API key from:

https://console.groq.com/keys

---

# ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run streamlit_app.py
```

The application will open automatically in your browser.

Default URL:

```
http://localhost:8501
```

---

# 💬 How It Works

1. User enters a question.
2. NLP detects the user's intent.
3. Relevant knowledge is retrieved from the knowledge base.
4. Context is converted into a prompt.
5. Prompt is sent to Groq LLM.
6. AI generates an accurate response.
7. Chat history is stored for the session.

---

# 🧠 Knowledge Base

All student-related information is stored in:

```
knowledge/
    knowledge_base.json
```

You can update this file to add new FAQs and information.

Example:

```json
[
  {
    "question": "What are the college timings?",
    "answer": "College timings are 9 AM to 5 PM."
  }
]
```

---

# 📦 Main Modules

### chatbot.py

Handles chatbot workflow.

### streamlit_app.py

Streamlit user interface.

### genai/

- Prompt generation
- Groq API communication

### retrieval/

- Embedding generation
- Similarity search
- Vector storage

### nlp/

- Intent detection
- Entity extraction
- Text preprocessing

### utils/

- Chat history
- Helper functions

---

# 🧪 Example Questions

- What courses are available?
- What is the admission process?
- Tell me about hostel facilities.
- What are the placement statistics?
- What is the fee structure?
- How can I contact the admission office?

---

# 🛠 Troubleshooting

## ModuleNotFoundError

Ensure:

- Virtual environment is activated.
- Dependencies are installed.

```bash
pip install -r requirements.txt
```

---

## Missing API Key

Check your `.env` file:

```env
GROQ_API_KEY=your_api_key
```

---

## Streamlit Not Found

Install Streamlit:

```bash
pip install streamlit
```

---

## Import Errors

Ensure all folders contain:

```
__init__.py
```

---

# 📌 Future Enhancements

- Voice Assistant
- Multi-language Support
- PDF Knowledge Base
- Database Integration
- Authentication
- Student Login
- Admin Dashboard
- Feedback System
- Analytics Dashboard
- Conversation Export

---

# 👨‍💻 Author

**Prabal Yadav**

Frontend Developer | Python Developer

---


                        +----------------------+
                        |      Student User    |
                        +----------+-----------+
                                   |
                                   |
                                   v
                     +---------------------------+
                     |     Streamlit Frontend    |
                     |   (streamlit_app.py)      |
                     +-------------+-------------+
                                   |
                                   v
                     +---------------------------+
                     |      Chatbot Engine       |
                     |      (chatbot.py)         |
                     +-------------+-------------+
                                   |
             +---------------------+----------------------+
             |                                            |
             |                                            |
             v                                            v
 +---------------------------+               +---------------------------+
 |      NLP Processing       |               |     Retrieval Module      |
 |---------------------------|               |---------------------------|
 | • Intent Detection        |               | • Embedding Generation    |
 | • Entity Extraction       |               | • Semantic Search         |
 | • Text Preprocessing      |               | • Vector Store            |
 +-------------+-------------+               +-------------+-------------+
               |                                           |
               +---------------------+---------------------+
                                     |
                                     v
                      +-------------------------------+
                      |      Knowledge Base (JSON)    |
                      | knowledge/knowledge_base.json |
                      +---------------+---------------+
                                      |
                                      v
                      +-------------------------------+
                      |     Prompt Builder Module     |
                      |      genai/prompt.py          |
                      +---------------+---------------+
                                      |
                                      v
                      +-------------------------------+
                      |       Groq LLM API            |
                      |       genai/grok.py           |
                      +---------------+---------------+
                                      |
                                      v
                      +-------------------------------+
                      |      AI Generated Response    |
                      +---------------+---------------+
                                      |
                                      v
                      +-------------------------------+
                      |        Chat History           |
                      |    utils/chat_history.py      |
                      +---------------+---------------+
                                      |
                                      v
                            Returned to User

# 📄 License

This project is developed for educational and learning purposes.

Feel free to modify and extend it for your own projects.

---

# ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.

Happy Coding! 🚀