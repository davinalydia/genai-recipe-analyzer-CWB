from helpers.ingredient_extractor import extract_ingredients

def test_extract_ingredients():
    s = "tomato, spinach, oil"
    out = extract_ingredients(s)
    assert out == ["tomato", "spinach", "oil"]
    s2 = ""
    assert extract_ingredients(s2) == []
