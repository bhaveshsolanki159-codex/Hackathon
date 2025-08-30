import os
import google.generativeai as genai
from flask import Blueprint, request, jsonify

chat_bp = Blueprint("chat", __name__)

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use Gemini
chat_model = genai.GenerativeModel("gemini-1.5-flash")  # good balance of speed & quality
mood_model = genai.GenerativeModel("gemini-1.5-flash")  # reuse Gemini for classification


def classify_mood(user_message: str) -> str:
    """Use Gemini to classify mood into categories."""
    try:
        prompt = f"""
        Analyze the mood of this message: "{user_message}"

        Respond with only ONE word from this list:
        - happy
        - sad
        - stressed
        - angry
        - neutral
        """
        response = mood_model.generate_content(prompt)
        mood = response.text.strip().lower()

        # Ensure it's one of the valid categories
        if mood not in ["happy", "sad", "stressed", "angry", "neutral"]:
            mood = "neutral"

        return mood
    except Exception:
        return "neutral"


@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    try:
        # Step 1: Mood detection
        mood = classify_mood(user_message)

        # Step 2: AI reply
        response = chat_model.generate_content(user_message)
        ai_reply = response.text if response and response.text else "I'm here to listen."

        return jsonify({"reply": ai_reply, "mood": mood})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
