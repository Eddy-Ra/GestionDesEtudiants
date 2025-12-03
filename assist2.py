import pyttsx3
import speech_recognition as sr
import datetime

listener = sr.Recognizer()
moteur = pyttsx3.init()
voices = moteur.getProperty('voices')
moteur.setProperty('voice', "fr")  # Utilisez voices[0].id pour la voix masculine, voices[1].id pour la voix féminine
moteur.setProperty('rate', 170)


def parler(texte):
    moteur.say(texte)
    moteur.runAndWait()


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
        recon.adjust_for_ambient_noise(source)
        print("Parler...")
        aud = recon.listen(source, timeout=5)
        try:
            nom = recon.recognize_google(aud, language="fr-FR")
            parler(f"vous appelez {nom}")
            print(f"vous avez dit : {nom}")

            parler("Êtes vous un étudiant ou un administrateur?")
            aud_choix = recon.listen(source, timeout=5)
            choix = recon.recognize_google(aud_choix, language="fr-FR")
            parler(f"ah bon,vous êtes un {choix}")
            print(f"ah bon,vous êtes un {choix}")

        except sr.UnknownValueError:
            parler("pardon veuillez repeter")
        except Exception as e:
            parler(f"erreur{e}")



