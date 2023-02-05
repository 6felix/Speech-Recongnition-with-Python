#!/usr/bin/env python3

# speech_recognition module
import speech_recognition as sr

# this is the sr recongnizer class instance
rec = sr.Recognizer()

# sets up the recongnizers source
havard = sr.AudioFile('harvard.wav')
with havard as source:
    rec.adjust_for_ambient_noise(source)
    audio = rec.record(source)

# repsonse
print(rec.recognize_google(audio, show_all=True)['alternative'][0]['transcript'])
