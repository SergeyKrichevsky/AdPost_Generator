# app.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from pipeline.generate import generate_ad_post
from pipeline.summarize import load_summarizer, SUMMARIZER_MODELS
from pipeline.qc import evaluate_text_similarity
from pipeline.toxicity import is_toxic

# Page configuration
st.set_page_config(page_title="Ad Generator", layout="centered")

st.title("🎯 AI-Powered Ad Post Generator")
st.markdown("Generate engaging marketing posts with quality checks and safety filters.")

# User input form
with st.form("generator_form"):
    subject = st.text_input("🔤 What is your ad about?", value="coffee discount")
    tone = st.selectbox("🎨 Tone of voice", ["friendly", "formal", "funny"])
    model_choice = st.radio("⚡ Choose summarization model:", ["fast", "accurate"])
    submit = st.form_submit_button("🚀 Generate")

if submit:
    # Generate content
    with st.spinner("Generating content..."):
        ad_post = generate_ad_post(subject=subject, tone=tone, with_emoji=True)
        summarizer = load_summarizer(model_choice)
        score = evaluate_text_similarity(ad_post, subject, summarizer)
        toxic = is_toxic(ad_post)

    # Display results
    st.subheader("📢 Generated Post")
    st.write(ad_post.strip())

    st.subheader("📊 Quality & Safety Checks")
    st.write(f"**Relevance Score:** `{score:.2f}`")
    st.write(f"**Toxic Content:** {'❌ Yes' if toxic else '✅ No'}")
