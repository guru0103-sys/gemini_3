# main.py
import os
from google import genai

# The SDK automatically picks up GEMINI_API_KEY from your Codespace secrets
client = genai.Client() 

def analyze_evidence(text_input):
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=text_input,
        config={
            "thinking_config": {"include_thoughts": True, "thinking_level": "high"}
        }
    )
    return response.text
    if __name__ == "__main__":
        print("🚀 Starting forensic analysis...")
        result = analyze_evidence("Verify this sample evidence.")
        print("Result:", result)
    

