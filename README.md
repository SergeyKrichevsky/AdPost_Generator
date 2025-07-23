# AdPost-Gen 📝🤖

**AdPost-Gen** is a promotional post generator for social media.  
It uses a lightweight generative language model (LLM) to produce text, applies summarization-based quality control, and performs ethical filtering. A simple UI is provided via Streamlit.

---

## 📌 Project Description

- Generates short promotional posts (~50–100 tokens) based on a given topic
- Allows users to select tone (`formal`, `friendly`, `funny`) and emoji preference
- Uses summarization and semantic similarity for quality checking
- Applies basic and optional ML-based ethical filtering (toxicity)
- Interactive UI built with Streamlit

---

## 🧾 User Input

- **Subject of the ad** – short topic like `"discount on coffee"`, `"new online course"`
- **Tone** – one of: `formal`, `friendly`, `funny`
- **Emoji** – `with emoji` or `no emoji`
- **Language** – English (only for prototype)

Prompt example:
> *"Write a funny advertisement post in English about a discount on coffee. Add emojis to make it more engaging."*

---

## 🧱 Pipeline Architecture

The system follows this pipeline:

1. **User Input**  
   User provides:  
   - subject of the ad  
   - tone (formal/friendly/funny)  
   - emoji option  
   - language (English)

2. **Prompt Construction**  
   The inputs are combined into a structured prompt.

3. **Text Generation**  
   The prompt is passed to `distilgpt2` via Hugging Face `transformers.generate()`.

4. **Summarization-Based Quality Control**  
   The generated output is summarized using `t5-small` or `bart-base`, and its relevance to the original prompt is measured using cosine similarity.

5. **Ethical Filtering**  
   The generated post is checked for toxic content using a basic keyword filter and optionally a `text-classification` pipeline.

6. **Final Output via UI**  
   The clean, high-quality ad post is displayed to the user through a Streamlit web interface.

---

## ⚙️ Tech Stack

| Module             | Model / Library                   | Purpose                    |
|--------------------|-----------------------------------|----------------------------|
| Text Generation    | `distilgpt2`, Hugging Face         | LLM-based generation       |
| Summarization      | `t5-small`, `bart-base`           | Relevance check            |
| Embeddings         | `all-MiniLM-L6-v2`, Sentence-Transformers | Semantic similarity |
| Filtering          | Keywords + `text-classification`  | Toxic content detection    |
| UI                 | Streamlit                         | Input and display          |

---

## 🚀 How to Run

```bash
git clone https://github.com/yourname/adpost-gen.git
cd adpost-gen
pip install -r requirements.txt
streamlit run app.py
```

Runs on CPU (no GPU required). Can be launched in Google Colab or locally.

---

## ✅ MVP Features

- Prompt-driven text generation
- Summarization-based quality control
- Basic toxicity filtering
- Streamlit UI for user interaction

---

## 🧪 Optional Enhancements

- Advanced ML-based toxicity classifier
- Evaluation metrics (BLEU, ROUGE)
- Scheduled automatic generation

---

## 👤 Author

Sergey Krichevsky — participant in the Generative AI Bootcamp @ Developers Institute

---
