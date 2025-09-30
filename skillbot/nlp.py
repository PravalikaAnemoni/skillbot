"""
NLP and ML utilities for SkillBot
Uses spaCy for intent recognition and sentiment analysis (placeholder for real model)
"""
import spacy
from textblob import TextBlob
"""NLP and ML utilities for SkillBot.

Uses spaCy for intent recognition and TextBlob for simple sentiment/translation in the
demo. These are lightweight placeholders — replace with a proper model/service for
production.
"""
from typing import Literal
import spacy
from textblob import TextBlob

nlp = spacy.blank("en")


def get_intent(text: str) -> str:
    """Very small intent heuristic for demo purposes."""
    text = text.lower()
    if "course" in text:
        return "course_info"
    if "internship" in text:
        return "internship_info"
    if "price" in text or "cost" in text:
        return "pricing"
    if "faq" in text or "question" in text:
        return "faq"
    if "thank" in text:
        return "gratitude"
    if any(greet in text for greet in ["hi", "hello", "hey"]):
        return "greeting"
    return "fallback"


def analyze_sentiment(text: str) -> Literal["positive", "neutral", "negative"]:
    """Return a coarse sentiment label using TextBlob polarity."""
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
    except Exception:
        # If sentiment analysis fails, default to neutral
        return "neutral"

    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"


def translate_text(text: str, target_lang: str = "en") -> str:
    """Translate `text` to `target_lang` using TextBlob with a safe fallback.

    TextBlob's translate uses an online service and may raise network or encoding
    related exceptions. In those cases we return the original text so the app can
    continue gracefully.
    """
    try:
        # Guard against empty input
        if not text:
            return text

        blob = TextBlob(text)
        translated = blob.translate(to=target_lang)
        # Ensure we return a str instance and avoid any encoding-related errors here
        return str(translated)
    except UnicodeEncodeError:
        # Windows console or internal encoding issues — fall back to original
        return text
    except Exception:
        # Network errors, rate limits, or other TextBlob exceptions — return original
        return text
