import os
import json
from newspaper import Article
from llama_cpp import Llama

# ============ CONFIG ============

WEBSITES = [
    'https://www.reuters.com/world/',
    'https://www.bbc.com/news',
    'https://www.aljazeera.com/news/',
]

MODEL_PATH = "mistral-7b-v0.1.Q2_K.gguf"  # <- Replace with your model path
OUTPUT_FILE = "news.jsonl"

# ============ LLM SETUP ============

print("[*] Loading model...")
llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=4)  # Adjust n_threads as per your CPU

# ============ FUNCTIONS ============

def extract_article_urls(base_url):
    """Dummy extractor: In production, use newspaper3k's `build` or BeautifulSoup"""
    return [base_url]  # For demo, we just use base URL directly

def extract_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return {
            "title": article.title,
            "text": article.text,
            "url": url
        }
    except Exception as e:
        print(f"[!] Failed to extract {url}: {e}")
        return None

def summarize(text):
    prompt = f"Summarize the following news article:\n\n{text}\n\nSummary:"
    output = llm(prompt)
    return output['choices'][0]['text'].strip()

def save_news(data):
    with open(OUTPUT_FILE, "a", encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")

# ============ MAIN ============

def main():
    for site in WEBSITES:
        print(f"\n[*] Processing site: {site}")
        urls = extract_article_urls(site)

        for url in urls:
            article_data = extract_article(url)
            if not article_data or not article_data['text']:
                continue

            print(f"[+] Summarizing: {article_data['title']}")
            summary = summarize(article_data['text'])

            final_data = {
                "title": article_data['title'],
                "summary": summary,
                "url": article_data['url']
            }

            save_news(final_data)
            print(f"[✓] Saved: {article_data['title']}")


if __name__ == "__main__":
    main()
