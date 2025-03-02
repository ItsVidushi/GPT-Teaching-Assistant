from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

def generate(leetcode_url, user_question):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text="""Hello"""
                ),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(
                    text="""Hi there! How can I help you today? Are you working on a specific problem or just exploring? Let me know what you're up to, and I'll do my best to assist you. 😊
"""
                ),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text="""Helllo"""
                ),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(
                    text="""Hey! Great to see you again. Did you want to pick up where we left off, or is there something new on your mind? I'm ready for anything, from trees to graphs, or even just a quick chat about Big O! Let me know what you're thinking. ✨
"""
                ),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=f"""
    You are a master of Data Structures and Algorithms (DSA), acting as a teaching assistant for students solving LeetCode problems. A user has submitted a LeetCode problem link along with a specific doubt or question about the problem. Your goal is NOT to provide a direct solution but to guide the user toward understanding the problem better. Use thought-provoking hints, break down key concepts, and ask leading questions that encourage problem-solving intuition.

Here is the LeetCode problem: {leetcode_url}
The user's question: {user_question}

Engage the user with an insightful response, referencing related concepts, potential edge cases, and common mistakes while keeping the tone friendly and interactive.
    """

                ),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(
                text="""You are an AI teaching assistant for DSA. Engage users with supportive tone,use analogies and real-world examples, and encourage critical thinking without giving direct answers. Incorporate humor and interactive dialogue, and suggest coding experiments."""
            ),
        ],
    )

    response_parts = []
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_parts.append(chunk.text)
    return ''.join(response_parts)


@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()  # Ensure you get JSON data
    leetcode_url = data.get('leetcode_url', '')
    user_question = data.get('question', '')
    
    # Check if both the URL and question are provided
    if not leetcode_url or not user_question:
        return jsonify({"error": "Both a LeetCode URL and a question are required."}), 400

    response = generate(leetcode_url, user_question)
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=3030)  # Run on a specific port if needed