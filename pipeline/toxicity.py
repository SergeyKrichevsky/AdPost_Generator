# pipeline/toxicity.py

from transformers import pipeline

# List of known toxic words for fast keyword-based filtering
BAD_WORDS = [
    "idiot", "hate", "kill", "stupid", "dumb", "fool", "moron", "retard",
    "trash", "ugly", "shut up", "bastard", "sucks", "disgusting", "racist"
]

def contains_bad_words(text: str) -> bool:
    """
    Check if the text contains known toxic keywords.

    This is a fast heuristic filter to catch obvious toxicity before
    running a heavy classification model. Helps reduce computation time.

    Parameters:
    - text (str): Input text

    Returns:
    - bool: True if any toxic keyword is found
    """
    text = text.lower()
    return any(bad_word in text for bad_word in BAD_WORDS)

# Load lightweight toxicity classifier from HuggingFace Hub
toxicity_classifier = pipeline("text-classification", model="unitary/toxic-bert", top_k=None)

def is_toxic(text: str, threshold: float = 0.5) -> bool:
    """
    Evaluate if a text is toxic using a two-stage filter:
    1. Fast keyword-based scan
    2. Deep classification with a pretrained toxicity model

    The goal is to reduce computational load by avoiding model calls
    for clearly toxic content caught by simple rules.

    Parameters:
    - text (str): Generated content
    - threshold (float): Minimum score to consider output toxic

    Returns:
    - bool: True if text is considered toxic, False otherwise
    """

    # Stage 1: Fast keyword match
    if contains_bad_words(text):
        return True

    # Stage 2: ML-based classification
    results = toxicity_classifier(text)[0]
    for item in results:
        label = item["label"].lower()
        score = item["score"]
        if "toxic" in label and score > threshold:
            return True

    return False
