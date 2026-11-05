import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key is required.")

client = Groq(api_key=my_api_key)

models = "openai/gpt-oss-20b"
message = {
    "role": "user", 
    "content": "What is OAuth? "
}

response = client.chat.completions.create(
    model=models,
    messages=[message]
)
print(response.choices[0].message.content)
