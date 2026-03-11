# ✈️ AI-Driven Adaptive Quiz System: EASA Flight Dispatcher

A dynamic, AI-powered quiz platform built to evaluate EASA Flight Dispatcher knowledge. Instead of relying on a static database, this application leverages Google's Gemini 2.5 Flash model to generate real-time, adaptive questions based on the user's ongoing performance.

## 🚀 Features
* **Adaptive Difficulty:** The system scales the question difficulty from Level 1 to 10. Correct answers increase the level, while incorrect answers decrease it.
* **Real-time Content Generation:** Questions are generated dynamically via the Gemini API, ensuring a unique assessment experience every time.
* **Instant Feedback:** Provides immediate evaluation and detailed explanations for every answer to facilitate learning.
* **Clean UI:** A fast, responsive frontend built entirely in Python using Streamlit.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Frontend/State Management:** Streamlit
* **AI/LLM:** Google GenAI SDK (Gemini 2.5 Flash)

## 📁 Project Structure
```text
├── app.py               # Streamlit frontend and state management
├── quiz_logic.py        # Core API logic and LLM prompt engineering
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables (API Key)
```
## ⚙️ Local Setup & Installation
### 1. Clone the repository:

```Bash
git clone [https://github.com/yourusername/easa-ai-quiz.git](https://github.com/yourusername/easa-ai-quiz.git)
cd easa-ai-quiz
```
### 2. Create and activate a virtual environment:

```Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies:

```Bash
pip install -r requirements.txt
Environment Variables:
```
### 4. Create a .env file in the root directory and add your Google Gemini API key:
```Plaintext
GEMINI_API_KEY=your_actual_api_key_here
```
### 5. Run the Application:
```Bash
streamlit run app.py
```
## 🌐 Live Deployment
The application is deployed and accessible here: https://ai-driven-adaptive-quiz-system.streamlit.app/