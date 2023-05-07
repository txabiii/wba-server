from flask import Blueprint
import os
import openai 
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

demo_bp = Blueprint('demo_bp', __name__)

@demo_bp.route('/demo')
def demo():
  system_prompt = """Create unique concepts in a fictional world. Names should not be in dictionary. Generate two properties only with name and value. Write description in max 3 sentences. Generate a color that fits the concept in HEX format. Follow my instructions strictly."""

  user_prompt = """Generate a world-building concept. Use the JSON format: {"name":"-","type": "-","properties":{"-": "-","-": "-"},"description": "-","color":"-"}"""

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
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