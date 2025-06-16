import win32com.client
import time
import os
import speech_recognition as sr
import webbrowser

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello Rudra, This is Jarvis!! Welcome to my World!!")
current_time = time.strftime("%H:%M:%S")
speaker.Speak(f"The current time is {current_time}")
hour = int(time.strftime("%H"))

if 0 <= hour < 12:
  speaker.Speak("Good Morning!!")
elif 12 <= hour < 16:
  speaker.Speak("Good Afternoon!!")
elif 16 <= hour < 20:
  speaker.Speak("Good Evening!!")
else:
  speaker.Speak("Good Night!!")

speaker.Speak("How Can I help Rudra???")

def take_command():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            speaker.Speak("Contacting the internal server...")
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speaker.Speak("Sorry, I didn't catch that. Please try again.")
            return None
    except sr.RequestError:
        speaker.Speak("Microphone not detected or unavailable.")
        return None

def jarvis():
    while True:
        command = take_command()
        if command:
            if "jarvis" in command or "open central server" in command or "jarvis wake up" in command:
                speaker.Speak("Hello Rudra, Welcome to my world!! How Can I help you today?")
            
            elif "open youtube" in command or "initialize youtube" in command or "youtube" in command:
                speaker.Speak("Opening YouTube...")
                webbrowser.open("https://www.youtube.com")
            
            elif "tell me the date" in command or "what is the date" in command:
                date_today = time.strftime("%d-%m-%Y")
                speaker.Speak(f"The current date is {date_today}")
            
            elif "what is the time now" in command or "what is the time" in command:
                current_time = time.strftime("%H:%M:%S")
                speaker.Speak(f"The time now is {current_time}")
            
            elif "open google" in command or "initialize google" in command or "google" in command:
                speaker.Speak("Opening Google...")
                webbrowser.open("https://www.youtube.com")
            
            elif "open visual studio" in command or "initialize visual studio code" in command:
                print("Opening Visual Studio Code...")
                os.system(r"start C:\Users\Rudra\Documents\Visual Studio Code\Code.exe")
            
            elif "open google chrome" in command or "initialize google chrome" in command:
                print("Opening Google Chrome...")
                os.system(r"start C:\Program Files\Google\Chrome\Application\chrome.exe")
            
            elif "open microsoft word" in command or "initialize microsoft word" in command:
                print("Opening Microsoft Word...")
                os.system(r"start C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
            
            elif "shut down the pc" in command or "turn off" in command:
                print("Shutting down...")
                speaker.Speak("Shutting down the computer. Goodbye!")
                os.system("shutdown /s /t 1")
            
            elif "exit" in command or "quit" in command:
                print("Exiting JARVIS...")
                speaker.Speak("Piling and executing the central servers.Goodbye Rudra! Have a great day!")
                break
            
            else:
                print("Unrecognized command.")
                speaker.Speak("Sorry, I didn't understand that. Please try again.")
        else:
            print("No command detected.")

jarvis()
