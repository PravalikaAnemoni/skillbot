"""
SkillBot Conversational AI Core
Handles intent recognition, response generation, and context management.
"""
import random
from typing import Dict, Any, List
import spacy
from textblob import TextBlob

class SkillBot:
    def __init__(self, faqs: Dict[str, str], courses: Dict[str, Any], internships: Dict[str, Any], language: str = 'en'):
        self.faqs = faqs
        self.courses = courses
        self.internships = internships
        self.language = language
        self.chat_history: List[Dict[str, str]] = []
        
        # Initialize NLP components
        self.nlp = spacy.load('en_core_web_sm')
        
        # Intent patterns
        self.intent_patterns = {
            'greet': ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon'],
            'thank': ['thanks', 'thank you', 'thx', 'appreciate', 'grateful'],
            'bye': ['bye', 'goodbye', 'see you', 'cya', 'farewell'],
            'course': ['course', 'class', 'learn', 'study', 'training', 'program'],
            'internship': ['internship', 'intern', 'work', 'job', 'opportunity'],
            'price': ['price', 'cost', 'fee', 'fees', 'pricing'],
            'duration': ['duration', 'long', 'time', 'months', 'weeks'],
            'certificate': ['certificate', 'certification', 'certified']
        }
"""
SkillBot Conversational AI Core
Handles intent recognition, response generation, and context management.
"""
import random
from typing import Dict, Any, List
import spacy
from textblob import TextBlob

class SkillBot:
    def __init__(self, faqs: Dict[str, str], courses: Dict[str, Any], internships: Dict[str, Any], language: str = 'en'):
        self.faqs = faqs
        self.courses = courses
        self.internships = internships
        self.language = language
        self.chat_history: List[Dict[str, str]] = []
        
        # Initialize NLP components
        self.nlp = spacy.load('en_core_web_sm')
        
        # Intent patterns
        self.intent_patterns = {
            'greet': ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon'],
            'thank': ['thanks', 'thank you', 'thx', 'appreciate', 'grateful'],
            'bye': ['bye', 'goodbye', 'see you', 'cya', 'farewell'],
            'course': ['course', 'class', 'learn', 'study', 'training', 'program'],
            'internship': ['internship', 'intern', 'work', 'job', 'opportunity'],
            'price': ['price', 'cost', 'fee', 'fees', 'pricing'],
            'duration': ['duration', 'long', 'time', 'months', 'weeks'],
            'certificate': ['certificate', 'certification', 'certified']
        }

    def get_intent(self, query: str) -> str:
        """
        Analyze user intent using pattern matching and NLP
        """
        doc = self.nlp(query.lower())
        
        # Check for intents
        for intent, patterns in self.intent_patterns.items():
            if any(pattern in doc.text for pattern in patterns):
                return intent
        
        return 'other'
    
    def get_sentiment(self, query: str) -> float:
        """
        Analyze sentiment of user query using TextBlob
        Returns a polarity score between -1 (negative) and 1 (positive)
        """
        blob = TextBlob(query)
        return blob.sentiment.polarity
    
    def greet(self) -> str:
        return "Hi, I'm SkillBot, your course guide! How can I help you today?"

    def handle_query(self, query: str, sentiment: str = None) -> str:
        # Improved intent recognition
        q = query.lower()
        self.chat_history.append({'user': query})
        # Empathetic response based on sentiment
        if sentiment == 'negative':
            empathy = "I'm sorry to hear that. "
        elif sentiment == 'positive':
            empathy = "That's great! "
        else:
            empathy = ""
        # Small talk detection (robust to punctuation and minor typos)
        import re

        def normalize(text):
            return re.sub(r'[^a-zA-Z0-9 ]', '', text.lower())

        norm_q = normalize(query)
        small_talk_keywords = [
            'how are you', 'how r u', 'how are you today', 'how do you do', "whats up", 'how is it going', 'how are things', 'how are you doing', 'hows it going', 'hru', 'hw r u'
        ]
        if any(kw in norm_q for kw in small_talk_keywords):
            return empathy + random.choice([
                "I'm just a bot, but I'm here to help you! 😊",
                "I'm doing great, thanks for asking! How can I assist you today?",
                "I'm always ready to help you with SkillHigh info!"
            ])
        # Onboarding (handle more variations)
        onboarding_keywords = ['onboarding', 'join', 'enroll', 'registration', 'orientation', 'welcome']
        if any(word in q for word in onboarding_keywords):
            return empathy + "SkillHigh onboarding involves registration, orientation, and access to course materials. After enrolling, you'll receive a welcome email with next steps."
        # Internship application (handle more variations and punctuation)
        if (
            ('apply' in norm_q or 'application' in norm_q or 'register' in norm_q)
            and 'internship' in norm_q
        ):
            return empathy + "To apply for an internship, visit the SkillHigh website, go to the Internships section, and fill out the application form. You will be contacted by our team if shortlisted."
        # Internship info (robust to punctuation/typos)
        if 'internship' in norm_q:
            return empathy + self._internship_info(q)
        # Courses
        if 'course' in q:
            return empathy + self._course_info(q)
        # Pricing
        if 'price' in q or 'cost' in q:
            return empathy + "SkillHigh courses range from ₹5,000 to ₹25,000 depending on duration and certification."
        # FAQ
        if 'faq' in q or 'question' in q:
            return empathy + self._faq_info(q)
        # Gratitude
        if 'thank' in q:
            return empathy + random.choice(["You're welcome!", "Glad to help!", "Anytime!"])
        # Greetings (handle misspellings)
        greeting_keywords = ['hi', 'hello', 'hey', 'helo', 'hlo', 'hai', 'heyy', 'helloo']
        if any(greet in q for greet in greeting_keywords):
            return empathy + random.choice(["Hello!", "Hi there!", "Hey! How can I assist you?"])
        return empathy + self._fallback(query)

    def _course_info(self, q: str) -> str:
        # Dummy course info
        return "SkillHigh offers Python, Data Science, and Web Development courses. Ask for details!"

    def _internship_info(self, q: str) -> str:
        return "Internships available in Data Science and Web Development. Duration: 3-6 months. Apply via our website."

    def _faq_info(self, q: str) -> str:
        for k, v in self.faqs.items():
            if k in q:
                return v
        return "You can ask about courses, pricing, internships, or certifications."

    def _fallback(self, query: str) -> str:
        return "Sorry, I didn't understand that. Can you rephrase or ask about courses, internships, or FAQs?"

    def get_history(self) -> List[Dict[str, str]]:
        return self.chat_history
