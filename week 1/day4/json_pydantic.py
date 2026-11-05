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

# Structure it 
from pydantic import BaseModel 

class Ticket(BaseModel):
    name: str
    device: str
    issue: str
    address: str
    phone_number: str

schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object",
}

system_prompt = f"""Please extract the following information from the text and return it in JSON format according to the schema: {schema}."""

message_system = {
    "role": "system",
    "content": system_prompt
}

text = "Hello  my name is neetu. I have an iphone which is not working properly. I want to get it repaired. Can you help me with that? My address is 123, ABC street, New York. My phone number is 1234567890. Please let me know the nearest repair center."

prompt = f"Please extract the following information from the text: Name, Device, Issue, Address, Phone Number. Text: {text}"

message = {
    "role": "user", 
    "content": prompt
}

response = client.chat.completions.create(
    model=models,
    messages=[message_system, message],
    response_format=response_format
)
print(response.choices[0].message.content)

import json
raw_json = response.choices[0].message.content
data = json.loads(raw_json)
ticket = Ticket(**data)
print(ticket.name)
print(ticket.device)
print(ticket.issue)
print(ticket.address)
print(ticket.phone_number)
