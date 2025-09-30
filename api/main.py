"""
SkillBot REST API using Flask
Exposes chatbot responses via /chat endpoint
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify
import json
from skillbot.chatbot import SkillBot

app = Flask(__name__)

# Load dummy data using absolute paths
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
with open(os.path.join(DATA_DIR, 'faqs.json'), 'r', encoding='utf-8') as f:
    faqs = json.load(f)
with open(os.path.join(DATA_DIR, 'courses.json'), 'r', encoding='utf-8') as f:
    courses = json.load(f)
with open(os.path.join(DATA_DIR, 'internships.json'), 'r', encoding='utf-8') as f:
    internships = json.load(f)

bot = SkillBot(faqs, courses, internships)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get('query', '')
    response = bot.handle_query(query)
    return jsonify({'response': response})

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify({'response': bot.greet()})

# Homepage endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to SkillBot API</h1>
    <p>Use <b>/chat</b> (POST) for chatbot queries.<br>
    Use <b>/greet</b> (GET) for a greeting.</p>''', 200

# List all courses
@app.route('/courses', methods=['GET'])
def courses_endpoint():
    return jsonify(courses)

# List all internships
@app.route('/internships', methods=['GET'])
def internships_endpoint():
    return jsonify(internships)

# List all FAQs
@app.route('/faq', methods=['GET'])
def faq_endpoint():
    """
    Clean, single-copy Flask API for SkillBot.
    """

    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from flask import Flask, request, jsonify
    import json
    from skillbot.chatbot import SkillBot

    app = Flask(__name__)

    # Load dummy data using absolute paths
    DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    with open(os.path.join(DATA_DIR, 'faqs.json'), 'r', encoding='utf-8') as f:
        faqs = json.load(f)
    with open(os.path.join(DATA_DIR, 'courses.json'), 'r', encoding='utf-8') as f:
        courses = json.load(f)
    with open(os.path.join(DATA_DIR, 'internships.json'), 'r', encoding='utf-8') as f:
        internships = json.load(f)

    bot = SkillBot(faqs, courses, internships)


    @app.route('/chat', methods=['POST'])
    def chat():
        data = request.get_json(silent=True) or {}
        query = data.get('query', '')
        response = bot.handle_query(query)
        return jsonify({'response': response})


    @app.route('/greet', methods=['GET'])
    def greet():
        return jsonify({'response': bot.greet()})


    @app.route('/', methods=['GET'])
    def home():
        return '''<h1>Welcome to SkillBot API</h1>
        <p>Use <b>/chat</b> (POST) for chatbot queries.<br>
        Use <b>/greet</b> (GET) for a greeting.</p>''', 200


    @app.route('/courses', methods=['GET'])
    def courses_endpoint():
        return jsonify(courses)


    @app.route('/internships', methods=['GET'])
    def internships_endpoint():
        return jsonify(internships)


    @app.route('/faq', methods=['GET'])
    def faq_endpoint():
        return jsonify(faqs)


    @app.route('/history', methods=['GET'])
    def history_endpoint():
        return jsonify({'history': bot.get_history()})


    @app.route('/sentiment', methods=['POST'])
    def sentiment_endpoint():
        data = request.get_json(silent=True) or {}
        query = data.get('query', '')
        from skillbot.nlp import analyze_sentiment
        sentiment = analyze_sentiment(query)
        return jsonify({'sentiment': sentiment})


    if __name__ == '__main__':
        app.run(debug=True)