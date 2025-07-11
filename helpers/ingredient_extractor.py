def extract_ingredients(ingredients_text: str) -> list:
    """
    Returns a list of ingredient strings.
    """
    return [x.strip() for x in ingredients_text.split(",") if x.strip()]