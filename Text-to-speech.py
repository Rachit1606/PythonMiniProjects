import pyttsx3

data = input("Enter the text you want to listen\n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()