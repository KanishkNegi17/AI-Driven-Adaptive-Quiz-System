import json
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# Initialize the new client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_adaptive_question(topic, level):
    # Using gemini-2.5-flash as it is the latest and fastest for this use case
    model_id = 'gemini-2.5-flash' 
    
    prompt = f"""
    You are an expert EASA Flight Dispatcher examiner.
    Generate a multiple-choice question about: {topic}.
    The difficulty level must be {level} out of 10 (1 = fundamental basics, 10 = highly advanced EASA regulations).
    
    You MUST respond with a valid JSON object in the exact structure below. No markdown formatting.
    {{
        "question": "Clear, concise question text",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "correct_answer": "The exact string of the correct option",
        "explanation": "Brief feedback explaining why the answer is correct."
    }}
    """
    
    try:
        response = client.models.generate_content(
            model=model_id,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.7
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"API Error: {e}")
        return None

if __name__ == "__main__":
    data = get_adaptive_question("Aviation Meteorology", 3)
    print(json.dumps(data, indent=2))