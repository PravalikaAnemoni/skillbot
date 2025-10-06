"""
SkillBot REST API using Flask
Clean, single-entrypoint server with basic input validation and helpful errors.
"""

import os
import sys
import json
import logging
from flask import Flask, request, jsonify

# Ensure project root is on path so imports work when running from api/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from skillbot.chatbot import SkillBot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load dummy data using project-relative paths
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
try:
    with open(os.path.join(DATA_DIR, 'faqs.json'), 'r', encoding='utf-8') as f:
        faqs = json.load(f)
    with open(os.path.join(DATA_DIR, 'courses.json'), 'r', encoding='utf-8') as f:
        courses = json.load(f)
    with open(os.path.join(DATA_DIR, 'internships.json'), 'r', encoding='utf-8') as f:
        internships = json.load(f)
except Exception as e:
    logger.exception('Failed to load data files from %s', DATA_DIR)
    raise

# Instantiate bot and fail fast with helpful message if dependencies are missing
try:
    bot = SkillBot(faqs, courses, internships)
except Exception as e:
    logger.exception('Failed to initialize SkillBot — check spaCy model and TextBlob corpora.')
    # Provide actionable hint for common spaCy error
    if "Can't find model" in str(e) or 'en_core_web_sm' in str(e):
        logger.error('spaCy model en_core_web_sm not found. Run: python -m spacy download en_core_web_sm')
    raise


def _bad_request(message: str):
    return jsonify({'error': message}), 400


@app.route('/', methods=['GET'])
def home():
    return (
        "<h1>Welcome to SkillBot API</h1>"
        "<p>Use <b>/chat</b> (POST) for chatbot queries.<br>"
        "Use <b>/greet</b> (GET) for a greeting.</p>",
        200,
    )


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True)
    if not data:
        return _bad_request('Request body must be JSON with a "query" field.')
    query = data.get('query')
    if not isinstance(query, str) or not query.strip():
        return _bad_request('Provide a non-empty string in the "query" field.')
    try:
        response = bot.handle_query(query)
        return jsonify({'response': response})
    except Exception:
        logger.exception('Error while handling query')
        return jsonify({'error': 'Internal server error while processing the query.'}), 500


@app.route('/greet', methods=['GET'])
def greet():
    try:
        return jsonify({'response': bot.greet()})
    except Exception:
        logger.exception('Error in greet()')
        return jsonify({'error': 'Internal server error.'}), 500


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
    try:
        return jsonify({'history': bot.get_history()})
    except Exception:
        logger.exception('Error getting history')
        return jsonify({'error': 'Internal server error.'}), 500


@app.route('/sentiment', methods=['POST'])
def sentiment_endpoint():
    data = request.get_json(silent=True)
    if not data:
        return _bad_request('Request body must be JSON with a "query" field.')
    query = data.get('query')
    if not isinstance(query, str):
        return _bad_request('Provide a string in the "query" field.')
    try:
        from skillbot.nlp import analyze_sentiment

        sentiment = analyze_sentiment(query)
        return jsonify({'sentiment': sentiment})
    except Exception:
        logger.exception('Error analyzing sentiment')
        return jsonify({'error': 'Internal server error.'}), 500


if __name__ == '__main__':
    # Allow overriding host/port with env vars for simple deployments/tests
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', '5000'))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() in ('1', 'true', 'yes')
    logger.info('Starting SkillBot API on %s:%s (debug=%s)', host, port, debug)
    app.run(host=host, port=port, debug=debug)