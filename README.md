# Web-Navigator-AI-Agent

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

## 👤 Person 1 — Ashmit (The Architect of Intelligence)  
- Installed and tested multiple **Ollama models** (small fast ones + large reasoning models).  
- Built the **instruction parsing layer** to turn plain English queries into step-by-step plans.  
- Designed **model selection logic** (fast models for speed, large models for accuracy).  
- Ensured the agent always chooses the **best model for the task**.  

---

## 👤 Person 2 — Prajithaa (The Voice of Experience)  
- Designed the **search bar UI with a built-in model picker**, letting users choose which Ollama model to use.  
- Built the **Demo Call UI** with personas like Health, Education, Skincare, and Diet.  
- Focused on keeping the design **modern, minimal, and consistent** with NexusAI’s theme.  
- Made Nexus feel **personal and approachable**, turning it from a tool into an experience.  

---

## 👤 Person 3 — Sriram (The Explorer of the Web)  
- Implemented **browser automation** using Playwright and Selenium.  
- Connected AI instructions to real browser actions (search, click, extract, fill forms).  
- Added **error handling and retries** to prevent failures during automation.  
- Optimized the pipeline so Nexus works smoothly across different **LLM outputs**.  

---

## 👤 Person 4 — Ansh (The Keeper of Memory)  
- Developed **transcripts, meeting summaries, and Ask-AI chat** so Nexus could hold conversations beyond one query.  
- Added **multi-step reasoning and embedding search** for recalling past instructions.  
- Linked the **recordings panel** with playback and time-code navigation.  
- Ensured Nexus doesn’t just solve one task but can **learn, remember, and grow** with users.  

---

## 👤 Person 5 — Abhinendra (The Alchemist of Data)  
- Built the **data pipeline** to clean and organize raw scraped results.  
- Converted results into **structured formats** (ranked tables, CSV, JSON).  
- Added **scoring and ranking logic** so answers are meaningful, not random.  
- Ensured **consistent outputs** across all Ollama models.  

