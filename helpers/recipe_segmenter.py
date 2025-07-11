def segment_recipe(recipe_text: str) -> dict:
    """
    Splits recipe into ingredients and steps sections.
    """
    sections = {}
    parts = recipe_text.split("Steps:")
    if len(parts) == 2:
        sections["ingredients"] = parts[0].replace("Ingredients:", "").strip()
        sections["steps"] = parts[1].strip()
    else:
        sections["ingredients"] = ""
        sections["steps"] = ""
    return sections