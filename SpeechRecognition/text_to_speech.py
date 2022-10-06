import pyttsx3

engine = pyttsx3.init()

text = "My name is jeli"
engine.say(text)
engine.runAndWait()