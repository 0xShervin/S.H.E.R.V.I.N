import speech_recognition as sr
import os
from gtts import gTTS as tts

def STT():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as src:
        r.adjust_for_ambient_noise(src, duration = 1)
        audio = r.listen(src)

    return r.recognize_google(audio)

def TTS(txt):
        speech = tts(text = txt, lang = 'en', slow = False)

        speech.save("text.mp3")

        os.system("mpg321 text.mp3")

while True:

    os.system("clear")

    print("I'm listening...\n")

    text = STT()

    print("you said: " + text + " !")

    if text == "exit":
        print("BYE")
        break

    elif text == "shut down":
        inpt = input("Are you sure?(y/n)")
        if inpt == "y":
            os.system('shutdown')
            break

    TTS(text)
