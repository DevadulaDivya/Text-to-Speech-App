import tkinter as tk
from tkinter import ttk
from gtts import gTTS
from playsound import playsound
import os

def convert_to_speech():
    text = text_entry.get("1.0", "end-1c")
    language = language_combobox.get()
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")

root = tk.Tk()
root.title("Text to Speech")

# Text Entry
text_entry = tk.Text(root, height=10, width=50)
text_entry.grid(row=0, column=0, padx=10, pady=10)

# Language Combobox
languages = ['en', 'es', 'fr', 'de'] # Add more languages as needed
language_combobox = ttk.Combobox(root, values=languages)
language_combobox.current(0) # Set default language to English
language_combobox.grid(row=0, column=1, padx=10, pady=10)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_to_speech)
convert_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()