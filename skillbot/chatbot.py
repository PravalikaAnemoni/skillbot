"""SkillBot Conversational AI Core
Handles intent recognition, response generation, and context management.
"""
import random
from functools import lru_cache
from typing import Dict, Any, List

from skillbot.nlp import tokenize, get_intent, analyze_sentiment


class SkillBot:
    def __init__(self, faqs: Dict[str, str], courses: Dict[str, Any], internships: Dict[str, Any], language: str = 'en'):
        self.faqs = faqs
        self.courses = courses
        self.internships = internships
        self.language = language
        self.chat_history: List[Dict[str, str]] = []

    @lru_cache(maxsize=2048)
    def _cached_intent(self, query: str) -> str:
        # Normalize whitespace before caching to avoid duplicates
        return get_intent((query or '').strip())

    def get_intent(self, query: str) -> str:
        return self._cached_intent(query)

    def get_sentiment(self, query: str) -> float:
        # Return a coarse polarity mapping for compatibility
        label = analyze_sentiment(query)
        return {"negative": -1.0, "neutral": 0.0, "positive": 1.0}.get(label, 0.0)

    def greet(self) -> str:
        return "Hi, I'm SkillBot, your course guide! How can I help you today?"

    def handle_query(self, query: str, sentiment: str = None) -> str:
        q = (query or '').strip()
        self.chat_history.append({'user': q})

        # Empathetic response based on sentiment label
        if sentiment == 'negative':
            empathy = "I'm sorry to hear that. "
        elif sentiment == 'positive':
            empathy = "That's great! "
        else:
            empathy = ""

        # Small talk detection using tokens and normalized text
        norm_q = ' '.join(tokenize(q, use_lemmas=False))
        small_talk_phrases = [
            'how are you', 'how r u', 'how are you today', 'how do you do', 'whats up',
            'how is it going', 'how are things', 'how are you doing', 'hows it going', 'hru', 'hw r u'
        ]
        if any(kw in norm_q for kw in small_talk_phrases):
            return empathy + random.choice([
                "I'm just a bot, but I'm here to help you! 😊",
                "I'm doing great, thanks for asking! How can I assist you today?",
                "I'm always ready to help you with SkillHigh info!"
            ])

        # Onboarding
        tokens = set(tokenize(q))
        if tokens & {'onboarding', 'join', 'enroll', 'registration', 'orientation', 'welcome'}:
            return empathy + "SkillHigh onboarding involves registration, orientation, and access to course materials. After enrolling, you'll receive a welcome email with next steps."

        # Internship application
        if ('apply' in tokens or 'application' in tokens or 'register' in tokens) and 'internship' in tokens:
            return empathy + "To apply for an internship, visit the SkillHigh website, go to the Internships section, and fill out the application form. You will be contacted by our team if shortlisted."

        # Internship info
        if 'internship' in tokens:
            return empathy + self._internship_info(q)

        # Courses
        if 'course' in tokens or 'courses' in tokens:
            return empathy + self._course_info(q)

        # Pricing
        if tokens & {'price', 'cost', 'fee', 'fees', 'pricing'}:
            return empathy + "SkillHigh courses range from ₹5,000 to ₹25,000 depending on duration and certification."

        # FAQ
        if 'faq' in tokens or 'question' in tokens or 'questions' in tokens:
            return empathy + self._faq_info(q)

        # Gratitude
        if tokens & {'thank', 'thanks', 'thankyou', 'thx'}:
            return empathy + random.choice(["You're welcome!", "Glad to help!", "Anytime!"])

        # Greetings
        if tokens & {'hi', 'hello', 'hey', 'helo', 'hlo', 'hai'}:
            return empathy + random.choice(["Hello!", "Hi there!", "Hey! How can I assist you?"])

        return empathy + self._fallback(query)

    def _course_info(self, q: str) -> str:
        return "SkillHigh offers Python, Data Science, and Web Development courses. Ask for details!"

    def _internship_info(self, q: str) -> str:
        return "Internships available in Data Science and Web Development. Duration: 3-6 months. Apply via our website."

    def _faq_info(self, q: str) -> str:
        for k, v in self.faqs.items():
            if k in q.lower():
                return v
        return "You can ask about courses, pricing, internships, or certifications."

    def _fallback(self, query: str) -> str:
        return "Sorry, I didn't understand that. Can you rephrase or ask about courses, internships, or FAQs?"

    def get_history(self) -> List[Dict[str, str]]:
        return self.chat_history
                        # Courses
