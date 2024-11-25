import pyttsx3
import time
def telltime(name):
    c_time=time.localtime()
    hour=int(c_time.tm_hour)
    formatted_time=time.strftime("%H:%M", c_time)
    if hour>=5 and hour<12:
        print(f"Good Morning {name}")
    elif hour>=12 and hour<17:
        speak(f"Good Afternoon {name}")
    else:
        speak(f"Good Night {name}")
    speak(f"Time is {formatted_time}")
def speak(text):
    gola = pyttsx3.init()
    voices = gola.getProperty('voices')
    gola.setProperty('rate', 150)
    gola.setProperty('volume', 1)
    gola.setProperty('voice', voices[1].id) 
    gola.say(text)
    gola.runAndWait()
speak("Hello I am Tanisha, Your Personal Assistant")
speak("Enter your name: ")
name=input("Enter your name: ")
telltime(name)