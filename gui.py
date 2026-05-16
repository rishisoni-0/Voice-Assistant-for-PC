import customtkinter as ctk #pip install customtkinter (used for GUI)
import threading
import speech
from assistant_core import assistant_loop, assistant_running

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
    frame,   #added to put things inside frame
    text="Rishi's Assistant",
    font=("Arial", 32))
title.pack(pady=20)

status_label = ctk.CTkLabel(frame,
    text="Offline",
    font=("Arial", 20))
status_label.pack(pady=10)  #pady: distance in y-axis

status_label.configure(
    text="Listening...",
    text_color="green")

command_label = ctk.CTkLabel(
    frame,
    text="Waiting...",
    font=("Arial", 18),
    wraplength=500)
command_label.pack(pady=20)

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
    speech.speak_os("Assistant stopped")
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
    height=45)
toggle_button.pack(pady=30)
