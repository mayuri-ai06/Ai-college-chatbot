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

## ⚙️ Features

* Conversational AI interface
* Tool calling (internet + custom database)
* Session memory
* College information retrieval

---

## 🖥️ Demo

![Chatbot Demo](assets/chatbot-demo.png)
![Chatbot Demo](assets/chatbot-demo.png)

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
