# This is an empty Python file
# This is actually not a python script, just for my learning purpose to be familar with github.

import pyttsx3

def speak_text():
    engine = pyttsx3.init()
    text = input("Please enter a few sentences: ")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak_text()