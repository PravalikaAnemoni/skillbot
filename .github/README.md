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

- RE Local URL: http://localhost:8501
  Network URL: http://192.168.0.105:8501

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

## demo working video
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

---

## ✨ Demo

### 🖼️ Screenshots

Here are a few glimpses of SkillBot in action, showcasing the chat interface and the analytics dashboard.

![WhatsApp Image 2025-09-30 at 20 59 42_ddee5797](https://github.com/user-attachments/assets/32258e01-b6f1-413a-bdda-4f60e249febd)
![WhatsApp Image 2025-09-30 at 20 59 56_bc55f597](https://github.com/user-attachments/assets/7eccc9b7-8adc-4531-933e-1b01e18ccaa2)
![WhatsApp Image 2025-09-30 at 20 59 56_6ebac2dd](https://github.com/user-attachments/assets/b4b27e89-e764-4b69-a974-881261e4915d)


### 🎬 Demo Video

Watch this short video to see the full functionality of SkillBot, including the conversational flow and the real-time analytics dashboard.


https://github.com/user-attachments/assets/7eeeb2d1-e43d-492e-848b-dddf48886577


---

## 🛠️ Tech Stack

- Python 3.8+
- spaCy (NLP processing)
- TextBlob (Sentiment analysis)
- Flask (REST API)
- Streamlit (Dashboard)
- scikit-learn (ML features)

---

## Here are the complete steps to run the SkillBot project:

Environment Setup ✅

# Navigate to project directory
cd c:\Users\naras\OneDrive\Desktop\skillbot

# Activate virtual environment
.venv\Scripts\activate

Start Flask API Server ✅
# In first terminal
python api/main.py

API will run at http://127.0.0.1:5000
Endpoints available:
GET /greet - Welcome message
POST /chat - Send chat messages
GET /courses - View courses
GET /internships - View internships
GET /faq - View FAQs

Launch Streamlit Dashboard ✅
# In second terminal
streamlit run dashboard/app.py

Dashboard will open at http://localhost:8501
Features:
Interactive chat interface
Real-time analytics
Course catalog
Internship listings
Access the Applications

API Documentation: Visit http://127.0.0.1:5000
Interactive Dashboard: Visit http://localhost:8501
Example API Usage
# Get greeting
curl http://127.0.0.1:5000/greet

# Send chat message
curl -X POST -H "Content-Type: application/json" \
     -d '{"query":"Tell me about your courses"}' \
     http://127.0.0.1:5000/chat
     
Dashboard Features

Chat directly in the web interface
View analytics in real-time
Access quick links to courses and internships
Monitor sentiment analysis and intent distribution
The project is now running with both the API server and the interactive dashboard. You can:

Use the REST API for programmatic access
Use the Streamlit dashboard for interactive chat and analytics
Test different types of queries about courses, internships, and general information



**Note**: This is an educational project developed for SkillHigh's learning platform.
