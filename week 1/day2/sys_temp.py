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
message_system = {
    "role": "system",   
    "content": "You are a brand manager who suggests name for my food company for burger. Give one name."
}
message = {
    "role": "user", 
    "content": "Suggest a name for my company."
}

response = client.chat.completions.create(
    model=models,
    messages=[message_system, message],
    temperature=0.7,
)
print(response.choices[0].message.content)
