# This is an empty Python file
# This is actually not a python script, just for my learning purpose to be familar with github.

import pyttsx3

def speak_text():
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)  # Set volume to maximum
    voices = engine.getProperty('voices')
    chinese_voice_id = None
    for voice in voices:
        print(f"Voice: {voice.name}, Languages: {voice.languages}")
        if 'zh' in voice.languages[0].decode('utf-8').lower():
            chinese_voice_id = voice.id
            break
    if chinese_voice_id:
        engine.setProperty('voice', chinese_voice_id)
    else:
        print("Chinese voice not found. Ensure Chinese language pack is installed.")
    text = input("Please enter a few sentences: ").encode('utf-8')
    engine.say(text.decode('utf-8'))
    engine.runAndWait()

if __name__ == "__main__":
    speak_text()