"""
SkillBot Analytics Dashboard
Basic usage stats and most asked queries
"""
import json
from collections import Counter

def get_most_asked(history):
    questions = [h['user'] for h in history if 'user' in h]
    return Counter(questions).most_common(5)

# Example usage
if __name__ == '__main__':
   file_path = "C:/Users/naras/OneDrive/Desktop/skillbot/demo/chat_history.json"

with open(file_path, 'r', encoding='utf-8') as f:
    data = f.read()


    history = json.load(f)
    print("Top 5 most asked questions:")
    for q, count in get_most_asked(history):
        print(f"{q}: {count} times")
