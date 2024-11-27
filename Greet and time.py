import pyttsx3
import time
import speech_recognition as sr
def telldate(name):
    current_date = time.strftime("%Y-%m-%d")
    speak(f"Date is {current_date}")
def telltime(name):
    c_time=time.localtime()
    hour=int(time.strftime("%H"))
    formatted_time=time.strftime("%H:%M", c_time)
    if hour>=5 and hour<12:
        print(f"Good Morning {name}")
    elif hour>=12 and hour<20:
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
speak("Hello I am Tanie, Your Personal Assistant")
speak("What is Your name: ")
recognizer = sr.Recognizer()
source=sr.Microphone()
print("Listening...")
source.__enter__()
audio = recognizer.listen(source)
source.__exit__(None, None, None)
name = recognizer.recognize_google(audio)
while True:
    speak(f"What do you want to know {name},")
    print("Listening...")
    source.__enter__()
    audio1 = recognizer.listen(source)
    source.__exit__(None, None, None)
    choice=recognizer.recognize_google(audio1)
    match(choice):
        case 'time please':
            telltime(name)
        case 'date please':
            telldate(name)
        case 'shutdown':
            speak("It was nice to help you")
            break
        case _:
            speak("Sorry, I can't understand,Can You repeat what you said")