# 🤖 AI Code Editor Agent (Learning Project)

This is a small project I built while learning more about **Python, APIs, and agent-style AI tools**.  
The idea was to create a simple “AI code editor” that can read code, suggest fixes, and simulate how modern AI coding assistants behave.

This is not meant to be a production tool — it’s more like a **sandbox for learning and experimenting** with LLMs and automation.

---

## 🧠 What I’m Trying to Learn Here

- How AI APIs work in real projects  
- Structuring Python projects in a cleaner way  
- Prompt engineering and function calling  
- Handling files and parsing code  
- Building small feedback loops where the AI improves its responses  

This repo represents my current level of learning — some parts are simple, some are experimental, and everything is part of the process.

---

## ⚙️ Main Features

- Basic agent that can **analyze code and suggest fixes**
- Integration with **Google Gemini API** for AI responses
- Simple **feedback loop** to retry or refine suggestions
- Ability to **read project files** and apply targeted changes
- Modular structure separating:
  - Agent logic  
  - API communication  
  - File handling  

---

## 🛠 Tech Stack

- **Python 3**
- **Google Gemini API**
- **uv / virtual environments**
- **Git & GitHub**
- **Linux / CLI workflow**

---

## 🔐 Notes on Security

API keys are stored in a `.env` file and **never committed** to the repository.

---

## Why I Built This

I wanted hands-on experience with:
- AI agents
- Debugging automation
- Real API usage
- Organizing a Python project beyond a single script

It’s basically my way of learning by building instead of only reading tutorials.

---

## How to Run (Basic)

```bash
git clone <repo>
cd <repo>
uv run main.py <arguments>
