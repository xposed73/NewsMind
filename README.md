# 🧠 NewsMind

**Local AI-powered news aggregator using GGUF LLMs.**

NewsMind extracts articles from multiple global news sources, summarizes them using a locally hosted LLM (like Mistral or LLaMA in GGUF format), and stores the results in a clean JSONL format. Ideal for privacy-focused users and offline NLP workflows.

---

## 🚀 Features

- ✅ Pull news from multiple websites
- ✅ Extract full articles using `newspaper3k`
- ✅ Summarize with local LLM using `llama-cpp-python`
- ✅ Store results in `news.jsonl`
- ✅ Fully offline & private (no API keys needed)

---

## 🛠️ Installation (using [`uv`](https://github.com/astral-sh/uv) - recommended)

`uv` is a fast Python package/dependency manager with built-in virtualenv support.

### ✅ Prerequisites

Install `uv`:
https://docs.astral.sh/uv/getting-started/installation/#installation-methods
```bash

# Clone the repo
git clone https://github.com/xposed73/NewsMind.git
cd NewsMind

# Sync dependencies
uv sync

# Run the script
uv run main.py
