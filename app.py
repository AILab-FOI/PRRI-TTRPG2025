import tkinter as tk
import json
from tkinter import ttk
from tkinter import filedialog
import shutil
import pygame
import os
import subprocess

import create_config
import generate

# Initialize the pygame mixer
pygame.mixer.init()

# Default
DEFAULT_LOCATION = ''
DEFAULT_BGM = ''

# Parse the configuration file
def parse_config(filename):
    with open(filename, 'r') as file:
        content = file.read()

    sections = content.split('# ')[1:]
    parsed_data = {}
    for section in sections:
        title, *items = section.strip().split('\n')
        parsed_data[title.strip()] = [item.strip() for item in items]

    return parsed_data

# Write to the JSON file
def write_json(selected_scene, selected_show, selected_sound, selected_bgm):
    data = {
        "scene": selected_scene.get() or DEFAULT_LOCATION,
        "show": [item for item in selected_show if selected_show[item].get()][:3],
        "sound": selected_sound,  # Directly use the string value of the last clicked sound
        "bgm": selected_bgm.get() or DEFAULT_BGM
    }
    with open('game/next.json', 'w') as file:
        json.dump(data, file, indent=4)

# Function to play sound
def play_sound(sound_name):
    sound_path = os.path.join('game', 'audio', 'soundeffects', f"{sound_name}.mp3")
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

