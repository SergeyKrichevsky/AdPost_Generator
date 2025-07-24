# pipeline/summarize.py

from transformers import pipeline

# Mapping from user choice to model names
SUMMARIZER_MODELS = {
    "fast": "t5-small",
    "accurate": "facebook/bart-base"
}

def load_summarizer(mode: str = "fast"):
    """
    Load a summarization pipeline using the specified model.

    Parameters:
    - mode (str): Either "fast" or "accurate"

    Returns:
    - HuggingFace pipeline: The loaded summarizer
    """
    model_name = SUMMARIZER_MODELS.get(mode, "t5-small")
    summarizer = pipeline("summarization", model=model_name)
    return summarizer
