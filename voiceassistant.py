###voice assistant in python part1 ###

import pyttsx3
import serial
import googlesearch
import speech_recognition as sr
import pyaudio

r = sr.Recognizer()        
query = sr.Microphone()

with query as s:
    audio = r.record(s, duration = 4)
r.recognize_google(audio)                           

for i in googlesearch.search(audio, tld="co.in", lang='en', num=10, start=0, stop=None, pause=2):  
    print(i)
          
