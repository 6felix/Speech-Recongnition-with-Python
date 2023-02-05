#!/usr/bin/env python3
"""

Function:
    Prints all possible
    transcibes of an audio

AudioFileType:
    WAV

Imports:
    Package: speech_recognition
    Recognizer: recognize_google

"""

# Imports
import speech_recognition as sr

# this is the sr recongnizer class instance
rec = sr.Recognizer()

# sets up the recongnizers source
havard = sr.AudioFile('harvard.wav')
with havard as source:
    rec.adjust_for_ambient_noise(source)
    audio = rec.record(source)

# repsonse
num = 0
while True:
    try:
        print("{}) ".format(num + 1) , rec.recognize_google(audio, show_all=True)['alternative']
              [num]['transcript'])
        num += 1

    except IndexError:
        print("END")
        break
