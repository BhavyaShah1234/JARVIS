import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <6:
        print('JARVIS:Good Night sir. I am JARVIS, your personal assistant. How may I help you?')
        speak('Good Night sir. I am JARVIS, your personal assistant. How may I help you?')
    elif 6 <= hour < 12:
        print('JARVIS:Good Morning sir. I am JARVIS, your personal assistant. How may I help you?')
        speak('Good Morning sir. I am JARVIS, your personal assistant. How may I help you?')
    elif 12 <= hour < 18:
        print('JARVIS:Good Afternoon sir. I am JARVIS, your personal assistant. How may I help you?')
        speak('Good Afternoon sir. I am JARVIS, your personal assistant. How may I help you?')
    elif hour >= 18:
        print('JARVIS:Good Evening sir. I am JARVIS, your personal assistant. How may I help you?')
        speak('Good Evening sir. I am JARVIS, your personal assistant. How may I help you?')


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        audio = r.listen(source)
    try:
        print('Recognizing....')
        speech = r.recognize_google(audio, language='en')
        print(f'USER:{speech}')
    except Exception as e:
        print(e)
        print(f"JARVIS:I can't get you sir.")
        speak("I can't get you sir.")
        return "None"
    return speech


def send_email(un, pw, add, sub, body, end):
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(un, pw)
    connection.sendmail(un,
                        add,
                        f'Subject:{sub}\n{body}\n{end}')


if __name__ == "__main__":
    wish_me()
    while True:
        query = listen().lower()
        if "wikipedia" in query:
            print('Searching Wikipedia....')
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print('JARVIS:According to Wikipedia, ' + str(results))
            speak('According to Wikipedia, ' + str(results))
        elif 'open youtube' in query:
            print('Opening Youtube....')
            speak('Opening Youtube....')
            webbrowser.open('https://www.youtube.com')
        elif 'ok google' in query:
            print('Opening Google....')
            speak('Opening Google....')
            webbrowser.open('https://www.google.com')
        elif 'play music' in query:
            music_dir = r'F:\Music\Music'
            songs = os.listdir(music_dir)
            print(f'Playing {songs[0]}')
            speak(f'Playing {songs[0]}')
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f'JARVIS:{time}')
            speak(time)
        elif "today's date" in query:
            date = datetime.datetime.today().strftime("%d-%m-%Y")
            print(f'JARVIS:{date}')
            speak(date)
        elif 'bye jarvis' in query:
            print("Good bye sir. It's been a pleasure serving you.")
            speak("Good bye sir. It's been a pleasure serving you.")
            exit(0)
        elif 'open pycharm' in query:
            code_path = r"E:\PyCharm Community Edition 2020.2\bin\pycharm64.exe"
            print('Opening PyCharm....')
            speak('Opening PyCharm....')
            os.startfile(code_path)
        elif 'mail Bhavya' in query:
            try:
                print('What should the subject say?')
                speak('What should the subject say?')
                subject = listen()
                print('What should the body contain?')
                speak('What should the body contain?')
                content = listen()
                print('How should I end it?')
                speak('How should I end it?')
                end = listen()
                to = 'bhavyaminesh.shah2019@vitstudent.ac.in'
                send_email('username@gmail.com', 'password', to, subject, content, end)
                print('Email sent successfully.')
                speak('Email sent successfully.')
            except Exception as e:
                print(e)
                print('I am sorry. I could not deliver this email.')