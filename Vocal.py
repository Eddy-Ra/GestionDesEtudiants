import speech_recognition as sr
import pyttsx3
from datetime import datetime


r = sr.Recognizer()

moteur = pyttsx3.init()
voice = moteur.getProperty("voices")
moteur.setProperty("voice","english")
moteur.setProperty("rate",125)
def Recorder():
   while(1):
        try:
            with sr.Microphone() as voiceSource:
                r.adjust_for_ambient_noise(voiceSource,duration=0.5)
                text = r.listen(voiceSource) # ecouter les messages
                Mytext = r.recognize_google(text, language='en-EN')
                #moteur.say(Mytext)
                #moteur.runAndWait()
                print(Mytext)
                print("text wrote")
                return Mytext
        except sr.RequestError as e:
            print("il y a probleme lors du processuce;{0}".format(e))
        except sr.UnknownValueError:
            print("Unknown value")

def WriteMytext():
    f = open("too/output.txt","a")
    mess = Recorder()
    f.write(mess)
    f.write("\n")
    f.close()

while(True):
    #WriteMytext()
    mess = Recorder()
    now = datetime.now()
    time = now.strftime("%H : %M: %S")
    print(time)
    if "hello" in mess:
        moteur.say("hello dear user")
        moteur.runAndWait()
    elif "how are you" in mess:
        moteur.say(" i' m fine And you")
        moteur.runAndWait()
    elif "time" in mess:
        moteur.say("it is"+time)
        moteur.runAndWait()

