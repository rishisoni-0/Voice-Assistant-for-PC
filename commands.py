import webbrowser 
import musicLibrary #musicLibrary.py
import time
import subprocess #pip install subprocess (used to open apps)
import speech

#process commands
def processcommand(c):
    #web 
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speech.speak_os("Opened Google") 
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speech.speak_os("Opened Instagram")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speech.speak_os("Opened Youtube")
    elif "open forex factory" in c.lower():
        webbrowser.open("https://www.forexfactory.com")
        speech.speak_os("Opened Forex Factory")
    elif "open mail" in c.lower():
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        speech.speak_os("Opened Mail Inbox")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
        speech.speak_os("Opening Whatsapp Web")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
        speech.speak_os("Opening GitHub")
    
    #music library
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        link =musicLibrary.music.get(song) #get the url from music library
        if link:
            webbrowser.open(link)
            speech.speak_os(f"Playing {song}")
        else:
            speech.speak_os("Song not Found in Library")
    
    #app
    elif "open discord" in c.lower():
        subprocess.Popen(r"C:\Users\rupesh soni\AppData\Local\Discord\Update.exe --processStart Discord.exe")  #path of your application 
        speech.speak_os("Opening Discord")
    elif "open chrome" in c.lower():
        #os.system("start chrome")
        #speak_os("Opened chrome")
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  #path of your application 
        subprocess.Popen([chrome_path,"--profile-directory=Profile 1"])  #open specific profile
        speech.speak_os("Opened Chrome")
