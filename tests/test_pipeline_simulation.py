from helpers.recipe_segmenter import segment_recipe
from helpers.ingredient_extractor import extract_ingredients
from helpers.step_extractor import extract_steps

def test_full_pipeline():
    fake = {"recipe_text": "Ingredients: tofu, broccoli, garlic. Steps: Steam tofu. Stir-fry broccoli and garlic."}
    sections = segment_recipe(fake["recipe_text"])
    ingredients = extract_ingredients(sections["ingredients"])
    steps = extract_steps(sections["steps"])
    assert ingredients == ["tofu", "broccoli", "garlic"]
    assert steps == ["Steam tofu", "Stir-fry broccoli and garlic"]
