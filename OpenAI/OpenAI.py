import os
import openai
import tkinter as tk
from tkinter import simpledialog, messagebox

class OpenAIChat:
    def __init__(self, api_key=None):

        if not api_key:
            api_key = self.ask_for_api_key()

        openai.api_key = api_key
        self.system_prompt = (
            "You have a role of a Dungeon Master assistant. Your task is to provide the Dungeon Master "
            "with necessary info that they need, in most cases that will be a backstory of a character. "
            "Based on the description that the Dungeon Master gives you, it is up to you to give them a backstory "
            "and necessary details such as what the character is like, their attributes, flaws, what they like and don't like, and so on."
        )

    def ask_for_api_key(self):
        root = tk.Tk()
        root.withdraw()

        api_key = simpledialog.askstring("API Key Required", "Please enter your OpenAI API key:")

        if not api_key:
            messagebox.showerror("Error", "API key is required to continue.")
            root.destroy()
            raise ValueError("API key not provided")

        root.destroy()
        return api_key

    def send_message(self, user_prompt):
        if not user_prompt:
            return "No prompt provided!"

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.5
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"
