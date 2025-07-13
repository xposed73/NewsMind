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
```bash

# Clone the repo
git clone https://github.com/xposed73/NewsMind.git
cd NewsMind

# Sync dependencies
uv sync

# Run the script
uv run main.py


```
## 🔧 Customization

You can easily configure which sources to pull news from and which local LLM model to use:

```python
# ✅ Add your preferred news sources
WEBSITES = [
    'https://www.reuters.com/world/',
    'https://www.bbc.com/news',
    'https://www.aljazeera.com/news/',
    # Add more sources as needed
]

# 🧠 Path to your GGUF model (downloaded locally)
MODEL_PATH = "mistral-7b-v0.1.Q2_K.gguf"


## 🙏 Support My Work

If you find this project helpful, consider supporting it by donating via UPI.

![Donate via UPI](https://raw.githubusercontent.com/xposed73/YTDL-python/main/upi-donation.png)

Thank you for your support! ❤️
