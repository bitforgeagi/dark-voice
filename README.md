
![u9855564576_create_a_cypher_graphic_for_DARK_VOICE_circuit_fade_f6c18a86-7094-48cf-bb18-11ab6279d2ef](https://github.com/user-attachments/assets/ef96d5ad-fe59-4881-b937-2ce420f134c8)

# Dark Voice Demo

A Python GUI application demonstrating the Dark Voice TTS engine. Learn how to build a simple wrapper for the [Kokoro-82M TTS model](https://huggingface.co/hexgrad/Kokoro-82M/tree/main). This educational project helps developers understand how to implement text-to-speech functionality in Python applications. 100% offline Text-to-Speech! (after model / voice downloads)

<img width="624" alt="Screenshot 2025-01-23 at 9 50 58 PM" src="https://github.com/user-attachments/assets/25313946-ee70-4d2e-9858-d4506861ad2e" />

## Prerequisites

- Python 3.11 or higher
- espeak-ng installed on your system

### Installing espeak-ng

#### Windows
Download from [espeak-ng releases](https://github.com/espeak-ng/espeak-ng/releases)

#### macOS
```bash
brew install espeak-ng
```

#### Linux
```bash
sudo apt install espeak-ng
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bitforgeagi/dark-voice.git
cd dark-voice
```

2. Create and activate virtual environment:
```bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install PyTorch (important to install first!):
```bash
pip install torch torchvision torchaudio
```

4. Install other requirements:
```bash
pip install -r requirements.txt
```

## Usage

Run the GUI application:
```bash
python gui_app.py
```

The application will:
1. Download necessary model files on first run
2. Present a simple interface for text-to-speech conversion
3. Allow you to select different voices
4. Convert your text input to speech

## Project Structure

```
dark-voice-demo/
├── gui_app.py         # GUI interface
├── models.py          # Model management and voice loading
├── tts_interface.py   # TTS engine interface
├── requirements.txt   # Project dependencies
└── README.md         # This file
```

## Available Voices

- af_bella (default)
- af_nicole
- af_sarah
- af_sky
- am_adam
- am_michael
- bf_emma
- bf_isabella
- bm_george
- bm_lewis

## License

Licensed under the Apache License, Version 2.0.
© 2025 Bitforge Dynamics LLC. All rights reserved.

## Acknowledgments

- Based on the Kokoro-82M TTS model
- Uses espeak-ng for phonemization
- Built with PyTorch and Hugging Face Transformers
