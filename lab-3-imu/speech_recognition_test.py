"""Guide from https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py"""

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)

try:
    print("Vosk thinks you said " + r.recognize_vosk(audio))
except sr.UnknownValueError:
        print("Could not understand")
except sr.RequestError as e:
    print(f"Error; {e}")
