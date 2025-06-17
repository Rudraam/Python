import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

emails = {
    "Rudra": "rudramanidhiman@gmail.com",
    "Devanshu": "devanshudhiman003@gmail.com",
}
#intializing the voice of windows
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voice)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour < 12:
        speak("Good Morning, Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, Sir")
    else:
        speak("Good Evening, Sir")

    speak("I am Jarvis Sir. Please tell me how can I help you today? ")

def take_command():
    '''
    This function will help the AI to take commands through Microphone and perform an action according to it.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #pause_threshold=seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        speak("Sorry, I didn't get that. Please try again.")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("rudramanidhiman@gmail.com","<--your password-->")
    server.sendmail("rudramanidhiman@gmail.com",to,content)
    server.close()


if __name__== "__main__":
    wishMe()
    while True:
     query = take_command().lower()
     #logic for executing tasks based on query
     if "search" in query:
         speak("Searching Wikipedia...")
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences=2)
         speak("According to Wikipedia")
         print(results)
         speak(results)

     elif 'open youtube' in query or 'youtube' in query:
         webbrowser.open("youtube.com")
     elif 'open google' in query or 'google' in query:
         webbrowser.open("google.com")
     elif 'open stackoverflow' in query or 'stackoverflow' in query:
         webbrowser.open("stackoverflow.com")
     elif 'play music' in query or 'play song' in query:
         music_dir = "D:\\Non-Critical\\songs\\Favourite_Songs2"
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[0]))
     elif 'the time' in query or 'time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is {strTime}")
     elif 'open code' in query or 'vs' in query:
         Codepath = "C:\\Users\\Rudramani Dhiman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(Codepath)
     elif 'email to rudra' in query or 'send email' in query:
         try:
             speak("What should I say?")
             content = take_command()
             to = "rudramanidhiman@gmail.com"
             sendEmail(to,content)
             speak("Email has been sent!")
         except Exception as e:
             print(e)
             speak("Sorry Sir. I am not able to send an Email.")

     elif 'exit' in query or 'close' in query or "that's it" in query:
         speak("Executing the Central servers.Goodbye Sir. Have a Great Day!!")
         break
         
         
         