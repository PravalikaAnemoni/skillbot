# SkillBot: AI Chatbot for SkillHigh Edtech Platform

## Overview
SkillBot is an AI-powered chatbot designed for SkillHigh, assisting students with FAQs, course and internship guidance, onboarding, and more. It uses NLP and ML to understand queries and provide engaging, accurate responses.

## Features
- Conversational AI with intent recognition
- FAQ, course, internship, and certification info
- Greeting and onboarding flow
- REST API (Flask)
- Streamlit demo interface
- Contextual chat memory
- Sentiment analysis (TextBlob)
- Multilingual support (English, placeholder for Hindi/Tamil)
- Analytics dashboard (basic usage stats)

## Folder Structure
- `skillbot/` - Core chatbot logic and NLP utilities
- `data/` - Dummy FAQ, course, and internship data
- `api/` - REST API (Flask)
- `demo/` - Streamlit demo app
- `dashboard/` - Analytics scripts

## Model Architecture & Libraries
- Python 3.8+
- spaCy (NLP)
- TextBlob (Sentiment analysis)
- Flask (API)
- Streamlit (Demo UI)

## Data Sources & Preprocessing
- Dummy data in `data/` folder
- Preprocessing handled in code (simple keyword-based intent)

## Reasoning Behind Choices
- spaCy: Lightweight NLP, easy to extend
- TextBlob: Quick sentiment analysis
- Flask/Streamlit: Fast prototyping and integration

## Limitations & Scope for Improvement
- Intent recognition is keyword-based (can be replaced with ML model)
- Multilingual support is a placeholder
- Analytics are basic; can be expanded
- No persistent database (can be added)

## Optimizations

- String processing has been optimized: the project now tokenizes and normalizes user input (lemmatization and lowercasing) using a cached tokenizer. This reduces repeated substring scans, improves intent detection accuracy, and speeds up repeated queries by reusing cached token tuples.
   - See `skillbot/nlp.py` for the tokenizer and `skillbot/chatbot.py` for how intents use token sets instead of raw substring matching.

## How to Run
1. Install dependencies:
   ```bash
   pip install flask streamlit spacy textblob
   ```
2. Run API:
   ```bash
   cd api
   python main.py
   ```
3. Run Streamlit demo:
   ```bash
   cd demo
   streamlit run app.py
   ```

## Integration
- API exposes `/chat` endpoint for integration with websites or LMS

## Contact
For questions, reach out to SkillHigh support or open an issue.
