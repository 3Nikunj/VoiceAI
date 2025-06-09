# Local Voice-Driven Conversational AI

This project is a prototype for a local, voice-driven conversational AI. It uses open-source models for the Large Language Model (LLM), Speech-to-Text (STT), and Text-to-Speech (TTS) components.

## Project Structure

- `main.py`: The main Python script that orchestrates the AI's components.
- `requirements.txt`: Lists the Python dependencies for this project.
- `config.py` (optional): For storing configuration like model names, API keys (if any), etc.
- `modules/`: Directory to potentially house separate Python modules for LLM, STT, and TTS logic if the project grows.

## Components

1.  **The "Brain" (Large Language Model - LLM)**: Understands queries and generates text responses. This prototype will aim to interface with a locally running LLM (e.g., via Ollama or LM Studio).
2.  **The "Ears" (Speech-to-Text - STT)**: Converts spoken words into text for the LLM.
3.  **The "Mouth" (Text-to-Speech - TTS)**: Converts the LLM's text response into audible speech.

## Setup and Running

1.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Set up a Local LLM Runner**:

    - Install and run [Ollama](https://ollama.ai/) or [LM Studio](https://lmstudio.ai/).
    - Download a suitable lightweight model (e.g., Llama 3.1 8B, Vicuna-13B, Qwen2 7B).
    - Ensure the LLM is accessible (e.g., Ollama serves models via an API by default).

3.  **Configure STT and TTS models** (Details to be added as implemented).

4.  **Run the Application**:
    ```bash
    python main.py --voice
    ```

## Development Steps (Based on User Blueprint)

- [x] **Step 0: Project Initialization** (README, requirements.txt, initial main.py)
- [ ] **Step 1: Set Up the "Brain" (The Local LLM)**
  - [ ] Choose a Model Runner (User choice: Ollama or LM Studio).
  - [ ] Select a Lightweight Model (User suggestions: Llama 3.1 (8B), Vicuna-13B, Qwen2 (7B), OpenHermes 2.5 Mistral (7B)).
  - [ ] Create a Basic Chat Interface in `main.py` to send prompts to the local LLM and print responses.
- [ ] **Step 2: Implement the "Ears" (Speech-to-Text)**
  - [ ] Find an Open-Source STT Library (e.g., from Hugging Face).
  - [ ] Integrate microphone input and STT model into `main.py`.
- [ ] **Step 3: Add the "Mouth" (Text-to-Speech)**
  - [ ] Select an Open-Source TTS Engine (e.g., Coqui TTS, Piper).
  - [ ] Integrate TTS engine into `main.py` to voice LLM responses.
