from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()
messages=[]
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


