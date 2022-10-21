import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import smtplib
import webbrowser
import pipwin
import pyaudio
from bs4 import BeautifulSoup as BS
import requests



listener = sr.Recognizer() #this is used to recognize our speech
engine = pyttsx3.init() # text to speech
MASTER = "Samkit"
# this is used to change male voice to female voice

voices = engine.getProperty('voices')  # here we get all the available voice choices
engine.setProperty('voice', voices[1].id) # here we set the choosen voice and here index[1] means 2nd choice

# here we are defining a function called talk means alexa will return text as a talk
def talk(text):
    engine.say(text)
    engine.runAndWait()
def takeCommand_Hindi ():
    try:
        listener = sr.Recognizer()
        with sr.Microphone as source:
            print("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(audio, language='hi-In')
            command = command.lower()
            if 'Jarvis' in command:
                command = command.replace('alexa', '')  # here we are replacing alexa with an blank space

            print(command)
    except:
        pass
    return command


# this function will greet you as per the given time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        talk("Good Morning" + MASTER)
    elif hour>=12 and hour<16:
        talk("Good Afternoon" + MASTER)
    else:
        talk("Good Evening" + MASTER)
    talk("Hi I am Jarvis How may i help you")


wishMe()
# here we are defining a function called take_command as we will be giving so many commands to alexa
def take_command():
    try:
        with sr.Microphone() as source: # here we will be getting indication when to speak
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Jarvis' in command:
                command = command.replace('alexa', '')# here we are replacing alexa with an blank space

                print(command)
    except:
        pass
    return command
def takeCommandHindi():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio,language='hi-In')
            command = command.lower()
            if 'Alexa' in command:
                command = command.replace('alexa', '')  # here we are replacing alexa with an blank space

                print(command)
        except:
            pass
        return command

# here we are defining a function called run_alexa to run alexa
def run_alexa():
    command = take_command()
    # command = takeCommandHindi() # here command will go to take_command and afterwards it will print command
    print(command)
    if 'play' in command:
        song = command.replace('play' , '')
        talk('playing' + song)
        pywhatkit.playonyt(song) # here we have used pywhatkit module for playing a song on youtube

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') # here we have used datetime module for current time
        print(time)
        talk('current time is ' + time)
    elif 'open music'in command:
        songs_dir = "D:\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[2]))
    elif 'search' in command:
        person = command.replace('search' , '')
        info = wikipedia.summary(person, 1) # here we have used wikipedia module to search about any person on internet
        print(info)
        talk(info)
      # here i am giving some funny command to alexa
    elif 'date' in command:
        talk('sorry, i have a headache')
    elif 'are you single' in command:
        talk('I am in relationship with Samkit')

    #elif 'gold' in command:
        def get_price(url): # method to get the price of gold
            data = requests.get(url) # getting the request from url
            soup = BS(data.text, 'html.parser') # converting the text
            ans = soup.find("div", class_= "BNeawe s3v9rd AP7Wnd").text # finding metha info for the current price
            return ans
        url = "http://www.google.com / search?q = gold + price" # URL of the gold price
        ans = get_price(url) # calling the function
        talk(ans)
        print(ans)

    elif 'ms dhoni' in command:
        talk('MS dhoni is an emotion')
    elif 'snehal' in command:
        talk('snehal shah is a multitalented girl an singer a dancer and a very emotional girl and samkit is so much proud of her performance.')
    elif 'jinal' in command:
        talk('jinal shah is very impressive girl she is an talented artist as well as an superb dancer and she is topper of class')
    elif 'joke' in command:
        talk(pyjokes.get_joke()) # here we are using pyjokes module to get jokes
    elif 'sam kit' in command:
        talk('Samkit Shah is very cute guy and he is gaining expertise in python and he is also an part time tuition teacher and content writer.')
    elif 'masi' in command:
        talk('Bhagyashree shah is samkit shah masi she is so much caring and her husband name is manoj shah he is so much hardworking man')
    else:
        talk('choti bachchi ho kya')

# for running in loop we will be using while loop

while True:
    run_alexa()