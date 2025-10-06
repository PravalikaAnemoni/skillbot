"""NLP utilities for SkillBot.

Provides a small, efficient tokenization helper and lightweight utilities
used by the demo chatbot. Tokenization is cached (LRU) to avoid
re-parsing repeated user messages.

Design goals:
- Use spaCy's tokenizer/lemmatizer when available (en_core_web_sm).
- Fall back to a fast regex-based tokenizer if spaCy isn't available.
- Cache tokenization results for repeated queries.
"""

from functools import lru_cache
import re
from typing import Literal, Tuple

import spacy
from textblob import TextBlob


# Try to load a full spaCy model; fall back to a blank English tokenizer if not
# available. This keeps behavior predictable in minimal environments.
try:
    _nlp = spacy.load("en_core_web_sm")
except Exception:
    _nlp = spacy.blank("en")


@lru_cache(maxsize=1024)
def tokenize(text: str, use_lemmas: bool = True) -> Tuple[str, ...]:
    """Return a tuple of normalized tokens for `text`.

    - Uses spaCy if available to perform tokenization and lemmatization.
    - Falls back to a regex word tokenizer on error.
    - Results are cached (LRU) to speed up repeated identical queries.

    Returns a tuple (so results are hashable and cacheable).
    """
    if not text:
        return tuple()

    # Normalize whitespace
    text = text.strip()
    try:
        doc = _nlp(text)
        tokens = []
        for tok in doc:
            if tok.is_space or tok.is_punct:
                continue
            if use_lemmas:
                # spaCy may produce "-PRON-" or empty lemma for some tokens; fall back
                lemma = (tok.lemma_ or tok.text).lower()
                tokens.append(lemma)
            else:
                tokens.append(tok.text.lower())
        return tuple(tokens)
    except Exception:
        # Safe regex fallback: split on word boundaries
        return tuple(re.findall(r"\b\w+\b", text.lower()))


def get_intent(text: str) -> str:
    """Tiny intent heuristic optimized to use token sets where possible.

    Returns one of: 'greeting', 'gratitude', 'course_info', 'internship_info',
    'pricing', 'faq', 'fallback'.
    """
    txt = (text or "").lower()
    tokens = set(tokenize(txt))

    # Multi-word checks (phrases) — keep substring check for these
    if any(phrase in txt for phrase in ["how are you", "how r u", "how is it going"]):
        return "greeting"

    # Single-word intent checks via token set (fast)
    if tokens & {"hi", "hello", "hey", "greetings", "helo", "hlo", "hai"}:
        return "greeting"
    if tokens & {"thanks", "thank", "thankyou", "thx", "appreciate", "grateful"}:
        return "gratitude"
    if "course" in tokens or "courses" in tokens or "learn" in tokens or "program" in tokens:
        return "course_info"
    if "internship" in tokens or "intern" in tokens or "internships" in tokens:
        return "internship_info"
    if "price" in tokens or "cost" in tokens or "fees" in tokens or "pricing" in tokens:
        return "pricing"
    if "faq" in tokens or "question" in tokens or "questions" in tokens:
        return "faq"

    return "fallback"


def analyze_sentiment(text: str) -> Literal["positive", "neutral", "negative"]:
    """Return a coarse sentiment label using TextBlob polarity.

    Wrapped here so the rest of the app can call a single utility.
    """
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
    except Exception:
        return "neutral"

    if polarity > 0.2:
        return "positive"
    if polarity < -0.2:
        return "negative"
    return "neutral"


def translate_text(text: str, target_lang: str = "en") -> str:
    """Translate `text` to `target_lang` using TextBlob with a safe fallback.

    TextBlob's translate uses an online service and may raise network or encoding
    related exceptions. In those cases we return the original text so the app can
    continue gracefully.
    """
    try:
        if not text:
            return text
        blob = TextBlob(text)
        return str(blob.translate(to=target_lang))
    except Exception:
        return text
