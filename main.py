# main.
import os
from google import genai
export GEMINI_API_KEY='AIzaSyCr2LNdmvhNYx41IPnIFbVqxxnOXg-8K_U'

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
    # --- Existing imports and analyze_evidence function above ---

# ADD THIS TO THE BOTTOM:
if __name__ == "__main__":
    print("🔍 Starting Forensic Analysis...")
    
    # Replace the text below with a sample you want to test
    sample_text = "Check for discrepancies in this testimony."
    
    try:
        result = analyze_evidence(sample_text)
        print("\n✅ Analysis Result:")
        print(result)
    except Exception as e:
        print(f"\n❌ Error: {e}")

