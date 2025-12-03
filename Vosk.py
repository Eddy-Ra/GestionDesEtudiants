import pyttsx3
import  datetime

def speak(word):
    moteur = pyttsx3.init()
    voice = moteur.getProperty("voices")
    moteur.setProperty("voice","French")
    moteur.setProperty("rate",150)
    moteur.say(""+word)
    moteur.runAndWait()

def heur():
    hours = datetime.datetime.now().strftime("%H:%M:%S")
    return hours