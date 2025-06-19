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

## 🛠️ Requirements

Install dependencies:

```bash
pip install newspaper3k lxml_html_clean llama-cpp-python
