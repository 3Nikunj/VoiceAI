import ollama
import speech_recognition as sr
import pyttsx3
import sys

# --- Configuration ---
LLM_MODEL = 'llama3:8b'  # Default model, user can change this
# For STT, we'll use SpeechRecognition, which can use various engines.
# For TTS, pyttsx3 is a simple offline engine.

# --- LLM Interaction (Step 1) ---
def get_llm_response(prompt, model=LLM_MODEL):
    """Sends a prompt to the local LLM and returns the response."""
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        print(f"Error communicating with LLM ({model}): {e}")
        print("Please ensure Ollama is running and the model is available.")
        print("You can list available models with 'ollama list'.")
        return None

# --- Speech-to-Text (Step 2) ---
def listen_for_voice():
    """Listens for voice input and transcribes it to text."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("No speech detected within the time limit.")
            return None

    try:
        print("Transcribing...")
        text = recognizer.recognize_whisper(audio, model="base") # Using local Whisper 'base' model
        # Alternative: recognizer.recognize_google(audio) # Requires internet
        # For fully offline, one might need to set up a local Whisper model or use CMU Sphinx (recognizer.recognize_sphinx(audio))
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    # sr.RequestError is typically for online services, less relevant for local recognize_whisper
    # However, keeping a general exception handler is good practice.
    # except sr.RequestError as e:
    #     print(f"Could not request results from speech recognition service; {e}")
    #     return None
    except Exception as e:
        print(f"An unexpected error occurred during speech recognition: {e}")
        return None

# --- Text-to-Speech (Step 3) ---
def speak_text(text):
    """Converts text to speech and plays it."""
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in TTS: {e}")

# --- Main Application Logic ---
def main_text_chat():
    """Runs a simple text-based chat loop with the LLM."""
    print(f"Starting text chat with {LLM_MODEL}. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        if user_input:
            prompt = f"You are a helpful assistant. User: {user_input} Assistant:"
            response = get_llm_response(prompt)
            if response:
                print(f"AI: {response}")

def main_voice_chat():
    """Runs a voice-based chat loop with STT, LLM, and TTS."""
    print(f"Starting voice chat with {LLM_MODEL}. Say 'goodbye' to exit.")
    speak_text(f"Hello! I am your voice assistant, powered by {LLM_MODEL.split(':')[0]}. How can I help you today?")

    while True:
        print("\nListening for your command...")
        user_input_text = listen_for_voice()

        if user_input_text:
            if "goodbye" in user_input_text.lower():
                speak_text("Goodbye!")
                break
            
            prompt = f"You are a helpful assistant. User: {user_input_text} Assistant:"
            llm_response = get_llm_response(prompt)

            if llm_response:
                print(f"AI: {llm_response}")
                speak_text(llm_response)
            else:
                speak_text("I had trouble getting a response from the language model.")
        else:
            # speak_text("I didn't catch that. Could you please repeat?") # Optional: prompt user to repeat
            print("No valid input received or transcription failed.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--voice':
        main_voice_chat()
    else:
        print("Starting in text mode. To start in voice mode, run: python main.py --voice")
        main_text_chat()