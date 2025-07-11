import json
from helpers.openai_client import fetch_openai_chat_response, load_prompt

def extract_dietary_restrictions(ingredients):
    prompt = load_prompt("prompts/dietary_restrictions.j2", ingredients=ingredients)
    result_text = fetch_openai_chat_response(prompt)
    try:
        return json.loads(result_text)
    except Exception:
        return {"error": f"Could not parse: {result_text}", "raw": result_text}
