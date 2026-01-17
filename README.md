**🔮 Numerology Expert (LangGraph Project)**
**AI-powered Numerology Advisor built using LangGraph**

Numerology Expert is an experimental AI application that takes a user’s date of birth as input and generates numerology-based insights about their life, personality, strengths, weaknesses, and areas of improvement.
The project demonstrates how LangGraph can be used to build structured, multi-step reasoning flows using LLMs.


**🚀 What This Project Does**
- Accepts Date of Birth as user input
- Uses Prompt Templates to guide reasoning
- Generates insights on:
- Personality traits
- Life direction
- Strengths & weaknesses
- Areas of improvement


**🏗️ Architecture Overview : **

User Input (DOB)
      |
      v
Prompt Template
      |
      v
LangGraph Node
      |
      v
LLM Reasoning
      |
      v
Final Numerology Insight



**🧪 Tech Stack**
- Python
- LangGraph
- Ollama / OpenAI-compatible LLM
- PromptTemplate


**🛠️ How to Run**

**1️⃣ Clone the repo**
git clone https://github.com/your-username/Numerology-Expert.git
cd Numerology-Expert

**2️⃣ Install dependencies**
pip install -r requirements.txt

**3️⃣ Run the app**
python main.py

**🧾 Example Input**
Date of Birth: 12-08-1995


**Example Output**
- You are naturally intuitive and emotionally intelligent.
- You tend to lead with empathy, but you must work on consistency and discipline.
- Your life path favors creativity and communication.


