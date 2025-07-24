# automation/runner.py

import sys
import os

# Add project root to sys.path to allow 'pipeline' import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import random
from datetime import datetime
from pipeline.generate import generate_ad_post
from pipeline.qc import evaluate_text_similarity
from pipeline.summarize import load_summarizer, SUMMARIZER_MODELS
from pipeline.toxicity import is_toxic
import os



def run_once():
    # Load subjects
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'subjects.csv')
    csv_path = os.path.abspath(csv_path)
    df = pd.read_csv(csv_path)

    subject = random.choice(df["subject"].tolist())

    # Generate ad post
    post = generate_ad_post(subject, tone="friendly", with_emoji=True)

    # Load summarizer for quality check
    summarizer = load_summarizer(SUMMARIZER_MODELS["accurate"])

    # Toxicity and relevance check
    toxic = is_toxic(post)
    relevance = evaluate_text_similarity(post, subject, summarizer)

    # Prepare log row
    result = {
        "timestamp": datetime.utcnow().isoformat(),
        "subject": subject,
        "generated_post": post,
        "is_toxic": toxic,
        "relevance_score": round(relevance, 3)
    }

    # Append to automation log
    # Resolve absolute path to log file
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'generated_log.csv'))

    exists = os.path.exists(output_path)
    pd.DataFrame([result]).to_csv(output_path, mode="a", header=not exists, index=False)

    print(f"✅ Generated post logged at {result['timestamp']} — {subject}")

if __name__ == "__main__":
    run_once()
