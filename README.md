# 🤖 Chatbot Manager

A simple chatbot system built with Python that allows users to interact with predefined responses. The chatbot can log conversations and dynamically load responses from a JSON file.

---

## 📌 Features
✅ **Predefined Responses** – The bot answers common questions.  
✅ **Customizable Responses** – Modify `responses.json` to add more responses.  
✅ **Conversation Logging** – Logs chats in `chat_logs.json`.  
✅ **Multiple Chatbots** – Create and manage multiple chatbot instances.  

---
### **Install Dependencies**
Ensure you have **Python 3.x** installed.

> 🔹 **Note**: The bot only requires Python's built-in `json` and `datetime` modules.

---

## 🛠️ Usage

### **Run the Chatbot**
```sh
python main.py
```

### **Exit the Chat**
To save chat logs and exit:
```
You: exit
Chat logs saved. Exiting...
```

---

## 📂 Project Structure
```
📁 ChatBot
│── 📄 main.py         # Chatbot manager & conversation logic
│── 📄 responses.json  # Predefined chatbot responses
│── 📄 chat_logs.json  # Chat history (auto-generated)
│── 📄 README.md       # Documentation
```

---

## 📝 Customizing Responses
You can edit `responses.json` manually:
```json
{
    "hello": "Hello! How can I assist you today?",
    "who invented python": "Python was created by Guido van Rossum and released in 1991."
}
```
Or, train it via chat using:
```
train:question|answer
train:Who is father of computer?|charless babbage
```


💡 **Ideas for Improvement**:
- 🌍 Integrate real-time APIs (e.g., weather, news)
- 🧠 Implement AI-based response generation
- 📝 Add GUI support
```
