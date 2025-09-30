"""
SkillBot Analytics Dashboard (Streamlit)
Shows usage stats, most asked questions, and sentiment trends
"""
import streamlit as st
import json
import os
from collections import Counter

st.set_page_config(page_title="SkillBot Analytics Dashboard", page_icon="📊", layout="wide")
st.title("SkillBot 📊 Analytics Dashboard")

# Load chat history
HIST_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'demo', 'chat_history.json'))
if os.path.exists(HIST_PATH):
    with open(HIST_PATH, 'r', encoding='utf-8') as f:
        history = json.load(f)
else:
    history = []

# Most asked questions
questions = [h['user'] for h in history if 'user' in h]
most_asked = Counter(questions).most_common(5)

st.subheader("Top 5 Most Asked Questions")
if most_asked:
    for q, count in most_asked:
        st.markdown(f"- **{q}** ({count} times)")
else:
    st.info("No questions found yet.")

# Sentiment trends (if available)
sentiments = []
for h in history:
    if 'sentiment' in h:
        sentiments.append(h['sentiment'])
if sentiments:
    st.subheader("Sentiment Trends")
    st.bar_chart(Counter(sentiments))
else:
    st.info("No sentiment data available.")

st.markdown("---")
st.markdown("_Dashboard updates in real-time as users interact with SkillBot._")
