# pipeline/generate.py

from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Load distilgpt2 once
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2")
text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

def generate_ad_post(subject: str, tone: str = "friendly", with_emoji: bool = True, max_length: int = 100) -> str:
    """
    Generate a marketing post based on input parameters.
    """
    emoji_clause = "Add emojis to make it more engaging." if with_emoji else ""
    prompt = f"Write a {tone} advertisement post in English about {subject}. {emoji_clause}".strip()

    result = text_generator(
    prompt,
    max_length=max_length,
    num_return_sequences=1,
    do_sample=True
)[0]["generated_text"].strip()
    
    return result
