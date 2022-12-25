import pyttsx3

engine = pyttsx3.init()
engine.say("Hello Muggles, My name is Apurba")
engine.runAndWait()
engine.stop()