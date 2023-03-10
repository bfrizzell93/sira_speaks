import speech_recognition as sr
import webbrowser
import gtts
import time
import playsound
import os  #contains a method for removing all the sound files that accumulate
import random
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            sira_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            sira_speak('Sorry, I did not get that')
        except sr.RequestError:
            sira_speak('Sorry, my speech service is unavailable')
        return voice_data

def sira_speak(audio_string):
    tts = gtts(text = audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        sira_speak('My name is Sira')
    if 'what time is it' in voice_data:
        sira_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        sira_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        sira_speak('Here is the location for ' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
sira_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)