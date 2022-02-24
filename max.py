import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import pywhatkit
import requests
import json
import wolframalpha


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    day = str(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)

    if month == 1:
        month = 'january'
    elif month == 2:
        month ='february'
    elif month == 3:
        month = 'march'
    elif month == 4:
        month = 'april'
    elif month == 5:
        month = 'may'
    elif month == 6:
        month = 'june'
    elif month == 7:
        month = 'july'
    elif month == 8:
        month = 'august'
    elif month == 9:
        month = 'september'
    elif month == 10:
        month = 'october'
    elif month == 11:
        month = 'november'
    else:
        month = 'december'

    if hour >= 0 and hour <6 :
        speak('Good night sir!')

    elif hour >= 6 and hour < 12 :
        speak('good morning sir!')

    elif hour >= 12 and hour < 18 :
        speak('good afternoon sir!')

    elif hour >= 18 and hour < 21 :
        speak('good evening sir!')
    else:
        speak('Good night sir!')

    speak(f'today is {month} {day} ')
    speak('hello sir i am maxx. tell me how may i help you.')

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == '__main__':
    wishMe()

    path_chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    path_vlc = 'C:/Program Files (x86)/VideoLAN/VLC/vlc.exe'
    path_vscode = 'C:/Users/dasdi/AppData/Local/Programs/Microsoft VS Code/Code.exe'
    path_spotify = 'C:/Users/dasdi/AppData/Roaming/Spotify/Spotify.exe'
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
          speak('Searching Wikipedia...')
          query = query.replace('wikipedia' , '')
          results = wikipedia.summary(query,sentences=2)
          print(results)
          speak(f'according to wikipedia {results}')

        elif 'open youtube' in query:
            webbrowser.get(path_chrome).open('https://youtube.com')

        elif 'open google' in query:
            webbrowser.get(path_chrome).open('https://google.com')

        elif 'open gmail' in query:
            webbrowser.get(path_chrome).open('https://mail.google.com/mail/u/0/#inbox')

        elif 'open facebook' in query:
            webbrowser.get(path_chrome).open('https://en-gb.facebook.com/campaign/landing.php?&campaign_id=973072070&extra_1=s%7Cc%7C231346440452%7Ce%7Cfb%7C&placement&creative=231346440452&keyword=fb&partner_id=googlesem&extra_2=campaignid%3D973072070%26adgroupid%3D54006247131%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-297263798525%26loc_physical_ms%3D1007799%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=Cj0KCQjwktKFBhCkARIsAJeDT0gmrapzDhaV3gmJzIw8y99xwuRmfoTrevGDYVQQTMjNqdJNG74ZUEwaAnCVEALw_wcB')

        elif 'open vlc' in query:
            os.startfile(path_vlc)

        elif 'open vs code' in query:
            os.startfile(path_vscode)

        elif 'open spotify' in query:
            os.startfile(path_spotify)

        elif 'play' in query:
            song = query.replace('play' , '')
            speak(song)
            pywhatkit.playonyt(song)

        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            print(time)
            speak(f'Sir the time is {time}')

        elif 'who are you' in query:
            speak('i am maxx your voice assistant. Mister Dibya jyoti Das made me using python programs. i am programed to do all the work for you in your command. My boss says sky is my limit... ')

        elif 'news' in query:
            source = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=496aa0b110c8487fbb7f49c04d98f67f")
            data = json.loads(source.content)
            for i in range(10):
                news = data["articles"][i]["title"]
                print("News",i+1,news)
                speak(news)

        elif 'temperature' in query:
            app = wolframalpha.Client("6737GH-VUK464KGWU")
            res = app.query(query)
            speak(next(res.results).text)

        elif 'calculate' in query:
            app = wolframalpha.Client("6737GH-VUK464KGWU")
            speak("What should i calculate?")
            gh = takeCommand().lower()
            res = app.query(gh)
            speak(next(res.results).text)

