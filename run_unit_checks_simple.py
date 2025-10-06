import json, os
from skillbot.nlp import tokenize, get_intent, analyze_sentiment
from skillbot.chatbot import SkillBot

repo = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
data_dir = os.path.join(repo, 'data')

print('Running simple unit checks')

# NLP checks
try:
    t = tokenize('Hello, world!')
    assert isinstance(t, tuple)
    assert any(x in t for x in ('hello', 'world'))
    print('test_tokenize_basic: PASS')
except Exception as e:
    print('test_tokenize_basic: FAIL', e)

try:
    assert get_intent('What courses do you have?') == 'course_info'
    assert get_intent('How do I apply for an internship?') == 'internship_info'
    assert get_intent('Hi there!') == 'greeting'
    print('test_get_intent_basic: PASS')
except Exception as e:
    print('test_get_intent_basic: FAIL', e)

try:
    assert analyze_sentiment('I love this course!') == 'positive'
    assert analyze_sentiment('I hate this') == 'negative'
    print('test_analyze_sentiment_basic: PASS')
except Exception as e:
    print('test_analyze_sentiment_basic: FAIL', e)

# SkillBot checks
try:
    with open(os.path.join(data_dir, 'faqs.json'), 'r', encoding='utf-8') as f:
        faqs = json.load(f)
    with open(os.path.join(data_dir, 'courses.json'), 'r', encoding='utf-8') as f:
        courses = json.load(f)
    with open(os.path.join(data_dir, 'internships.json'), 'r', encoding='utf-8') as f:
        internships = json.load(f)
    bot = SkillBot(faqs, courses, internships)
    print('Bot greet:', bot.greet())
    r1 = bot.handle_query('What courses do you have?')
    print('Bot response (courses):', r1)
    assert any(k in r1 for k in ('Python', 'Data Science', 'Web Development'))
    r2 = bot.handle_query('How do I apply for an internship?')
    print('Bot response (internship):', r2)
    assert 'intern' in r2.lower() or 'apply' in r2.lower()
    print('SkillBot tests: PASS')
except Exception as e:
    print('SkillBot tests: FAIL', e)
