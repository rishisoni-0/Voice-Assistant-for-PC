"""Nessa01 is an improved version that has two types of speak functions if one fails, """
"Best version"
#installations 
    #add virtualenv = jarvenv
    #activate virtualenv = jarvenv\Scripts\activate
    #pip install speechrecognition
    #pip install setuptools
    #pip install pyttsx3 (used for text to speech)
    #pip install pyaudio
    #pip install pocketsphinx (used for speech recognition)
    #pip install subprocess (used to open apps)
    #pip install customtkinter (used for GUI)

import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import time
import subprocess
import threading #used to run assistant loop in separate thread so that GUI doesn't freeze
import customtkinter as ctk

#speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

#GUI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("700x500")
app.title("Rishi's Assistant")
frame = ctk.CTkFrame(app, corner_radius=20)
frame.pack(padx=20, pady=20, fill="both", expand=True)

#labels
title = ctk.CTkLabel(
    frame,                     #added to put things inside frame
    text="Rishi's Assistant",
    font=("Arial", 32)
)
title.pack(pady=20)

status_label = ctk.CTkLabel(frame,
    text="Offline",
    font=("Arial", 20))

status_label.pack(pady=10)

status_label.configure(
    text="Listening...",
    text_color="green")

command_label = ctk.CTkLabel(
    frame,
    text="Waiting...",
    font=("Arial", 18),
    wraplength=500
)
command_label.pack(pady=20)


#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_os(text):
    os.system(f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')

#process commands
def processcommand(c):
    #web 
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak_os("Opened Google") 
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak_os("Opened Instagram")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak_os("Opened Youtube")
    elif "open forex factory" in c.lower():
        webbrowser.open("https://www.forexfactory.com")
        speak_os("Opened Forex Factory")
    elif "open mail" in c.lower():
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        speak_os("Opened Mail Inbox")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
        speak_os("Opening Whatsapp Web")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
        speak_os("Opening GitHub")
    

    #music library
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        link =musicLibrary.music.get(song) #get the url from music library
        if link:
            webbrowser.open(link)
            speak_os(f"Playing {song}")
        else:
            speak_os("Song not Found in Library")
    
    #app
    elif "open discord" in c.lower():
        subprocess.Popen(r"C:\Users\rupesh soni\AppData\Local\Discord\Update.exe --processStart Discord.exe")
        speak_os("Opening Discord")
    elif "open chrome" in c.lower():
        #os.system("start chrome")
        #speak_os("Opened chrome")
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([
            chrome_path,
            "--profile-directory=Profile 1" #open specific profile
        ])
        speak_os("Opened Chrome")

assistant_running = False
assistant_thread = None
#assistant loop
def assistant_loop():

    speak_os("Initializing Assistant")

    while assistant_running:

        try:

            status_label.configure(text="Waiting for Wake Word...")

            with sr.Microphone() as source:

                recognizer.adjust_for_ambient_noise(source, duration=1)

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5
                )

            word = recognizer.recognize_google(audio)

            print("Heard:", word)

            command_label.configure(text=f"Heard: {word}")

            # WAKE WORDS
            wake_words = ["bro","nasa","jarvis","hello","hello jarvis"]

            if any(w in word.lower() for w in wake_words):
                speak_os("Yupp")
                status_label.configure(text="Listening for Command...")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                command = command.lower()
                print("Command:", command)
                command_label.configure(text=f"Command: {command}")

            # STOP
            stop_words = ["stop","exit","quit","shutdown"]

            if any(w in word.lower() for w in stop_words):
                speak_os("Turning Off Assistant")
                status_label.configure(text="Assistant Stopped")
                break

            processcommand(command)

        except sr.UnknownValueError:
            print("Couldn't understand")
        except sr.RequestError as e:
            print("Google API issue:", e)
        except Exception as e:
            print("Error:", e)

##start button fn
def start_assistant():
    global assistant_running, assistant_thread

    if not assistant_running:
        assistant_running = True
        assistant_thread = threading.Thread(target=assistant_loop)
        assistant_thread.daemon = True
        assistant_thread.start()
        status_label.configure(text="Assistant Started")

#stop button fn 
def stop_assistant():
    global assistant_running
    assistant_running = False
    speak_os("Assistant stopped")
    status_label.configure(text="Assistant Stopped")

#toggle button (start/stop)
def toggle_assistant():
    global assistant_running

    if assistant_running:
        stop_assistant()
        toggle_button.configure(text="Start Assistant")
    else:
        start_assistant()
        toggle_button.configure(text="Stop Assistant")

toggle_button = ctk.CTkButton(
    frame,
    text="Start Assistant",
    command=toggle_assistant,
    width=220,
    height=45
)
toggle_button.pack(pady=30)

#run app
app.mainloop()
