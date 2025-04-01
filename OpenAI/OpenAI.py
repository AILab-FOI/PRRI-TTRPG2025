#!/usr/bin/env python
import os
import openai
openai.api_key = ""
system_prompt = "You have a role of a Dungeon Master assistent. Your task is to provide the Dungeon master with necessary info that he needs, in most cases that will be a backstory of a character, based on the description that the dungeon master gives you it is up to you to to give them a backstory and necessary details as to what the character is like, their attribues what they like and so on."

prompt = sys.stdin.read().strip()
if prompt:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )
    assistant_reply = response.choices[0].message.content
    print(assistant_reply)
else:
    print("No prompt provided!")
