# 🚀 Web-Navigator-AI-Agent

## 📌 Problem Statement Chosen
Build an AI Agent that can take natural language instructions and autonomously drive the web on a local computer.

---

## 📝 Detailed Proposal & Prototype Plan
We built a fully local AI agent that runs offline using **Ollama models**.

- Understands simple English instructions  
- Converts them into step-by-step execution plans  
- Uses browser automation (Playwright/Selenium) to navigate the web  
- Extracts and returns structured results (tables, CSV, JSON)  
- Adds post-call features such as transcripts, summaries, memory, Ask-AI chat, and recording playback  

### 🔄 Prototype Flow
1. User types an instruction (e.g., “Find top 5 laptops under 50k”).  
2. LLM (Ollama) parses the instruction into a plan.  
3. Browser automation executes the plan in Chrome headless.  
4. Extracted data is structured and displayed/exported.  
5. Extra features (meeting calls, transcripts, summaries, recordings) enhance usability.  

---

## 🌟 Unique Features of Our Project
- **100% Local Execution** → Runs fully offline with Ollama (no cloud, no API keys).  
- **Multi-Model Ecosystem** → Integrated **Gemma, LLaMA, Granite, Qwen, Smollm, Llava, BGE-m3**.  
- **Dynamic Model Selection** → Fast models for parsing, reasoning models for planning, embeddings for transcript search.  
- **Meeting Flow Integration** → Supports demo calls with transcripts, summaries, Ask-AI chat, and timecoded playback.  
- **Memory & Transcript Search** → Semantic transcript search using **BGE-m3** embeddings.  
- **UI Innovation** → Clean Tailwind UI with a **model selector** and **demo personas** (Health, Education, Skincare, Diet).  
- **Structured Result Pipeline** → Converts raw web data into **ranked, consistent outputs** (tables, JSON, CSV).  

---

## 🚀 Features to be Implemented
- Instruction Parsing using multiple Ollama models  
- Browser Automation (search, click, extract, fill forms)  
- Structured Outputs (ranked tables, JSON, CSV)  
- Model Selector UI with all Ollama models integrated  
- Meeting Calls, Transcripts & Summaries  
- Ask-AI Chat with memory  
- Record/Playback with transcript search  
- **Privacy-first execution** with fully local setup  

---

## 🛠 Tech Stack Used
- **LLM Runtime (Ollama Models Tested):**  
  - Gemma  
  - LLaMA  
  - Granite  
  - Qwen  
  - Smollm  
  - Llava  
  - BGE-m3  
- **Orchestration:** Python + LangChain  
- **Browser Automation:** Playwright / Selenium  
- **Frontend:** React + Tailwind  
- **Embeddings:** BGE-m3 for transcript indexing  
- **Storage:** Local storage, JSON export  

---

## 👥 Contribution Details of Each Team Member

**👤 Ashmit — LLM Setup & Instruction Parsing**  
- Installed and tested Gemma, LLaMA, Granite, Qwen, Smollm, Llava, and BGE-m3 using Ollama  
- Designed instruction parsing & model selection logic  

**👤 Person 2 — Browser Automation**  
- Implemented Playwright/Selenium automation  
- Linked parsed steps with real browser actions  
- Added error handling & retries  

**👤 Person 3 — Structured Results & Exports**  
- Built pipeline for structured outputs (tables, CSV, JSON)  
- Implemented ranking/scoring system  

**👤 Person 4 — User Interface & Model Selector**  
- Designed UI (search bar, model picker, demo call)  
- Integrated all Ollama models in a clean interface  

**👤 Person 5 — Post-Call Features & Memory**  
- Developed transcripts, summaries, and Ask-AI chat  
- Added memory + transcript search (BGE-m3)  
- Linked recordings with playback & navigation  

---
