from flask import Blueprint
import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

demo_bp = Blueprint('demo_bp', __name__)

@demo_bp.route('/demo')
def demo():
  system_prompt = """Create unique concepts in a fictional world. Names should not be in dictionary. You will generate two properties with its name and value. Write description in max 3 sentences. Write output in the JSON format below:
  {"name":"-","type": "-","properties":{"-": "-","-": "-"},"description": "-"}
  Follow my instructions strictly."""

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": "Write a world building object with no context. Use your inventiveness."}
    ]
  )

  output = completion['choices'][0]['message']['content']

  try:
    parsed_output = json.loads(completion['choices'][0]['message']['content'])
    output = json.dumps({"status": "success", "content": parsed_output})
  except json.JSONDecodeError as e:
    output = json.dumps({"status": "fail", "content" : e})
    
  return output