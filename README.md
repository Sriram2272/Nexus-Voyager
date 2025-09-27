# Web-Navigator-AI-Agent

We built a **local AI agent** that runs fully offline with **Ollama models**.  
It understands simple English commands, plans steps, drives the browser, and shows clean results.  

Extra features include:  
- Meeting calls  
- Transcripts  
- Summaries  
- Ask-AI chat  
- Record/playback  

All teamwork, no cloud needed.  
**NexusAI — Local AI Agent for Web Automation**

---

## 🎯 Hackathon Challenge
**“Build an AI Agent that can take natural language instructions and autonomously drive the web on a local computer.”**

---

## 🛠 How We Built It
We combined locally running **LLMs (via Ollama)** with browser automation to create an AI that can:  

- Understand user instructions in plain English  
- Plan steps, drive the browser, and extract results  
- Return structured outputs like tables or JSON  
- Provide transcripts, summaries, and Ask-AI features after a session  

---

## ⚡ Why This Matters
The system runs **100% locally** — all models are from **Ollama**.  

We experimented with a wide range of models, from small fast ones to large reasoning models, including:  
**Gemma, LLaMA, Granite, Qwen, Smollm, Llava, BGE-m3, and others.**  

👉 **No cloud APIs or keys are used. Everything stays on-device.**

---

## 👥 Team Contributions
We worked as a team of 5 and divided the work equally. Each person owned a key part of the project, but we supported each other during integration.  

---

### 👤 Person 1 — LLM Setup & Instruction Parsing
- Installed and tested many Ollama models (small to large).  
- Compared models for speed and accuracy.  
- Created the **instruction parsing layer** to turn queries like *“Find top 5 laptops under 50k”* into a step-by-step plan.  
- Designed model selection logic (fast models for parsing, larger ones for reasoning).  

---

### 👤 Person 2 — Browser Automation
- Set up **Playwright/Selenium** for controlling Chrome in headless mode.  
- Connected parsed instructions to **real browser actions** (search, click, extract, fill forms).  
- Added **error handling and retries** for reliable execution.  
- Ensured smooth integration with different LLM outputs.  

---

### 👤 Person 3 — Structured Results & Exports
- Built the pipeline to convert raw scraped data into **clean structured results**.  
- Supported exports like **ranked tables, CSV, and JSON**.  
- Implemented scoring/ranking so results were meaningful, not random.  
- Made outputs consistent across all Ollama models.  

---

### 👤 Person 4 — User Interface & Model Selector
- Designed the **search bar UI with a model picker** (chip + `+` modal).  
- Integrated **all Ollama models** into the selector, showing local vs available models.  
- Built the **Demo Call UI** with personas (Health, Education, Skincare, Diet, etc.).  
- Kept the UI clean, modern, and consistent with NexusAI’s theme.  

---

### 👤 Person 5 — Post-Call Features & Memory
- Developed **transcripts, meeting summaries, and Ask-AI chat** (all powered by Ollama).  
- Added **multi-step reasoning and memory** so AI could remember past instructions.  
- Implemented **transcript search** with embedding models like **BGE-m3**.  
- Linked the **recordings panel** with playback and timecode navigation.  

---

## 🔑 Key Features
- Instruction Parsing via multiple Ollama models  
- Browser Automation with Playwright/Selenium  
- Structured Outputs (tables, CSV, JSON)  
- Model Selector UI with all Ollama models available  
- Meeting Flows: demo calls, transcripts, summaries, Ask-AI, recordings  
- 100% Local Setup — no cloud, no API keys  

---

## 🛠 Tech Stack
- **LLM Runtime**: Ollama (all available models tested)  
- **Orchestration**: Python + LangChain  
- **Browser Automation**: Playwright / Selenium  
- **Frontend**: React + Tailwind  
- **Embeddings**: BGE-m3 for transcript indexing  
- **Storage**: Local storage / JSON export  

---

## 🌍 About the Company
We participated under **OneCompiler**, an online coding and development platform helping **12.8M+ developers worldwide** to write, run, and share code.  

Their mission is to make coding **accessible for everyone**.  

---

✨ This README highlights our teamwork, fair contribution split, and the fact that we explored the **entire Ollama model ecosystem** in our project.
