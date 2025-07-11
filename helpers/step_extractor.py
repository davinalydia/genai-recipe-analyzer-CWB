def extract_steps(steps_text: str) -> list:
    """
    Returns a list of cooking steps.
    """
    return [x.strip() for x in steps_text.split(".") if x.strip()]