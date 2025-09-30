"""
SkillBot Streamlit Demo Interface
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import json
from skillbot.chatbot import SkillBot
from skillbot.nlp import analyze_sentiment, get_intent

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
with open(os.path.join(DATA_DIR, 'faqs.json'), 'r', encoding='utf-8') as f:
    faqs = json.load(f)
with open(os.path.join(DATA_DIR, 'courses.json'), 'r', encoding='utf-8') as f:
    courses = json.load(f)
with open(os.path.join(DATA_DIR, 'internships.json'), 'r', encoding='utf-8') as f:
    internships = json.load(f)

# Multilingual support
LANGUAGES = {"English": "en", "Hindi": "hi"}
st.set_page_config(page_title="SkillBot - Your SkillHigh Guide", page_icon="🤖", layout="wide")
st.title("SkillBot 🤖 - Your SkillHigh Guide")
st.sidebar.header("Onboarding & Quick Start")
st.sidebar.markdown("Welcome to SkillHigh! Ask me anything about courses, internships, or SkillHigh policies.")
st.sidebar.markdown("**Sample Questions:**")
st.sidebar.markdown("- What courses are available?\n- How do I apply for an internship?\n- Tell me about SkillHigh onboarding.")
st.sidebar.markdown("---")
language = st.sidebar.selectbox("Language", list(LANGUAGES.keys()), index=0)

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if 'bot' not in st.session_state or st.session_state.get('bot_language') != language:
    st.session_state['bot'] = SkillBot(faqs, courses, internships, language=LANGUAGES[language])
    st.session_state['bot_language'] = language
bot = st.session_state['bot']

user_input = st.text_input("Type your message:", "", key="user_input")
send_button = st.button("Send", key="send_button")

# Display chat history with contextual memory and sentiment
for entry in st.session_state['chat_history']:
    sender = entry.get('sender', 'user')
    message = entry.get('message', '')
    sentiment = entry.get('sentiment', '')
    if sender == "user":
        # User chat bubble: purple gradient
        st.markdown(f"<div style='text-align:right; background: linear-gradient(90deg, #a770ef 0%, #cf8bf3 100%); color: white; padding:10px; border-radius:16px; margin-bottom:6px; font-size:1.1em;'>👤 <b>You:</b> {message}</div>", unsafe_allow_html=True)
    """
    SkillBot Streamlit Demo Interface
    """

    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import streamlit as st
    import json
    from skillbot.chatbot import SkillBot
    from skillbot.nlp import analyze_sentiment

    DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    with open(os.path.join(DATA_DIR, 'faqs.json'), 'r', encoding='utf-8') as f:
        faqs = json.load(f)
    with open(os.path.join(DATA_DIR, 'courses.json'), 'r', encoding='utf-8') as f:
        courses = json.load(f)
    with open(os.path.join(DATA_DIR, 'internships.json'), 'r', encoding='utf-8') as f:
        internships = json.load(f)

    # Multilingual support
    LANGUAGES = {"English": "en", "Hindi": "hi"}
    st.set_page_config(page_title="SkillBot - Your SkillHigh Guide", page_icon="🤖", layout="wide")
    st.title("SkillBot 🤖 - Your SkillHigh Guide")
    st.sidebar.header("Onboarding & Quick Start")
    st.sidebar.markdown("Welcome to SkillHigh! Ask me anything about courses, internships, or SkillHigh policies.")
    st.sidebar.markdown("**Sample Questions:**")
    st.sidebar.markdown("- What courses are available?\n- How do I apply for an internship?\n- Tell me about SkillHigh onboarding.")
    st.sidebar.markdown("---")
    language = st.sidebar.selectbox("Language", list(LANGUAGES.keys()), index=0)

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    if 'bot' not in st.session_state or st.session_state.get('bot_language') != language:
        st.session_state['bot'] = SkillBot(faqs, courses, internships, language=LANGUAGES[language])
        st.session_state['bot_language'] = language
    bot = st.session_state['bot']

    user_input = st.text_input("Type your message:", "", key="user_input")
    send_button = st.button("Send", key="send_button")

    # Display chat history with contextual memory and sentiment
    for entry in st.session_state['chat_history']:
        sender = entry.get('sender', 'user')
        message = entry.get('message', '')
        sentiment = entry.get('sentiment', '')
        if sender == "user":
            # User chat bubble: purple gradient
            st.markdown(f"<div style='text-align:right; background: linear-gradient(90deg, #a770ef 0%, #cf8bf3 100%); color: white; padding:10px; border-radius:16px; margin-bottom:6px; font-size:1.1em;'>👤 <b>You:</b> {message}</div>", unsafe_allow_html=True)
        else:
            # Bot chat bubble: blue gradient
            st.markdown(f"<div style='text-align:left; background: linear-gradient(90deg, #43e97b 0%, #38f9d7 100%); color: #222; padding:10px; border-radius:16px; margin-bottom:6px; font-size:1.1em;'>🤖 <b>SkillBot:</b> {message} <span style='font-size:0.9em; color:#555;'>({sentiment})</span></div>", unsafe_allow_html=True)

    if send_button and user_input:
        # Multilingual support: translate user input to English if Hindi selected
        if language == "Hindi":
            try:
                from skillbot.nlp import translate_text
                user_text = translate_text(user_input, target_lang="en")
            except Exception:
                user_text = user_input
        else:
            user_text = user_input
        # Sentiment analysis
        sentiment = analyze_sentiment(user_text)
        # Contextual memory: pass previous user messages
        context = [e['message'] for e in st.session_state['chat_history'] if e.get('sender') == 'user']
        response = bot.handle_query(user_text, sentiment=sentiment)
        # Always translate bot response to Hindi if Hindi selected
        if language == "Hindi":
            try:
                from skillbot.nlp import translate_text
                response = translate_text(response, target_lang="hi")
            except Exception:
                pass
        # Save user message in original language for display
        st.session_state['chat_history'].append({'sender': 'user', 'message': user_input, 'sentiment': sentiment})
        st.session_state['chat_history'].append({'sender': 'bot', 'message': response, 'sentiment': sentiment})
        # Save history to file for analytics (include sentiment)
        hist_data = [
            {'user': e['message'], 'sentiment': e['sentiment']} 
            for e in st.session_state['chat_history'] if e.get('sender') == 'user'
        ]
        hist_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chat_history.json'))
        with open(hist_path, 'w', encoding='utf-8') as f:
            json.dump(hist_data, f, ensure_ascii=False, indent=2)

        st.rerun()

    # --- Dashboard/Analytics Section ---
    import collections
    st.markdown("---")
    st.subheader("📊 Chatbot Usage Analytics")
    hist_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chat_history.json'))
    if os.path.exists(hist_path):
        with open(hist_path, 'r', encoding='utf-8') as f:
            history = json.load(f)
    else:
        history = []

    # Most asked questions
    questions = [h['user'] for h in history if 'user' in h]
    most_asked = collections.Counter(questions).most_common(5)
    st.markdown("**Top 5 Most Asked Questions:**")
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
        st.markdown("**Sentiment Trends:**")
        st.bar_chart(collections.Counter(sentiments))
    else:
        st.info("No sentiment data available.")
