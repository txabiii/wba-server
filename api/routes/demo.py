from flask import Blueprint
import os
import openai 
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

demo_bp = Blueprint('demo_bp', __name__)

@demo_bp.route('/demo')
def demo():
  system_prompt = """You are a world-building expert. Draw inspiration from fantasy and sci-fi books. Names should unique. Generate two properties only with name and value. Write description in max 5 sentences. Generate a color that fits the concept in HEX format. Follow instructions strictly."""

  user_prompt = """Generate a unique world-building concept which could be a character, creature, place, object, skills, events, etc. Use the JSON format: {"name":"-","type": "-","properties":{"-": "-","-": "-"},"description": "-","color":"-"}"""

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": user_prompt}
    ]
  )

  output = completion['choices'][0]['message']['content']

  try:
    parsed_output = json.loads(completion['choices'][0]['message']['content'])
    output = json.dumps({"status": "success", "content": parsed_output})
  except json.JSONDecodeError as e:
    output = json.dumps({"status": "fail", "content" : "error"})
    
  return output