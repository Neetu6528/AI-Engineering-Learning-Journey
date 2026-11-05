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

# 3 prompts
role = "user"
prompt1 = "What is OAuth? in short 2 lines"
prompt2 = "What is session? in short 2 lines"
prompt3 = "What is cookie? in short 2 lines"

prompt = [prompt1, prompt2, prompt3]
for p in prompt:
    message = {
        "role": role, 
        "content": p
    }

    response = client.chat.completions.create(
        model=models,
        messages=[message],
        max_tokens=50
    )
    usage = response.usage
    print(f"Prompt: {p} -> prompt token : {usage.total_tokens} tokens. Completion tokens: {usage.completion_tokens} tokens. Finish reason: {response.choices[0].finish_reason}")
    print(response.choices[0].message.content)


