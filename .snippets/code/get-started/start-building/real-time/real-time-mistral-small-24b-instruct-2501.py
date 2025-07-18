# Real-time completions with the Mistral Small model on kluster.ai

from os import environ
from openai import OpenAI
from getpass import getpass

# Get API key from user input
api_key = environ.get("API_KEY") or getpass("Enter your kluster.ai API key: ")

print(f"📤 Sending a chat completion request to kluster.ai...\n")

# Initialize OpenAI client pointing to kluster.ai API
client = OpenAI(
    api_key=api_key,
    base_url="https://api.kluster.ai/v1"
)

# Create chat completion request
completion = client.chat.completions.create(
    model="mistralai/Mistral-Small-24B-Instruct-2501",
    messages=[
        {"role": "user", "content": "What is the ultimate breakfast sandwich?"}
    ]
)

"""Logs the full AI response to terminal."""

# Extract model name and AI-generated text
model_name = completion.model
text_response = completion.choices[0].message.content

# Print response to console
print(f"\n🔍 AI response (model: {model_name}):")
print(text_response)
