import pyttsx3
import os
import speech_recognition as sr
#speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_os(text):
    os.system(f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')
