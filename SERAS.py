from gtts import gTTS
import speech_recognition as sr
from pygame import mixer
import random


def talk(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()


def mycommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('seras is Ready...')
        r.pause_threshold = 1

        r.adjust_for_ambient_noise(source, duration=0.5)

        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print("I couldn't understand what you said, sir")
        command = mycommand();
    return command


def seras(command):
    errors = [
        "I don't know what you mean",
        "Do you even now how to speak english?",
        "Can you repeat it please?",
        "Excuse me?",
        "Pardon me?",
    ]
    if 'hello' in command:
        talk('Hello! I am seras. How can I help you?')
    else:
        error = random.choice(errors)
        talk(error)


talk('seras is ready!')

while True:
    seras(mycommand())
