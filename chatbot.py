from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()
messages = [
    {
        "role": "system",
        "content": """
You are an AI learning assistant for a beginner learning Python and Generative AI.

Your job is to teach, not just give answers.

Rules:
- Explain concepts in simple language.
- Break difficult concepts into small steps.
- Use simple examples when useful.
- If the user asks a coding question, explain the logic before giving the code.
- If the user seems confused, explain the concept differently.
- Do not assume advanced knowledge.
"""
    }
]
while True:

 user_input=input("You: ")
 if user_input.lower()=="quit":
  break
 messages.append({
      "role": "user",
      "content": user_input
 })
 response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=messages
 )
 print(response.choices[0].message.content)
 messages.append({
  "role": "assistant",
  "content":response.choices[0].message.content
 })


