"""
SkillBot Streamlit Dashboard
Provides a user interface for interacting with the chatbot and viewing analytics
"""
import streamlit as st
import sys
import os
import json
import plotly.express as px
import pandas as pd
from datetime import datetime

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from skillbot.chatbot import SkillBot

# Page config
st.set_page_config(
    page_title="SkillBot Dashboard",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'analytics' not in st.session_state:
    st.session_state.analytics = {
        'queries_count': 0,
        'intent_distribution': {},
        'sentiment_scores': [],
        'popular_topics': {}
    }

# Load data
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

@st.cache_resource
def load_bot():
    with open(os.path.join(DATA_DIR, 'faqs.json'), 'r', encoding='utf-8') as f:
        faqs = json.load(f)
    with open(os.path.join(DATA_DIR, 'courses.json'), 'r', encoding='utf-8') as f:
        courses = json.load(f)
    with open(os.path.join(DATA_DIR, 'internships.json'), 'r', encoding='utf-8') as f:
        internships = json.load(f)
    return SkillBot(faqs, courses, internships)

bot = load_bot()

# Sidebar for analytics
st.sidebar.title("SkillBot Analytics")

# Query count
st.sidebar.metric("Total Queries", st.session_state.analytics['queries_count'])

# Intent distribution
if st.session_state.analytics['intent_distribution']:
    st.sidebar.subheader("Intent Distribution")
    intent_df = pd.DataFrame({
        'Intent': list(st.session_state.analytics['intent_distribution'].keys()),
        'Count': list(st.session_state.analytics['intent_distribution'].values())
    })
    st.sidebar.plotly_chart(px.pie(intent_df, values='Count', names='Intent', title='Intent Distribution'))

# Sentiment analysis
if st.session_state.analytics['sentiment_scores']:
    st.sidebar.subheader("Sentiment Analysis")
    sentiment_df = pd.DataFrame({
        'Query': range(len(st.session_state.analytics['sentiment_scores'])),
        'Sentiment': st.session_state.analytics['sentiment_scores']
    })
    st.sidebar.plotly_chart(px.line(sentiment_df, x='Query', y='Sentiment', title='Sentiment Trend'))

# Main chat interface
st.title("🤖 SkillBot - Your Educational Assistant")

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Update analytics
    st.session_state.analytics['queries_count'] += 1
    
    # Get bot response
    response = bot.handle_query(user_input)
    
    # Add to chat history
    st.session_state.chat_history.append({"user": user_input, "bot": response})
    
    # Update analytics
    intent = bot.get_intent(user_input)
    sentiment = bot.get_sentiment(user_input)
    
    if intent in st.session_state.analytics['intent_distribution']:
        st.session_state.analytics['intent_distribution'][intent] += 1
    else:
        st.session_state.analytics['intent_distribution'][intent] = 1
    
    st.session_state.analytics['sentiment_scores'].append(sentiment)

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(message["user"])
    with st.chat_message("assistant"):
        st.write(message["bot"])

# Course catalog
st.sidebar.subheader("Quick Links")
if st.sidebar.button("View Course Catalog"):
    st.sidebar.json(bot.courses)

# Internship opportunities
if st.sidebar.button("View Internships"):
    st.sidebar.json(bot.internships)

# FAQ section
if st.sidebar.button("View FAQs"):
    st.sidebar.json(bot.faqs)
