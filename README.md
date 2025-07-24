# 🚀 GenAI Content Generator: Ethical Marketing Post Creator

## 🧠 Project Summary

An automated content generation system that creates marketing-style posts from trending topics, evaluates relevance, filters for toxicity, and logs results. All modules run on CPU. Designed for fast demo and future extensibility.

---

## 📦 Core Modules & Pipeline

```
Prompt → Text Generator → Summarizer (Relevance Score) → Toxicity Filter → Result Log
```

### ✅ Implemented Features:

* **Text Generation** with `distilgpt2`
* **Summarization-based Evaluation** using `t5-small` and `facebook/bart-base`
* **Toxicity Detection** (heuristics + classifier)
* **Daily Automation** using `schedule`
* **Streamlit Interface** for manual prompt testing
* **Evaluation Dashboard** (average score, outliers)

---

## 🧪 Evaluation

* Relevance scoring via **cosine similarity** between generated summary and topic prompt
* No BLEU/ROUGE: no reference samples → not meaningful for this task
* Average similarity score on test set: **0.56**

---

## 🔄 Automation

Runs `runner.py` once per day (or on demand) and appends:

* Timestamp
* Input topic
* Generated post
* Toxicity status
* Relevance score

---

## ✅ Ethical Filtering

Two-stage:

1. Heuristic keyword check
2. `unitary/toxic-bert` classifier for borderline cases

---

## 🚧 Future Improvements

* Add **image generation module** (e.g. thumbnail or icon for post)
* External data for topics: live scraping or APIs (e.g. Google Trends)
* Multi-lingual support
* Hosting on Hugging Face Spaces or deployment to server

---

## ▶️ How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# One-time test
python -m automation.runner

# Daily automation
python -m automation.scheduler

# Run Streamlit UI
streamlit run interface/app.py
```

---

## 👤 Author: Sergey Krichevsky (Bootcamp Hackathon)

## 🔑 Keywords

Generative AI, Streamlit, Hugging Face, NLP, Filtering, Automation, Transformers, Toxicity Detection, Evaluation, Ethical AI
