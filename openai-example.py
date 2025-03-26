#!/usr/bin/env python
import os
import openai
openai.api_key = os.environ.get("OPENAI_API_KEY")

while True:
    prompt = input( 'Unesi pitanje>' )

    response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}        
            ]
        )
    assistant_reply = response.choices[0].message.content

    print( assistant_reply )
