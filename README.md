<img width="624" alt="Screenshot 2025-01-23 at 9 50 58 PM" src="https://github.com/user-attachments/assets/25313946-ee70-4d2e-9858-d4506861ad2e" />

# Dark Voice Demo

A Python GUI application demonstrating the Dark Voice TTS engine, a simple wrapper for the Kokoro-82M TTS model. This educational project helps developers understand how to implement text-to-speech functionality in Python applications.

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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

Licensed under the Apache License, Version 2.0.
© 2025 Bitforge Dynamics LLC. All rights reserved.

## Acknowledgments

- Based on the Kokoro-82M TTS model
- Uses espeak-ng for phonemization
- Built with PyTorch and Hugging Face Transformers
