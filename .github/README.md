# SkillBot 🤖

An AI-powered educational chatbot for SkillHigh, built with Python, spaCy, and machine learning. The chatbot assists students with course information, internship details, and FAQs while providing a natural, engaging conversational experience.

## 🌟 Key Features

- **🧠 NLP-Based Intelligence**
  - Intent recognition using spaCy
  - Sentiment analysis for empathetic responses
  - Smart context handling
  - Natural language understanding

- **💬 Conversational Features**
  - Course and internship guidance
  - FAQ handling with context awareness
  - Small talk capabilities
  - Multi-turn conversations

- **🔌 Integration & Analytics**
  - REST API for easy integration
  - Real-time analytics dashboard
  - Usage statistics and insights
  - Interactive Streamlit interface

## 🛠️ Tech Stack

- Python 3.8+
- spaCy (NLP processing)
- TextBlob (Sentiment analysis)
- Flask (REST API)
- Streamlit (Dashboard)
- scikit-learn (ML features)

## 📊 Architecture

```
skillbot/
├── api/          # Flask REST API
├── dashboard/    # Streamlit analytics interface
├── data/         # Training data and resources
└── skillbot/     # Core chatbot implementation
    ├── chatbot.py  # Main chatbot logic
    └── nlp.py      # NLP processing utilities
```

## 🚀 Quick Start

1. Clone and setup:
```bash
git clone https://github.com/yourusername/skillbot.git
cd skillbot
python -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

2. Run the API:
```bash
python api/main.py
```

3. Launch dashboard:
```bash
streamlit run dashboard/app.py
```

## 📝 About

SkillBot is designed to provide instant, intelligent support for students and learners at SkillHigh. It uses advanced NLP techniques to understand queries and provide relevant, contextual responses while maintaining a friendly, helpful tone.

## ✨ Demo

- REST API: http://localhost:5000
- Dashboard: [http://localhost:8501](http://localhost:8503/)

## 🔍 Key Capabilities

- Course information and recommendations
- Internship opportunity details
- FAQ handling with context awareness
- Real-time analytics and insights
- Sentiment-aware responses
- Chat history tracking

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- spaCy for NLP capabilities
- Streamlit for the awesome dashboard framework
- Flask for the reliable API framework

---
**Note**: This is an educational project developed for SkillHigh's learning platform.
