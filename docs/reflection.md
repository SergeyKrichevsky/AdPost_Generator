## 📐 Pipeline Architecture Summary

This project implements a modular, CPU-efficient generative content pipeline designed to create marketing posts while ensuring quality and ethical safety.

### 🔁 End-to-End Flow:

**Prompt ➝ Text Generator ➝ Summarizer (QC) ➝ Similarity Scorer ➝ Toxicity Filter ➝ Output**

### 🔧 Components:

- **Text Generator (`distilgpt2`)**  
  A lightweight autoregressive language model is used to generate ad-style content. We chose `distilgpt2` for its small size and fast performance on CPU.

- **Summarizer (`t5-small`, `facebook/bart-base`)**  
  Two summarization models are integrated to check the relevance of the generated post to the original prompt.  
  - `t5-small` is optimized for speed.  
  - `facebook/bart-base` provides higher accuracy.  
  This supports fast development iteration vs. deeper offline checks.

- **Semantic Relevance Scorer**  
  The `sentence-transformers` model (e.g., `all-MiniLM-L6-v2`) evaluates cosine similarity between the prompt and summary. This gives a rough but useful relevance score between 0 and 1.

- **Toxicity Filter**  
  The pipeline uses a two-stage filter:  
  1. **Keyword list** for fast toxic word checks  
  2. **HuggingFace `unitary/toxic-bert` classifier** for deeper ML-based detection  
  This prevents generation of unsafe or offensive content.

- **Automation (`schedule`)**  
  A lightweight scheduler runs automatic daily generation jobs. Prompts are randomly sampled from a curated list.

- **Interface (`Streamlit`)**  
  A user-friendly UI allows custom prompt input, tone selection, model choice, and interactive result review.

All modules are fully compatible with CPU environments and rely on pre-trained models from Hugging Face.

## ⚙️ **CPU Trade-offs**

In our project, we prioritized *accuracy and clarity* over performance speed. This decision is most evident in our summarization step, where we allow the user to select either a fast or accurate model. While accurate models (e.g., BART, Pegasus) produce higher-quality summaries, they require more computational time and memory. This trade-off affects responsiveness, especially in web interface or automated runs.

For local development, we used CPU inference to remain compatible with low-resource environments. However, running on CPU means slower generation and evaluation cycles compared to GPU-based deployment. In a production scenario, we would likely migrate to GPU-based backends or lightweight quantized models (e.g., DistilBERT) for better performance.

---

## ✅ **Quality Outcomes**

We integrated multiple layers of quality control:

* **Relevance Score**: Calculated using text similarity between the generated post and the original topic via embeddings + summarization. This helps detect "hallucinated" or off-topic generations.
* **Toxicity Check**: Filters content for harmful or offensive language using a classification model.
* **User Control**: Users can specify tone and summarization depth to tailor content.

However, our evaluation is **limited by the absence of a gold-standard reference**, which restricts the use of automatic metrics like BLEU or ROUGE. Manual inspection or A/B testing would be more reliable in future iterations.

---

## ⚠️ **Ethical Challenges**

We addressed several ethical concerns:

1. **Toxicity Filtering** – We use automated detection to block harmful language, but no filter is perfect. False negatives or positives may still occur.
2. **Bias in Models** – Pretrained language models may carry social biases (e.g., gender, race, stereotypes). This could reflect in generated content depending on the subject.
3. **Automation Risks** – Automating ad generation raises concerns of misinformation, spam, or manipulation. While this project is educational, deploying such systems at scale requires clear safeguards and human-in-the-loop mechanisms.
