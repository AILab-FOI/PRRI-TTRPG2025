import tkinter as tk
import json
from tkinter import ttk
from tkinter import filedialog
import shutil
import pygame
import os
import subprocess
from OpenAI.OpenAI import OpenAIChat

from PIL import Image, ImageTk
import create_config
import generate

import sys
from tkinter import messagebox, filedialog

# Initialize the pygame mixer
pygame.mixer.init()

# Default
DEFAULT_LOCATION = ''
DEFAULT_BGM = ''
api_key = ''

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

def save_api_key(api_key, filename='config.json'):
    data = {'api_key': api_key}

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def read_api_key(filename='config.json'):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump({'api_key' : ''}, f, indent=4)
        return ''

    with open(filename, 'r')as f:
        data = json.load(f)

    api_key = data.get('api_key')
    return api_key


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
        
        style = ttk.Style()
        style.theme_use('default')  # Use 'default' to allow custom colors (important!)

        # Style for a regular Frame
        style.configure("Custom.TFrame", background="lightgreen")

        # Style for a LabelFrame (frame with a title)
        style.configure("Custom.TLabel", 
            background="lightgreen", 
            foreground="darkblue", 
            font=("Arial", 14, "bold"))
        
        # Style for Button
        style.configure("Custom.TButton",
            background="darkblue",
            foreground="lightgreen",
            font=("Arial", 10, 'bold'))

        # Style for Checkbutton
        style.configure("Custom.TCheckbutton",
            background="lightgreen",
            foreground="darkblue",
            font=("Arial", 10, 'bold'))

        # Style for Radiobutton
        style.configure("Custom.TRadiobutton",
            background="lightgreen",
            foreground="darkblue",
            font=("Arial", 10, 'bold'))
        
        # Top frames
        self.create_option_frame("Backgrounds", self.selected_scene, self.config_data['Backgrounds'])
        self.create_check_frame("Characters", self.selected_show, self.config_data['Characters'])
        self.create_check_frame("NPCs", self.selected_show, self.config_data['NPCs'])
        self.create_sound_effects_frame("Sound effects", self.config_data['Sound effects'])
        self.create_option_frame("Background music", self.selected_bgm, self.config_data['Background music'])

        # Bottom frame
        bottom_frame = ttk.Frame(self, style="Custom.TFrame")
        bottom_frame.pack(side="bottom", fill="x", padx=5, pady=10)

        label = ttk.Label(bottom_frame, text="Pitanje za AI:", style="Custom.TLabel")
        label.pack(anchor="w", pady=(0, 5))

        self.text_input = tk.Text(bottom_frame, height=3, wrap="word")
        self.text_input.pack(side="left", expand=True, fill="both", padx=(0, 10))

        scrollbar = ttk.Scrollbar(bottom_frame, orient="vertical", command=self.text_input.yview)
        scrollbar.pack(side="right", fill="y")

        self.text_input.configure(yscrollcommand=scrollbar.set)


        send_button = ttk.Button(bottom_frame, text="Send", command=self.on_send,  style="Custom.TButton")
        send_button.pack(side="right")

        # OK Button
        ttk.Button(self, text="OK", command=self.on_ok, style="Custom.TButton").pack(side="left", padx=5)
        ttk.Button(self, text="Run game", command=self.on_run, style="Custom.TButton").pack(side="left", padx=5)

    def create_check_frame(self, title, variable_dict, options):
        
        title_label = ttk.Label(self, text=title, style="Custom.TLabel", anchor="w")
        title_label.pack(fill="x", padx=5, pady=(5, 0))  # Only top padding
        
        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(fill="x", padx=5)  # Padding bottom only
        
        frame = ttk.Frame(self, style="Custom.TFrame")
        frame.pack(fill='both', expand=True, padx=5, pady=(0, 5))

        for i, option in enumerate(options):
            # Modifikacije za brisanje uz svaku opciju
            row = i // 6
            col = (i % 6) * 2
            ttk.Checkbutton(frame, text=option, variable=variable_dict[option], style="Custom.TCheckbutton").grid(row=row, column=col, sticky='w')
            del_button = ttk.Button(frame, text="Obriši", width=6, command=lambda opt=option: self.remove_item_from_section(title, opt), style='Custom.TButton')
            del_button.grid(row=row, column=col + 1, sticky='w', padx=5)

        # Umetni gumb (nemojte ovo mjenjati bez da proučite kako funkcionira!)
        num_columns = 13  
        insert_button = ttk.Button(frame, text="Umetni", command=lambda: self.insert_file(title), style='Custom.TButton')
        insert_button.grid(row=0, column=num_columns - 1, sticky='e', padx=(40, 5))

    def create_option_frame(self, title, variable, options):
        
        title_label = ttk.Label(self, text=title, style="Custom.TLabel", anchor="w")
        title_label.pack(fill="x", padx=5, pady=(10, 0))  # Only top padding
        
        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(fill="x", padx=5)  # Padding bottom only
        
        frame = ttk.Frame(self, style="Custom.TFrame")
        frame.pack(fill='both', expand=True, padx=5, pady=(0, 10))
        
        for i, option in enumerate(options):
            # Modifikacije za brisanje uz svaku opciju
            row = i // 6
            col = (i % 6) * 2
            ttk.Radiobutton(frame, text=option, variable=variable, value=option, style='Custom.TRadiobutton').grid(row=row, column=col, sticky='w')
            del_button = ttk.Button(frame, text="Obriši", width=6, command=lambda opt=option: self.remove_item_from_section(title, opt), style='Custom.TButton')
            del_button.grid(row=row, column=col + 1, sticky='w', padx=5)

        # Umetni gumb (nemojte ovo mjenjati bez da proučite kako funkcionira!)
        num_columns = 13  
        insert_button = ttk.Button(frame, text="Umetni", command=lambda: self.insert_file(title), style='Custom.TButton')
        insert_button.grid(row=0, column=num_columns - 1, sticky='e', padx=(40, 5))

    def create_sound_effects_frame(self, title, options):
        
        title_label = ttk.Label(self, text=title, style="Custom.TLabel", anchor="w")
        title_label.pack(fill="x", padx=5, pady=(10, 0))  # Only top padding
        
        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(fill="x", padx=5)  # Padding bottom only
        
        frame = ttk.Frame(self, style="Custom.TFrame")
        frame.pack(fill='both', expand=True, padx=5, pady=(0, 10))
        
        for i, option in enumerate(options):
            # Modificirano za brisanje
            row = i // 6
            col = (i % 6) * 2
            play_button = ttk.Button(frame, text=option, command=lambda opt=option: self.on_sound_button_click(opt), style="Custom.TButton")
            play_button.grid(row=row, column=col, sticky='w')
            del_button = ttk.Button(frame, text="Obriši", width=6, command=lambda opt=option: self.remove_item_from_section(title, opt), style="Custom.TButton")
            del_button.grid(row=row, column=col + 1, sticky='w', padx=5)

        
       # Umetni gumb (nemojte ovo mjenjati bez da proučite kako funkcionira!)
        num_columns = 13  
        insert_button = ttk.Button(frame, text="Umetni", command=lambda: self.insert_file(title), style="Custom.TButton")
        insert_button.grid(row=0, column=num_columns - 1, sticky='e', padx=(40, 5))

    def on_sound_button_click(self, sound_name):
        self.selected_sound = sound_name  # Update the selected_sound with the clicked sound's name
        play_sound(sound_name)  # Play the sound

    def on_ok(self):
        write_json(self.selected_scene, self.selected_show, self.selected_sound, self.selected_bgm)

    def on_run(self):
        
        renpy_path = create_config.get_or_select_renpy_path()
        current_dir = os.getcwd()

        if renpy_path:
            print(f"Pokretanje Ren'Pya s: {renpy_path}")
            subprocess.Popen([renpy_path, current_dir])
        else:
            messagebox.showerror("Greška", "RenPy nije odabran. Igra se neće pokrenuti.")
    
    def on_send(self):
        global api_key

        if not api_key:
            api_key = OpenAIChat.ask_for_api_key(self)
            save_api_key(api_key)

        chat = OpenAIChat(api_key)

        tekstZaGpt = self.text_input.get("1.0", "end").strip()
        reply = chat.send_message(tekstZaGpt)
        
        if not tekstZaGpt:
            return  # ne radi ništa ako je polje prazno (mora bit tu inače ne radi?!) 
        
        if self.send_window and self.send_window.winfo_exists():
            # Ako prozor već postoji, dodaj novi tekst i zadrži stari
            self.send_text_area.insert("end", f"\n\nUpit: {tekstZaGpt}")
            self.send_text_area.insert("end", f"\n{reply}")
            self.send_text_area.see("end")  # scroll na dno kad se refresha
            self.text_input.delete("1.0", "end") #briše upit u text boxu
        else:
            # Otvori novi prozor
            self.send_window = tk.Toplevel(self)
            self.send_window.title("Odgovor AI-a")
            self.send_window.geometry("800x600")
            self.text_input.delete("1.0", "end")
            self.send_window.resizable(False, False)  #sprječava resize

           #učitavanje slike (bilo bi dobro da ostane di je)
            bg_image = Image.open("resursi_UI/OkvirOdgovor.webp")
            try:
             resample_filter = Image.Resampling.LANCZOS
            except AttributeError:
              resample_filter = Image.ANTIALIAS  #ako slučajno nema dobru vezciju iz PIL
            bg_image = bg_image.resize((800, 600), resample_filter)
            bg_photo = ImageTk.PhotoImage(bg_image)

          # Canvas i slika
            canvas = tk.Canvas(self.send_window, width=800, height=600, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=bg_photo, anchor="nw")
            self.send_window.bg_photo = bg_photo

         # Frame unutar canvasa za sadržaj, centriran
            frame = ttk.Frame(canvas)
            canvas.create_window(400, 300, window=frame, anchor="center", width=535, height=410)  

         # Scrollbar i text area
            scrollbar = ttk.Scrollbar(frame)
            scrollbar.pack(side="right", fill="y")

            self.send_text_area = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set)
            self.send_text_area.pack(side="left", fill="both", expand=True)
            scrollbar.config(command=self.send_text_area.yview)

            #tag za boldani tekst
            self.send_text_area.tag_configure("bold", font=("TkDefaultFont", 10, "bold"))

           #tekst s tagovima
            self.send_text_area.insert("1.0", "Upit: ", "bold")
            self.send_text_area.insert("end", tekstZaGpt + "\n", "bold")
            self.send_text_area.insert("end", reply)

    # Brisanje fajlova
    def remove_item_from_section(self, section_name, item_name):
        if item_name in self.config_data[section_name]:
            self.config_data[section_name].remove(item_name)

            # Mape za fajlove
            section_paths = {
                "Characters": os.path.join("game", "images", "characters"),
                "NPCs": os.path.join("game", "images", "npcs"),
                "Backgrounds": os.path.join("game", "images", "locations"),
                "Sound effects": os.path.join("game", "audio", "soundeffects"),
                "Background music": os.path.join("game", "audio", "bcgsound")
            }

            if section_name in section_paths:
                directory = section_paths[section_name]
                extensions = [".png", ".jpg", ".jpeg", ".webp", ".bmp", ".mp3", ".wav"]
                for ext in extensions:
                    file_path = os.path.join(directory, item_name + ext)
                    if os.path.exists(file_path):
                        os.remove(file_path)
                        break

            if section_name in ["Characters", "NPCs"]:
                if item_name in self.selected_show:
                    del self.selected_show[item_name]

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

    api_key = read_api_key()

    app.mainloop()