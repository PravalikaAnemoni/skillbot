from skillbot.nlp import tokenize, get_intent, analyze_sentiment


def test_tokenize_basic():
    tokens = tokenize("Hello, world!")
    assert isinstance(tokens, tuple)
    # ensure at least one expected token is present
    assert any(t in tokens for t in ("hello", "world"))


def test_get_intent_basic():
    assert get_intent("What courses do you have?") == "course_info"
    assert get_intent("How do I apply for an internship?") == "internship_info"
    assert get_intent("Hi there!") == "greeting"


def test_analyze_sentiment_basic():
    assert analyze_sentiment("I love this course!") == "positive"
    assert analyze_sentiment("I hate this") == "negative"
