# Changelog

All notable changes to this project will be documented in this file.

## added
- Refactor: optimize string tokenization into cached tokens; use tokenization for intent detection.
- Add: centralized tokenizer and intent helpers in `skillbot/nlp.py` (LRU cache + spaCy fallback).
- Refactor: `skillbot/chatbot.py` updated to use token sets and cached intent lookups (faster, more robust).
- Add: `scripts/setup_env.ps1` to automate virtualenv creation, dependency install, spaCy model and TextBlob corpora downloads.
- Add: unit tests for NLP utilities and core chatbot behaviors in `tests/`.
