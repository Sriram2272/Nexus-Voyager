# Web-Navigator-AI-Agent

We built a local AI agent that runs fully offline with **Ollama models**.  
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

## ⚡ Important
The system runs **100% locally** — all models are from **Ollama**.  

We experimented with many models, from small fast ones to large reasoning models, including:  
**Gemma, LLaMA, Granite, Qwen, Smollm, Llava, BGE-m3, and others.**  

👉 No cloud APIs or keys are used.  

---

## 👥 Team Contributions
We worked as a team of 5, and divided the work equally. Each person owned a separate part of the project, but we also helped each other during integration.  

---

### 👤 Person 1 — LLM Setup & Instruction Parsing
- Installed and tested a wide range of Ollama models (small to large).  
- Compared models like **Smollm, Gamma, LLaMA2/3, Gemma2/3, Granite, Qwen, Llava, BGE-m3** for speed and accuracy.  
- Created the instruction parsing layer so AI could turn queries like *“Find top 5 laptops under 50k”* into a clear plan.  
- Handled model selection logic (small fast model for parsing, bigger models for reasoning).  

---

### 👤 Person 2 — Browser Automation
- Set up **Playwright/Selenium** for controlling Chrome in headless mode.  
- Connected parsed instructions to **real browser actions** (search, click, extract data, fill forms).  
- Added **error handling and retries** so tasks don’t fail easily.  
- Ensured the automation pipeline worked with different LLM outputs from Ollama.  

---

### 👤 Person 3 — Structured Results & Exports
- Built the pipeline to turn scraped data into **clean structured results**.  
- Supported outputs like **ranked tables, CSV download, and JSON export**.  
- Added scoring/ranking so results are meaningful (not random).  
- Made outputs consistent across all Ollama models used.  

---

### 👤 Person 4 — User Interface & Model Selector
- Designed the **search bar UI with model picker** (chip + `+` modal).  
- Integrated **all Ollama models** into the selector, showing which are local vs available to download.  
- Worked on the **Demo Call UI** (meeting personas like Health, Education, Skincare, Diet, etc.).  
- Kept the UI consistent with NexusAI’s theme and simple for users.  

---

### 👤 Person 5 — Post-Call Features & Memory
- Built **transcripts, meeting summaries, and Ask-AI chat** (all powered by Ollama).  
- Added **multi-step reasoning & memory** — AI could remember earlier instructions.  
- Implemented **transcript search** using embedding models like **BGE-m3**.  
- Connected the **recordings panel** with playback and mock export.  

---

## 🔑 Key Features
- Instruction Parsing via multiple Ollama models  
- Browser Control with Playwright/Selenium  
- Structured Outputs (tables, CSV, JSON)  
- Model Selector UI with all Ollama models available  
- Meeting Flows — demo calls, transcripts, summaries, Ask-AI, and recordings  
- Local-only setup (no cloud, no API keys)  

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
