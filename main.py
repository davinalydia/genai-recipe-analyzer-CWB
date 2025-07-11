import json
from helpers.recipe_segmenter import segment_recipe
from helpers.ingredient_extractor import extract_ingredients
from helpers.step_extractor import extract_steps
from helpers.gpt_summarizer import summarize_recipe
from helpers.gpt_dietary import extract_dietary_restrictions
from helpers.gpt_health_analyzer import analyze_healthiness

def main():
    with open("data/sample_recipes.json", "r") as f:
        recipes = json.load(f)
    for recipe in recipes:
        sections = segment_recipe(recipe["recipe_text"])
        ingredients = extract_ingredients(sections["ingredients"])
        steps = extract_steps(sections["steps"])

        summary = summarize_recipe(ingredients, steps)
        restrictions = extract_dietary_restrictions(ingredients)
        health = analyze_healthiness(ingredients, steps)

        print(f"Recipe: {recipe['name']}")
        print("Summary:", summary.get("summary") or summary)
        print("Restrictions:", restrictions.get("restrictions") or restrictions)
        print("Health Analysis:", health)
        print("---")

if __name__ == "__main__":
    main()
