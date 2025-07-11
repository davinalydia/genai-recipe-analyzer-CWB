from helpers.step_extractor import extract_steps

def test_extract_steps():
    s = "Mix all. Bake at 180C. Serve."
    out = extract_steps(s)
    assert out == ["Mix all", "Bake at 180C", "Serve"]
