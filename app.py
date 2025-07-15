import streamlit as st
import json
from helpers.recipe_segmenter import segment_recipe
from helpers.ingredient_extractor import extract_ingredients
from helpers.step_extractor import extract_steps
from helpers.gpt_summarizer import summarize_recipe
from helpers.gpt_dietary import extract_dietary_restrictions
from helpers.gpt_health_analyzer import analyze_healthiness

st.title("Recipe Analyzer Demo (GenAI Pipeline)")

st.write("""
This app analyzes recipes using a multi-step GenAI pipeline:
- **Summary:** Condenses the recipe in one sentence.
- **Dietary Restrictions:** Identifies common allergens or dietary issues.
- **Health Analysis:** Classifies ingredients, suggests substitutions, and gives a healthiness score.
""")

# --- Input area ---
st.header("Input Recipes")

tab1, tab2 = st.tabs(["Paste JSON", "Upload File"])

recipes = None
input_error = None

with tab1:
    pasted = st.text_area("Paste your recipes JSON (array of objects, each with 'name' and 'recipe_text'):", height=200)
    if pasted.strip():
        try:
            recipes = json.loads(pasted)
            assert isinstance(recipes, list)
            for r in recipes:
                assert "name" in r and "recipe_text" in r
        except Exception as e:
            input_error = f"Invalid JSON: {e}"

with tab2:
    uploaded = st.file_uploader("Or upload a recipes.json file", type=["json"])
    if uploaded and not recipes:  # file takes priority only if pasted is empty
        try:
            recipes = json.load(uploaded)
            assert isinstance(recipes, list)
            for r in recipes:
                assert "name" in r and "recipe_text" in r
        except Exception as e:
            input_error = f"Invalid JSON file: {e}"

# Fallback to sample if no user input
if not recipes and not input_error:
    with open("data/sample_recipes.json", "r") as f:
        recipes = json.load(f)

if input_error:
    st.error(input_error)
elif recipes:
    recipe_names = [r.get("name", "Unnamed Recipe") for r in recipes]
    selected = st.selectbox("Choose a recipe to analyze", recipe_names)
    recipe = next(r for r in recipes if r.get("name") == selected)
    st.subheader(f"Input Recipe: {recipe.get('name', '')}")
    st.code(recipe.get("recipe_text", ""), language="markdown")

    if st.button("Analyze"):
        sections = segment_recipe(recipe.get("recipe_text", ""))
        ingredients = extract_ingredients(sections.get("ingredients", ""))
        steps = extract_steps(sections.get("steps", ""))

        with st.spinner("Summarizing recipe..."):
            summary = summarize_recipe(ingredients, steps)
        st.success("Summary:")
        st.json(summary)

        with st.spinner("Extracting dietary restrictions..."):
            restrictions = extract_dietary_restrictions(ingredients)
        st.success("Dietary Restrictions:")
        st.json(restrictions)

        with st.spinner("Analyzing healthiness..."):
            health = analyze_healthiness(ingredients, steps)
        st.success("Health Analysis:")
        st.json(health)
