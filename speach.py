import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)  # Record the audio

# Convert speech to text
try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio)  # Use Google's speech recognition
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
