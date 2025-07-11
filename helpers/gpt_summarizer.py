import json
from helpers.openai_client import fetch_openai_chat_response, load_prompt

def summarize_recipe(ingredients, steps):
    prompt = load_prompt("prompts/summarize_recipe.j2", ingredients=ingredients, steps=steps)
    result_text = fetch_openai_chat_response(prompt)
    try:
        return json.loads(result_text)
    except Exception:
        return {"error": f"Could not parse: {result_text}", "raw": result_text}
