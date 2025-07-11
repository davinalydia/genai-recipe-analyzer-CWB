from helpers.recipe_segmenter import segment_recipe

def test_segment_recipe():
    text = "Ingredients: egg, milk. Steps: Mix well."
    result = segment_recipe(text)
    assert result["ingredients"] == "egg, milk"
    assert result["steps"] == "Mix well."
