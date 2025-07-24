# 🏠 Project Architecture: AI-Powered Ad Post Generator

## 📁 Project Structure

```
AdPost_Generator/
├── interface/              # Streamlit user interface
│   └── app.py              # Main Streamlit app
├── pipeline/               # Core logic modules
│   ├── __init__.py
│   ├── generate.py         # Post generation logic
│   ├── summarize.py        # Summarizer loading and models
│   ├── qc.py               # Quality control (relevance metric)
│   └── toxicity.py         # Toxicity detection
├── evaluation/             # Evaluation tools and reports
│   ├── evaluate.py
│   ├── metrics.py
│   ├── results.csv         # Output of evaluation runs
│   └── view_results.py     # Utility to render results
├── automation/             # Automation scripts and schedulers
│   ├── generated_log.csv   # Log from Scheduler Functionality
│   ├── fetch_topics.py     # (optional) trending topic fetcher
│   ├── scheduler.py        # Scheduler script
│   └── runner.py           # Script to run generation + checks
├── data/
│   └── subjects.csv        # Set of predefined subjects
├── docs/
│   └── reflection.md       # Developer reflection (optional)
├── README.md
├── requirements.txt
└── architecture.md         # This file
```

## 🤠 Components

* **interface/app.py** – Streamlit interface that collects input and displays output.
* **pipeline/** – Contains modular, testable logic for each step:

  * `generate_ad_post()` creates the ad.
  * `evaluate_text_similarity()` scores relevance.
  * `is_toxic()` detects harmful content.
  * `load_summarizer()` loads summarizer models.
* **evaluation/** – Code to evaluate and report on quality of generated content.
* **automation/** – Includes scheduled runs and logging for automatic generation.

## ⌚️ Workflow

1. **Subject Selection**: Randomly from `subjects.csv` or manually in UI.
2. **Generation**: Using prompt and selected parameters.
3. **Quality Checks**:

   * Similarity to subject (Relevance)
   * Toxicity check
4. **Result**: Display in Streamlit / append to CSV log
5. **Automation**: Optional scheduled run using `scheduler.py`

## ✨ Future Enhancements

* Trending topics fetcher (SerpAPI, PyTrends)
* Image generation (DALLE, Midjourney API)
* Admin analytics dashboard
* Model fine-tuning / personalization
