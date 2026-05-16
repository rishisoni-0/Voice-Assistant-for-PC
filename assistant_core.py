#pip install setuptools
#pip install pyaudio

import speech_recognition as sr #pip install speechrecognition
import time
import commands
import gui
import speech


#assistant loop
assistant_running = False
assistant_thread = None
def assistant_loop():
    speech.speak_os("Initializing Assistant")

    while assistant_running:

        try:
            gui.status_label.configure(text="Waiting for Wake Word...")
            with sr.Microphone() as source:

                speech.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = speech.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5)

            word = speech.recognizer.recognize_google(audio)
            print("Heard:", word)
            gui.command_label.configure(text=f"Heard: {word}")

            # WAKE WORDSgui.
            wake_words = ["bro","nasa","jarvis","hello","hello jarvis"]

            if any(w in word.lower() for w in wake_words):
                speech.speak_os("Yupp")
                gui.status_label.configure(text="Listening for Command...")
                with sr.Microphone() as source:
                    audio = speech.recognizer.listen(source)

                command = speech.recognizer.recognize_google(audio)
                command = command.lower()
                print("Command:", command)
                gui.command_label.configure(text=f"Command: {command}")

            # STOP WORDS
            stop_words = ["stop","exit","quit","shutdown"]

            if any(w in word.lower() for w in stop_words):
                speech.speak_os("Turning Off Assistant")
                gui.status_label.configure(text="Assistant Stopped")
                break

            commands.processcommand(command)

        except sr.UnknownValueError:
            print("Couldn't understand")
        except sr.RequestError as e:
            print("Google API issue:", e)
        except Exception as e:
            print("Error:", e)
