import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from jinja2 import Template

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a recipe analysis assistant for a demo GenAI pipeline project. "
        "Your job is to follow the instructions, reply only in JSON as specified, "
        "and do NOT invent any data not present in the input."
    )
}

def fetch_openai_chat_response(prompt_text, max_tokens=1000, deployment=None):
    model = deployment or os.getenv("AZURE_OPENAI_DEPLOYMENT")
    completion = client.chat.completions.create(
        model=model,
        messages=[
            SYSTEM_MESSAGE,
            {"role": "user", "content": prompt_text}
        ],
        max_completion_tokens=max_tokens,
        stream=False
    )
    return completion.choices[0].message.content

def load_prompt(path, **kwargs):
    with open(path, 'r', encoding='utf-8') as f:
        template = Template(f.read())
    for k, v in kwargs.items():
        if isinstance(v, list):
            kwargs[k] = ", ".join(v)
    return template.render(**kwargs)
