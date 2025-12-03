import pyttsx3
import speech_recognition as sr
import datetime
from les_func import parler

listener = sr.Recognizer()
moteur = pyttsx3.init()



def greet():
    heure = datetime.datetime.now().hour
    if 0 <= heure < 12:
        parler("Bonjour,je m'appelle Tessa")

    elif 12 <= heure < 18:
        parler("Bonne après midi,je m'appelle Tessa")

    else:
        parler("Bonsoir, Je m'appelle Tessa")




def ecouter():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parler....")
        recon.adjust_for_ambient_noise(source)
        aud = recon.listen(source, timeout=5)
        try:
            texte = recon.recognize_google(aud, language="fr-FR")
            parler(texte)
            print(f"vous avez dit : {texte}")
            if texte == "Eddy":
                parler("je t'aime eddy")
                print("je t'aime Eddyy")
        except sr.UnknownValueError:
            parler("excuse me ,i don't know")
            print("no")


ecouter()
