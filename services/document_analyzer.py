import json
import re

from services.gemini_service import ask_gemini


def analyze_document(text):

    prompt = f"""
You are an Industrial AI Assistant.

Analyze this industrial document and return ONLY valid JSON.

Return this schema:

{{
    "document_type":"",
    "department":"",
    "summary":"",
    "maintenance_type":"",
    "risk_level":"",
    "equipment":[],
    "keywords":[]
}}

Document:

{text[:8000]}
"""

    response = ask_gemini(prompt, context=text[:8000])
 # Remove markdown fences if Gemini returns ```json ... ```
    response = re.sub(r"^```json|```$", "", response.strip(), flags=re.MULTILINE).strip()
    # Convert JSON string to Python dictionary
    return json.loads(response)