import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from google.genai import types

# 1. Initialize FastAPI
app = FastAPI()

# 2. Setup Gemini Client (Picks up GEMINI_API_KEY from environment)
client = genai.Client()

# 3. Define the Request Data Model
class ForensicRequest(BaseModel):
    evidence: str

# --- ROUTES ---

@app.get("/")
def read_root():
    """This route fixes the 'Cannot GET /' error"""
    return {"status": "Forensiq Backend is Live", "version": "Gemini-3-Pro"}

@app.post("/analyze")
async def analyze_evidence_route(request: ForensicRequest):
    """This route is for your frontend to call the AI"""
    try:
        response = client.models.generate_content(
            model="gemini-3-pro-preview",
            contents=request.evidence,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(include_thoughts=True, thinking_level="high")
            )
        )
        
        # Capture the thought process for the 'Reasoning Engineer' audit log
        thoughts = [p.text for p in response.candidates[0].content.parts if p.thought]
        
        return {
            "result": response.text,
            "thoughts": thoughts
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 4. Local execution block (for testing in terminal)
if __name__ == "__main__":
    print("🚀 Running manual test...")
    # This manually calls the AI to prove the terminal isn't blank
    test_response = client.models.generate_content(
        model="gemini-3-pro-preview", 
        contents="Manual terminal test: Are you active?"
    )
    print("AI Response:", test_response.text)