# Main GUI Application
class Application(tk.Tk):
    def __init__(self, config_data):
        super().__init__()
        self.title("Game Configuration")
        self.config_data = config_data

       # refernece koje se koriste za refreshanje (nemoj micat nigdje/uključeno)
        self.send_window = None
        self.send_text_area = None

        self.style = ttk.Style()
        self.style.theme_use('clam')  # or try 'clam', 'alt', 'default', 'classic' etc.

        self.selected_scene = tk.StringVar()
        self.selected_show = {item: tk.BooleanVar() for item in config_data['NPCs'] + config_data['Characters']}
        self.selected_sound = ""  # Updated to store the last clicked sound as a string
        self.selected_bgm = tk.StringVar()

        self.create_frames()

    def refresh_ui(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_frames()

    def insert_file(self, section_name):
        file_path = filedialog.askopenfilename(title="Odaberi datoteku")
        if file_path:
            self.add_item_to_section(section_name, file_path)

    def add_item_to_section(self, section_name, file_path):
        print(section_name)
        # Dohvati path
        name = os.path.splitext(os.path.basename(file_path))[0]

        # Dodaj u config_data
        self.config_data[section_name].append(name)


        # Postavi datoteku u odredjenu mapu
        # Definiraj mapu sekcija i njihovih putanja
        section_paths = {
            "Characters": os.path.join("game", "images", "characters"),
            "NPCs": os.path.join("game", "images", "npcs"),
            "Backgrounds": os.path.join("game", "images", "locations"),
            "Sound effects": os.path.join("game", "audio", "soundeffects"),
            "Background music": os.path.join("game", "audio", "bcgsound")
        }

        # Provjera postoji li odgovarajuci put
        if section_name in section_paths:
            dest_dir = section_paths[section_name]
            dest = os.path.join(dest_dir, os.path.basename(file_path))

            # Provjera da li datoteka već postoji
            if os.path.exists(dest):
                tk.messagebox.showwarning("Datoteka već postoji", f"Datoteka {os.path.basename(file_path)} već postoji u {dest_dir}.")
                return

            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy(file_path, dest)


        # Ovo slozi da bude checkbox
        if section_name in ["Characters", "NPCs"]:
            self.selected_show[name] = tk.BooleanVar()

        # Refresh
        self.refresh_ui()

    def create_frames(self):
        # Top frames
        self.create_option_frame("Backgrounds", self.selected_scene, self.config_data['Backgrounds'])
        self.create_check_frame("Characters", self.selected_show, self.config_data['Characters'])
        self.create_check_frame("NPCs", self.selected_show, self.config_data['NPCs'])
        self.create_sound_effects_frame("Sound effects", self.config_data['Sound effects'])
        self.create_option_frame("Background music", self.selected_bgm, self.config_data['Background music'])

        # Bottom frame
        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        label = ttk.Label(bottom_frame, text="Pitanje za AI:")
        label.pack(anchor="w", pady=(0, 5))

        self.text_input = tk.Text(bottom_frame, height=3, wrap="word")
        self.text_input.pack(side="left", expand=True, fill="both", padx=(0, 10))

        send_button = ttk.Button(bottom_frame, text="Send", command=self.on_send)
        send_button.pack(side="right")

        # OK Button
        ttk.Button(self, text="OK", command=self.on_ok).pack(side="right")
        ttk.Button(self, text="Run game", command=self.on_run).pack(side="left")

    def create_check_frame(self, title, variable_dict, options):
        frame = ttk.LabelFrame(self, text=title)
        frame.pack(fill='both', expand=True, pady=10)

        for i, option in enumerate(options):
            ttk.Checkbutton(frame, text=option, variable=variable_dict[option]).grid(row=i // 4, column=i % 4, sticky='w')

        # Umetni gumb
        insert_button = ttk.Button(frame, text="Umetni", command=lambda: self.insert_file(title))
        insert_button.grid(row=(len(options) // 4) + 1, column=0, sticky='w', pady=5)

    def create_option_frame(self, title, variable, options):
        frame = ttk.LabelFrame(self, text=title)
        frame.pack(fill='both', expand=True)
        for i, option in enumerate(options):
            ttk.Radiobutton(frame, text=option, variable=variable, value=option).grid(row=i // 4, column=i % 4, sticky='w')

        # Umetni gumb
        insert_button = ttk.Button(frame, text="Umetni", command=lambda: self.insert_file(title))
        insert_button.grid(row=(len(options) // 4) + 1, column=0, sticky='w', pady=5)

    def create_sound_effects_frame(self, title, options):
        frame = ttk.LabelFrame(self, text=title)
        frame.pack(fill='both', expand=True)
        for i, option in enumerate(options):
            button = ttk.Button(frame, text=option, command=lambda opt=option: self.on_sound_button_click(opt))
            button.grid(row=i // 4, column=i % 4, sticky='w')
        
        # Umetni gumb
        insert_button = ttk.Button(frame, text="Umetni", command=lambda: self.insert_file(title))
        insert_button.grid(row=(len(options) // 4) + 1, column=0, sticky='w', pady=5)

    def on_sound_button_click(self, sound_name):
        self.selected_sound = sound_name  # Update the selected_sound with the clicked sound's name
        play_sound(sound_name)  # Play the sound

    def on_ok(self):
        write_json(self.selected_scene, self.selected_show, self.selected_sound, self.selected_bgm)

    def on_run(self):
        subprocess.Popen([ "../renpy-8.3.7-sdk/renpy.sh", os.getcwd() ])

    def on_send(self):
        odgovorOdGpt = 'placeholder_odgovor'
        tekstZaGpt = self.text_input.get("1.0", "end").strip()
        if not tekstZaGpt:
            return  # ne radi ništa ako je polje prazno (mora bit tu inače ne radi?!) 
        
        if self.send_window and self.send_window.winfo_exists():
            # Ako prozor već postoji, dodaj novi tekst i zadrži stari
            self.send_text_area.insert("end", f"\n\nUpit: {tekstZaGpt}")
            self.send_text_area.insert("end", f"\n{odgovorOdGpt}")
            self.send_text_area.see("end")  # scroll na dno kad se refresha
        else:
            # Otvori novi prozor
            self.send_window = tk.Toplevel(self)
            self.send_window.title("Odgovor AI-a")
            self.send_window.geometry("500x400")

            frame = ttk.Frame(self.send_window)
            frame.pack(fill="both", expand=True, padx=10, pady=10)

            scrollbar = ttk.Scrollbar(frame) #malo promjenjeni scroll ali radi
            scrollbar.pack(side="right", fill="y")

            self.send_text_area = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set)
            self.send_text_area.pack(side="left", fill="both", expand=True)
            scrollbar.config(command=self.send_text_area.yview)
            text_area = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set)
            text_area.pack(side="left", fill="both", expand=True)

            scrollbar.config(command=text_area.yview)

            self.send_text_area.insert("1.0", f"Upit: {tekstZaGpt}\n")
            tekstZaGpt = self.text_input.get("1.0", "end").strip()
            self.send_text_area.insert("end", f"{odgovorOdGpt}")

# Run the application
if __name__ == "__main__":
    create_config.main( overwrite=True )
    current_dir = os.path.dirname(os.path.realpath(__file__))
    config_file_path = os.path.join(current_dir, 'interface.conf')
    data = generate.parse_config( config_file_path )
    characters, npcs, sound_effects, backgrounds, bgms = data[ "Characters" ], data[ "NPCs" ], data[ "Sound effects" ], data[ "Backgrounds" ], data[ "Background music" ]
    DEFAULT_LOCATION = backgrounds[ 0 ]
    DEFAULT_BGM = bgms[ 0 ]

    # Generate the complete script.rpy file
    generate.generate_script(characters, npcs, backgrounds, current_dir, True)
    config = parse_config('interface.conf')
    app = Application(config)
    app.mainloop()
