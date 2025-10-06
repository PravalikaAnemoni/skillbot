from skillbot.nlp import tokenize, get_intent, analyze_sentiment
from skillbot.chatbot import SkillBot
import json, os

print('Running quick local checks...')
print('Tokens for "Hello world":', tokenize('Hello world'))
print('Intent for "What courses do you have?":', get_intent('What courses do you have?'))
print('Sentiment for "I love this":', analyze_sentiment('I love this'))

# Create bot
repo = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
data_dir = os.path.join(repo, 'data')
with open(os.path.join(data_dir, 'faqs.json'), 'r', encoding='utf-8') as f:
    faqs = json.load(f)
with open(os.path.join(data_dir, 'courses.json'), 'r', encoding='utf-8') as f:
    courses = json.load(f)
with open(os.path.join(data_dir, 'internships.json'), 'r', encoding='utf-8') as f:
    internships = json.load(f)

bot = SkillBot(faqs, courses, internships)
print('Bot greet:', bot.greet())
print('Bot response (courses):', bot.handle_query('What courses do you have?'))
print('Bot response (internship):', bot.handle_query('How do I apply for an internship?'))
