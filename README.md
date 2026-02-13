# 🎓 AI College Chatbot (Agentic AI)

An AI powered college assistant chatbot built using **LangChain + Groq + Streamlit**.

This chatbot can:

* Answer general questions using LLM
* Search the internet using Google Serper Tool
* Provide details of specific colleges (SIRT & JNCT) using a custom tool
* Maintain chat history (memory)

---

## 🧠 Tech Stack

* Python
* Streamlit (UI)
* LangChain Agents
* Groq LLM (gpt-oss-120b)
* Google Serper API
* Custom Tool Function Calling

---
## 🔄 Flowchart / Working

![AI College Chatbot Flowchart](assets/architecture.png)

This flowchart explains how the AI College Chatbot processes a user query.

1. The user enters a message in the Streamlit chat interface.
2. The message is passed to the LangChain agent.
3. The agent sends the query to the Groq LLM for understanding.
4. The LLM analyzes the query and decides the next action:

   * For college-related questions → retrieves data from the college database (JSON file)
   * For general or real-time questions → performs a web search using the Serper API
5. The selected tool returns information to the LLM.
6. The LLM generates a human-like response.
7. The response is displayed back to the user and conversation history is maintained.

## ⚙️ Features

* Conversational AI interface
* Tool calling (internet + custom database)
* Session memory
* College information retrieval

---

## 🖥️ Demo

![Chatbot Demo](https://github.com/mayuri-ai06/Ai-college-chatbot/blob/main/assets/toolagent_output.png?raw=true)
![Chatbot Demo](https://github.com/mayuri-ai06/Ai-college-chatbot/blob/main/assets/output%202.png?raw=true)

---

## 🚀 How to Run

1. Clone the repo
   git clone https://github.com/your-username/ai-college-chatbot.git

2. Install requirements
   pip install -r requirements.txt

3. Create `.env` file and add:
   GROQ_API_KEY=your_key_here
   SERPER_API_KEY=your_key_here

4. Run the app
   streamlit run chatbotwithowntool.py

---

## 📌 Example Questions

* Tell me about SIRT
* What is the contact number of JNCT?
* Who is the Prime Minister of India?

---

## 👩‍💻 Author

Mayuri Khatarkar
AI & ML Student
