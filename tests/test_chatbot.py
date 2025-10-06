from skillbot.chatbot import SkillBot


def make_bot():
    import json, os
    repo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_dir = os.path.join(repo, 'data')
    with open(os.path.join(data_dir, 'faqs.json'), 'r', encoding='utf-8') as f:
        faqs = json.load(f)
    with open(os.path.join(data_dir, 'courses.json'), 'r', encoding='utf-8') as f:
        courses = json.load(f)
    with open(os.path.join(data_dir, 'internships.json'), 'r', encoding='utf-8') as f:
        internships = json.load(f)
    return SkillBot(faqs, courses, internships)


def test_greet():
    bot = make_bot()
    resp = bot.greet()
    assert isinstance(resp, str)
    assert "SkillBot" in resp or "Hi" in resp


def test_course_response():
    bot = make_bot()
    resp = bot.handle_query("What courses do you have?")
    assert isinstance(resp, str)
    assert "Python" in resp or "Data Science" in resp or "Web Development" in resp


def test_internship_response():
    bot = make_bot()
    resp = bot.handle_query("How do I apply for an internship?")
    assert isinstance(resp, str)
    assert "intern" in resp.lower() or "apply" in resp.lower()
