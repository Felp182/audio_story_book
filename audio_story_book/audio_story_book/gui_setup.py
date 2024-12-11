import tkinter as tk
import pygame

pygame.mixer.init()

class AudioStoryBook():
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Story Book")

        self.bg_music = pygame.mixer.Sound("Path to background music ") # Later I want to use procedural or AI to generate this
        self.bg_music.play(loops=1, fade_ms=2000)

        #GUI Area
        self.title_label = tk.Label(self.root, text="Your Audio Book Begins!", font=("Arial, 24"))
        self.title_label.pack(pady=20)

        self.story_text = tk.Label(self.root, text="Welcome!", font=("Arial", 16))
        self.story_text.pack(pady= 10)

       # self.button_choice = tk.Button(self.root, text=("Tell me where you want to explore ?")) # Here I want to use speech recognition so the player can tell its story, with that I want to procedural generate the audio or ambience

        

root = tk.Tk()

app = AudioStoryBook(root)