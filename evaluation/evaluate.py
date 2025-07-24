# evaluation/evaluate.py

import os
import pandas as pd
from pipeline.generate import generate_ad_post
from pipeline.summarize import load_summarizer, SUMMARIZER_MODELS
from pipeline.qc import evaluate_text_similarity
from pipeline.toxicity import is_toxic

# Load test subjects
data_path = os.path.join("data", "subjects.csv")
df = pd.read_csv(data_path)

# Select summarization model for quality check (e.g., accurate)
summarizer = load_summarizer(SUMMARIZER_MODELS["accurate"])

# Prepare output storage
results = []

for i, row in df.iterrows():
    subject = row["subject"]

    # Generate advertisement post
    generated = generate_ad_post(subject, tone="friendly", with_emoji=True)

    # Toxicity check
    toxic = is_toxic(generated)

    # Relevance check
    relevance_score = evaluate_text_similarity(generated, subject, summarizer)

    # Save result
    results.append({
        "subject": subject,
        "generated_post": generated,
        "is_toxic": toxic,
        "relevance_score": round(relevance_score, 3)
    })

# Save to CSV
output_df = pd.DataFrame(results)
output_df.to_csv("evaluation/results.csv", index=False)
print("✅ Evaluation complete. Results saved to evaluation/results.csv")
