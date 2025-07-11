import streamlit as st
import json
from helpers.recipe_segmenter import segment_recipe
from helpers.ingredient_extractor import extract_ingredients
from helpers.step_extractor import extract_steps
from helpers.gpt_summarizer import summarize_recipe
from helpers.gpt_dietary import extract_dietary_restrictions
from helpers.gpt_health_analyzer import analyze_healthiness

st.title("Recipe Analyzer Demo (GenAI Pipeline)")

uploaded = st.file_uploader("Upload a Recipe JSON file (or use examples)", type=["json"])

if uploaded:
    recipes = json.load(uploaded)
else:
    # Fallback: load example recipes
    with open("data/sample_recipes.json", "r") as f:
        recipes = json.load(f)

recipe_names = [r["name"] for r in recipes]
selected = st.selectbox("Choose a recipe", recipe_names)

if selected:
    recipe = next(r for r in recipes if r["name"] == selected)
    st.subheader(f"Input Recipe: {recipe['name']}")
    st.write(recipe["recipe_text"])

    if st.button("Analyze"):
        sections = segment_recipe(recipe["recipe_text"])
        ingredients = extract_ingredients(sections["ingredients"])
        steps = extract_steps(sections["steps"])

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
