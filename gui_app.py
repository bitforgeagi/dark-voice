import tkinter as tk
from tkinter import ttk
from tts_interface import TTSEngine
import threading
from models import list_available_voices

class TTSGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech")
        
        # Initialize TTS Engine
        print("Initializing TTS engine...")
        self.tts = TTSEngine()
        
        # Create and configure main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid columns to expand properly
        main_frame.columnconfigure(0, weight=1)
        
        # Create voice selection frame
        voice_frame = ttk.LabelFrame(main_frame, text="Select Voice", padding="10")
        voice_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        voice_frame.columnconfigure(0, weight=1)
        
        # Add voice dropdown
        self.voice_var = tk.StringVar(value=self.tts.voice_name)
        self.voice_dropdown = ttk.Combobox(
            voice_frame, 
            textvariable=self.voice_var,
            values=list_available_voices(),
            state='readonly',
            width=40
        )
        self.voice_dropdown.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5)
        self.voice_dropdown.bind('<<ComboboxSelected>>', self.change_voice)
        
        # Create input frame
        input_frame = ttk.LabelFrame(main_frame, text="Enter Text", padding="10")
        input_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(0, weight=1)
        
        # Add text input
        self.text_input = ttk.Entry(input_frame)
        self.text_input.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=(0, 5))
        self.text_input.bind('<Return>', self.speak_text)
        
        # Add speak button below text input
        self.speak_button = ttk.Button(
            input_frame, 
            text="Speak",
            command=self.speak_text,
            width=20
        )
        self.speak_button.grid(row=1, column=0, pady=(0, 5))
        
        # Add status label
        self.status_label = ttk.Label(main_frame, text="Ready", anchor="center")
        self.status_label.grid(row=2, column=0, sticky=(tk.W, tk.E))
        
        # Focus on text input
        self.text_input.focus()
        
        # Configure window resize behavior
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # Set minimum window size
        root.minsize(400, 200)
    
    def change_voice(self, event=None):
        """Handle voice change"""
        new_voice = self.voice_var.get()
        self.status_label.config(text=f"Changing voice to {new_voice}...")
        self.root.update()
        
        def voice_change_thread():
            try:
                self.tts.change_voice(new_voice)
                self.root.after(0, lambda: self.status_label.config(text="Ready"))
            except Exception as e:
                self.root.after(0, lambda: self.status_label.config(text=f"Error: {str(e)}"))
        
        threading.Thread(target=voice_change_thread, daemon=True).start()
    
    def speak_text(self, event=None):
        """Handle speak button click or Enter key"""
        text = self.text_input.get().strip()
        if text:
            self.speak_button.state(['disabled'])
            self.status_label.config(text="Generating...")
            
            def speak_thread():
                self.tts.speak(text)
                self.root.after(0, self.reset_ui)
            
            threading.Thread(target=speak_thread, daemon=True).start()
    
    def reset_ui(self):
        """Reset UI elements after speaking"""
        self.speak_button.state(['!disabled'])
        self.status_label.config(text="Ready")
        self.text_input.select_range(0, tk.END)

def main():
    root = tk.Tk()
    app = TTSGui(root)
    root.mainloop()

if __name__ == "__main__":
    main() 