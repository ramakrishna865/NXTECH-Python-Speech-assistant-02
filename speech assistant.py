import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for a command, please say something...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def respond_with_text(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("start response.mp3")  # Opens the generated mp3 file

if __name__ == "__main__":
    while True:
        command = listen_for_command()
        if "hello" in command:
            response = "Hello there! How can I assist you?"
        elif "how are you" in command:
            response = "I'm just a program, but I'm here to help!"
        elif "goodbye" in command:
            response = "Goodbye! Have a great day!"
            respond_with_text(response)
            break
        elif "open youtube" in command:
            response = "Opening YouTube..."
            respond_with_text(response)
            webbrowser.open("https://www.youtube.com")
        elif "open google" in command:
            response = "Opening Google..."
            respond_with_text(response)
            webbrowser.open("https://www.google.com")
        elif "open whatsapp web" in command:
            response = "Opening WhatsApp Web..."
            respond_with_text(response)
            webbrowser.open("https://web.whatsapp.com")
        else:
            response = "Sorry, I didn't understand that."
        
        print(response)
        respond_with_text(response)
