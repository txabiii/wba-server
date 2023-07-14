# Scrollarium server

This is a **Python Flask** server that functions as the backend for Scrollarium which you can see its code, and learn more about it [here](http:example.com).

## About

The server handles several functionalities such as demo, login, sign up and verification functions of the frontend. Scrollarium is still a work-in-progress and as of now only the demo function is utilized by the deployed website [here](https://scrollarium.vercel.app/)

## Demo.py

The route demo.py makes use of OpenAi's API to generate a world building concept. The prompts used are shown below:

```
  system_prompt = """You are a world-building expert. Draw inspiration from fantasy and sci-fi books. Names should unique. Generate two properties only with name and value. Write description in max 5 sentences. Generate a color that fits the concept in HEX format. Follow instructions strictly."""

  user_prompt = """Generate a unique world-building concept which could be a character, creature, place, object, skills, events, etc. Use the JSON format: {"name":"-","type": "-","properties":{"-": "-","-": "-"},"description": "-","color":"-"}"""

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": user_prompt}
    ]
  )

```

## Created by

The Scrollarium backend server was created by Txabi Guerrero. For inquiries you can contact me at txabiguerrero2000@gmail.com.

## License

Just a simple [MIT license](https://opensource.org/license/mit/)
