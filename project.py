import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
import pywhatkit
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from desktopassistant1 import Ui_Form

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("helio 1 point o")
    speak("I am your Assistant")
    speak(assname)
    speak("I have been cretaed as a minor project by Shreyash, Devansh and Amit")
    speak("Under the guidance of our faculty members")
def username(self):
    speak("What should i call you sir")
    uname =self. takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")
    



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

   
    server.login('it1938@global.org.in', 's')
    server.sendmail('it1938@global.org.in', to, content)
    server.close()






class MainThread(QThread):
    def _init_(self):
        super(MainThread, self)._init_()

    def run(self):
            self.TaskExecution()
    
   
            

    def takeCommand(self):

        r = sr.Recognizer()

        with sr.Microphone(device_index=0) as source:

            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 4000

            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"

        return query

    def TaskExecution(self):
        wishMe()
        username(self)
      

        while True:

            self.query = self.takeCommand().lower()

           
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                speak("sir what do you want to play")
                se =self.takeCommand().lower()
                video = se.replace('play', '')
                pywhatkit.playonyt(video)

            elif 'open google' in self.query:
                speak("What do you want to search sir")
                cm = self.takeCommand().lower()
                speak("Here is your search sir\n")
                webbrowser.open(f"{cm}")

            elif 'open stackoverflow' in self.query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")

            elif 'play music' in self.query or "play song" in self.query:
                speak("Here you go with music")
                music_dir = "C:\\Users\\Devansh\\Downloads\\songs"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            
            elif 'email to yash' in self.query:
                try:
                    speak("What should I say?")
                    content =self. takeCommand()
                    to = "yashtamrakar82@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'send a mail' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    speak("whome should i send")
                    to = input()
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("Sorry my bhai shreyash I am not able to send this email")

            elif 'how are you' in self.query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in self.query or "good" in self.query:
                speak("It's good to know that your fine")

            elif "change my name to" in self.query:
                self.query = self.query.replace("change my name to", "")
                assname = self.query

            elif "change name" in self.query:
                speak("What would you like to call me, Sir ")
                assname = self.takeCommand()
                speak("Thanks for naming me")

            elif "what's your name" in self.query or "What is your name" in self.query:
                speak("My friends call me")
                speak(assname)
                print("My friends call me", assname)

            elif 'exit' in self.query:
                speak("Thanks for giving me your time")
                exit()

            elif "who made you" in self.query or "who created you" in self.query:
                speak("I have been created by Shreyash.")

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())


            elif 'search' in self.query or 'play' in self.query:

                self.query = self.query.replace("search", "")
                self.query = self.query.replace("play", "")
                webbrowser.open(self.query)

            elif "who i am" in self.query:
                speak("If you talk then definitely your human.")

            elif "why you came to world" in self.query:
                speak("Thanks to Shreyash. further It's a secret")

            
            elif 'is love' in self.query:
                speak("It is 7th sense that destroy all other senses")

            elif "who are you" in self.query:
                speak("I am your virtual assistant created by Shreyash amit and devansh")

            elif 'reason for you' in self.query:
                speak("I was created as a Minor project by Mister Shreyash amit and devansh")


            elif 'news' in self.query:
                webbrowser.open("https://timesofindia.indiatimes.com/defaultinterstitial.cms")

            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'shutdown system' in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")

            elif "don't listen" in self.query or "stop listening" in self.query:
                speak(
                    "for how much time you want to stop jarvis from listening commands")
                a = int(self.takeCommand())
                time.sleep(a)
                print(a)

            elif "where is" in self.query:
                self.query = self.query.replace("where is", "")
                location = self.query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open(
                    "https://www.google.nl / maps / place/" + location + "")

        
            elif "restart" in self.query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in self.query or "sleep" in self.query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

            elif "log off" in self.query or "sign out" in self.query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "write a note" in self.query:
                speak("What should i write, sir")
                note =self. takeCommand()
                file = open('jarvis.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm =self.takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("helio.txt", "r")
                print(file.read())
                speak(file.read(6))

            elif "helio" in self.query:

                wishMe()
                speak("Helio 1 point o in your service Mister")
                speak(assname)

            elif "weather" in self.query:

                search="temperature in jabalpur"
                url=f"https://www.google.com/search?={search}"
                r=requests.get(url)
                data=BeautifulSoup(r.text,"html.parser")
                temp=data.find("div",class_="BNeawe").text
                speak(f"current{search} is {temp}")
                print(f"current temperature in {search} is {temp}")
                
          #  elif "wikipedia" in self.query:
               # webbrowser.open("wikipedia.com")

            elif "Good Morning" in self.query:
                speak("A warm" + self.query)
                speak("How are you Mister")
                speak(assname)

            elif "will you be my gf" in self.query or "will you be my bf" in self.query:
                speak("I'm not sure about, may be you should give me some time")

            elif "how are you" in self.query:
                speak("I'm fine, glad you me that")

            elif "i love you" in self.query:
                speak("It's hard to understand")


            elif "open notepad" in self.query:
                npath="C:\Windows\System32\\notepad.exe"
                os.startfile(npath)

            elif "open command prompt" in self.query:
                os.system("start cmd")    
            
            elif "close notepad" in self.query:
                speak("Closing notepad")
                
startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
         super().__init__()
         self.ui = Ui_Form()
         self.ui.setupUi(self)
         self.ui.run.clicked.connect(self.startTask)
         self.ui.exit.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie=QtGui.QMovie("images/main1.gif") 
        self.ui.main.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("images/init1.gif")   
        self.ui.init.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("images/heart.gif")   
        self.ui.heart.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

         
        

  

app=QApplication(sys.argv)
project=Main()
project.show()
exit(app.exec_())