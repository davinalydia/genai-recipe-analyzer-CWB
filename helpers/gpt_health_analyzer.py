import json
from helpers.openai_client import fetch_openai_chat_response, load_prompt

def analyze_healthiness(ingredients, steps):
    prompt = load_prompt("prompts/health_score_prompt.j2", ingredients=ingredients, steps=steps)
    result_text = fetch_openai_chat_response(prompt)
    try:
        return json.loads(result_text)
    except Exception:
        return {"error": f"Could not parse: {result_text}", "raw": result_text}
