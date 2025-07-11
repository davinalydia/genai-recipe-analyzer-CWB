# Recipe Analyzer

A demo GenAI-style pipeline for segmenting, extracting, and analyzing recipes using OpenAI API and prompt files.

## Setup

1. Clone this repo.
2. Create a `.env` file in the root folder and add your OpenAI API key:
    ```
    OPENAI\_API\_KEY=sk-xxxxxx
    ```
3. (Recommended) Create a virtual environment and activate it:
    ```
    python -m venv venv
    venv\Scripts\activate
    ```
4. Install dependencies:
    ```
    pip install -r requirements.txt
    ````

## Running the Pipeline
    ```
    python main.py
    ```

## Running Tests
    ```
    python -m pytest tests/
    ```

## Prompts

All LLM prompts are stored in the `/prompts` folder as Jinja2 templates.

## Security

* Do **NOT** commit your `.env` or API keys to GitHub!


## requirements.txt
```
openai
jinja2
python-dotenv
pytest

```