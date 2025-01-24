import torch
from models import build_model, load_voice, generate_speech
import sounddevice as sd
import numpy as np
import queue
import threading
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TTSEngine:
    """Simple interface for text-to-speech functionality"""
    
    def __init__(self, voice_name: str = "af_bella", device: Optional[str] = None):
        """Initialize TTS engine with specified voice"""
        # Determine device
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        self.voice_name = voice_name
        logger.info(f"Initializing TTS engine with voice '{voice_name}' on {self.device}")
        
        try:
            # Initialize model and voice
            self.model = build_model("kokoro-v0_19.pth", self.device)
            self.voice = load_voice(voice_name, self.device)
            self.sample_rate = 22050
            
            # Setup audio queue
            self.audio_queue = queue.Queue()
            self.is_speaking = False
            
            # Start audio playback thread
            self.playback_thread = threading.Thread(target=self._audio_player, daemon=True)
            self.playback_thread.start()
        except Exception as e:
            logger.error(f"Failed to initialize TTS engine: {e}")
            raise
    
    def change_voice(self, voice_name: str) -> None:
        """Change the current voice"""
        try:
            logger.info(f"Changing voice to: {voice_name}")
            self.voice = load_voice(voice_name, self.device)
            self.voice_name = voice_name
        except Exception as e:
            logger.error(f"Error changing voice: {e}")
            raise
    
    def speak(self, text: str) -> None:
        """Convert text to speech and play it"""
        if not text.strip():
            logger.warning("Empty text provided")
            return
            
        try:
            logger.info(f"Generating speech for: {text}")
            audio, _ = generate_speech(self.model, text, self.voice, device=self.device)
            if audio is not None:
                self.audio_queue.put(audio)
            else:
                logger.error("Failed to generate speech - no audio generated")
        except Exception as e:
            logger.error(f"Error generating speech: {e}")
            raise
    
    def _audio_player(self):
        """Background thread for audio playback"""
        while True:
            try:
                audio = self.audio_queue.get()
                self.is_speaking = True
                
                # Normalize audio
                audio = np.float32(audio)
                if np.max(np.abs(audio)) > 0:  # Avoid division by zero
                    audio = audio / np.max(np.abs(audio))
                
                # Play audio
                sd.play(audio, self.sample_rate)
                sd.wait()
            except Exception as e:
                logger.error(f"Error playing audio: {e}")
            finally:
                self.is_speaking = False
    
    def stop(self):
        """Stop current speech and clear queue"""
        logger.info("Stopping speech and clearing queue")
        while not self.audio_queue.empty():
            self.audio_queue.get()
            
    def __del__(self):
        """Cleanup when object is deleted"""
        self.stop()

if __name__ == "__main__":
    # Test the TTS engine
    engine = TTSEngine()
    test_text = "This is a test of the text to speech system."
    print(f"Speaking: {test_text}")
    engine.speak(test_text)
    input("Press Enter to exit...") 
            