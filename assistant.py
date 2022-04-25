# Voice Assistant
# @Pratheeka_m_u
# (C) - 2022 Pratheeka_m_u, Karnataka, India
# email pratheekamundigesara389@gmail.com

# import ...
import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import datetime
import wikipedia
import time
import os
import wolframalpha
import pywhatkit as kit
import pyjokes
import pyautogui
import random
import sys
# install the above modules using --pip install--


# Recognize the commands using Speech_Recognition module
def GiveCommand():
    r = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=3)
        print('Listening...')
        # r.energy_threshold = 1000
        audio = r.listen(source)
        # r.pause_threshold = 0.8
        # r.phrase_threshold = 1

        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            lower_text = text.lower()
            print(text)
        except sr.UnknownValueError:
            print("Sorry didn't catch that, Try typing the command:")
            text = str(input("-->"))
            lower_text = text.lower()

    return lower_text


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

# Wolfram-Alpha ID
dict_app_id = {
    "app_id": "J5G2KU-88W2HHAVEG"
}
per_id = dict_app_id["app_id"]
client = wolframalpha.Client(per_id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Phone Directory which maps names with their phone numbers
phoneDirectory = {
    'akshar': 6364536585
}


# Hot word for waking-up/activating the assistant
def HotWord():
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        r2.adjust_for_ambient_noise(source, duration=2)
        print('...')
        audio = r2.listen(source)
        # r2.energy_threshold = 300

        try:
            text = r2.recognize_google(audio)
            lower_text = text.lower()
        except Exception as e:
            print(e)

    return lower_text


def WishMe():
    hour = int(datetime.datetime.now().hour)
    cur_time = datetime.datetime.now().strftime('%I:%M %p')
    if 4 <= hour < 12:
        gm = "Good Morning"
        print(gm)
        speak(gm)
    elif 12 <= hour <= 16:
        ga = "Good Afternoon"
        print(ga)
        speak(ga)
    elif 16 < hour <= 19:
        ge = "Good Evening"
        print(ge)
        speak(ge)
    print(cur_time)
    speak("It's " + cur_time)


# This function adds two numbers
def add(x, y):
    print("Sum : ", x + y)


# This function subtracts two numbers
def subtract(x, y):
    print("Difference : ", x - y)


# This function multiplies two numbers
def multiply(x, y):
    print("Product : ", x * y)


# This function divides two numbers
def divide(x, y):
    print("Quotient : ", x / y)


def tasksExcecutioner():
    WishMe()
    speak("I'm Alpha, What can i do for you?")
    while True:
        query = GiveCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Open apps, webpages, system apps (Opening Web Application)(yt,quora,google,cal)
        elif 'open' in query:
            if 'youtube' in query:
                speak("Opening YouTube")
                wb.open(WebSiteLinks["yt"])
            elif 'quora' in query:
                speak("Opening Quora")
                wb.open(WebSiteLinks["quora"])
            elif 'google' in query:
                speak("Opening Google")
                wb.open(WebSiteLinks["google"])
            elif 'gmail' in query:
                speak("Opening G-Mail")
                wb.open(WebSiteLinks["g_mail"])
            elif 'whatsapp' in query:
                speak("Opening whatsapp")
                wb.open(WebSiteLinks["w_app"])
            elif 'calculator' in query or 'can you do math' in query:
                print("Basic-Calculator V-0.1")
                speak("This is a basic calculator:")
                while True:
                    time.sleep(1)
                    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit Basic-Calculator")
                    speak("What operation you want?")
                    time.sleep(2)
                    ans = GiveCommand()

                    if 'addition' in ans:
                        x = int(input("x : "))
                        y = int(input("y : "))
                        add(x, y)
                    elif 'subtraction' in ans:
                        x = int(input("x : "))
                        y = int(input("y : "))
                        subtract(x, y)
                    elif 'multiplication' in ans:
                        x = int(input("x : "))
                        y = int(input("y : "))
                        multiply(x, y)
                    elif 'division' in ans:
                        x = int(input("x : "))
                        y = int(input("y : "))
                        divide(x, y)
                    elif 'exit' in ans:
                        speak("Exiting basic calculator")
                        break
                    else:
                        speak("choose again:")
            # open offline software
            elif 'chrome' in query:
                filepath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                speak("Opening Chrome")
                os.startfile(filepath)
            elif 'pycharm' in query:
                filepath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
                speak("Opening Pycharm")
                os.startfile(filepath)
            elif 'visual studio code' in query or 'vs code' in query:
                filepath = 'C:\\Users\\PRATHEEK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                speak("Opening vs code")
                os.startfile(filepath)
            elif 'spotify' in query:
                pass
            elif 'cmd' in query or 'command prompt' in query:
                speak("Command Prompt")
                os.system("start cmd")
            elif 'notepad' in query:
                filepath = '%windir%\\system32\\notepad.exe'
                speak("Opening Notepad")
                os.startfile(filepath)
            else:
                query = query.replace("open ", "")
                query = query.replace(" ", "")
                speak("Opening " + query)
                wb.open("https://www." + query + ".com")

        # search for section(yt, quora, google//others:wiki,google)
        elif 'search for' in query:
            query = query.replace("search for", "")
            if 'youtube' in query:
                query = query.replace("in youtube", "")
                speak("Searching for " + str(query) + " in youtube")
                wb.open(WebSiteLinks["yt"] + "/results?search_query=" + str(query))
            elif 'quora' in query:
                query = query.replace("in quora", "")
                speak("Searching for " + str(query) + " in quora")
                wb.open(WebSiteLinks["quora"] + "/search?q=" + str(query))
            elif 'google' in query:
                query = query.replace("in google", "")
                speak("Searching for " + str(query) + " in google")
                wb.open(WebSiteLinks["google"] + "/search?q=" + str(query))
            elif "wikipedia" in query:
                query = query.replace("in wikipedia", "")
                speak("Searching for " + str(query) + " in wikipedia")
                wb.open(WebSiteLinks["wiki"] + str(query))
            else:
                speak("Searching for " + str(query))
                wb.open(WebSiteLinks["google"] + "/search?q=" + str(query))

        elif 'the time' in query:  # Current Time
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak("The time is " + time_now)

        elif 'the date' in query:  # Current Date
            date = datetime.datetime.today().date()
            print(date)
            speak("Today is " + str(date))

        elif 'who are you' in query:
            print("I'm Alpha, Your personal assistant ")
            speak("I'm Alpha, Your personal assistant ")
            print("Version--1.0")
            speak("version 1.0")

        elif "shutdown" in query or 'sleep now' in query or 'go to sleep' in query:
            sd_hour = int(datetime.datetime.now().hour)
            if sd_hour >= 20 or sd_hour in range(0, 5):
                speak("Alright Sir!")
                print("Good Night")
                speak("Good Night")
            else:
                speak("Alright Sir!")
                speak("Have a good day")
            break

        elif "hi" in query or 'hello' in query or 'hai' in query:
            speak("Hello Sir...")

        elif 'play' in query:
            query = query.replace("play", "")
            speak("Playing " + query + " in youtube")
            kit.playonyt(query)

        elif "who is your owner" in query:
            speak("My owner is Pratheek Bhat")

        elif 'skip' in query:
            pass

        # Sending whatsapp message
        elif 'send message' in query or 'send whatsapp message' in query:
            try:
                if 'to' in query:
                    query = query.replace("send message to ", "")
                    senderName = query
                    number = phoneDirectory[senderName]
                    str_number = "+91" + str(number)
                    speak("what do you want me to send?")
                    message = GiveCommand()
                    time_hour = int(datetime.datetime.now().hour)
                    time_minute = 2 + int(datetime.datetime.now().minute)
                    kit.sendwhatmsg(str_number, message, time_hour, time_minute)
                    speak("Message has been sent")
                    time.sleep(2)
                else:
                    speak("whom do you want to send the message to")
                    senderName = GiveCommand().lower()
                    number = phoneDirectory[senderName]
                    str_number = "+91" + str(number)
                    print(str_number)
                    speak("what do you want me to send?")
                    message = GiveCommand()
                    time_hour = int(datetime.datetime.now().hour)
                    time_minute = 2 + int(datetime.datetime.now().minute)
                    kit.sendwhatmsg(str_number, message, time_hour, time_minute)
                    speak("Message has been sent")
                    time.sleep(2)
            except Exception as e:
                print(e)
                speak("Sorry i couldn't send the message")
                speak("Please try again...")

        elif 'what can you do' in query:
            speak(
                "I can do pretty much things..., I can search things for you, calculate things, play songs, open apps, "
                "send messages")
            speak("And many more...")
            speak("Try saying Open youtube, What is the time or date now or play song, send message")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke(language='en', category='neutral')
            speak(joke)

        elif 'switch window' in query or 'switch the window' in query or 'switch to recent window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'minimise window' in query or 'minimise the window' in query:
            pyautogui.keyDown('win')
            pyautogui.press('d')
            time.sleep(1)
            pyautogui.keyUp('win')

        elif 'close window' in query or 'close the window' in  query or 'close the tab' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'take screenshot' in query:
            img = pyautogui.screenshot()
            n1 = random.randrange(0, 9)
            n2 = random.randrange(0, 9)
            screenshot_name = 'screenshot' + str(n1) + str(n2) + '.png'
            img.save(screenshot_name)
            speak("screenshot saved as" + screenshot_name)

        elif "goodbye" in query or "terminate" in query:
            speak("Terminating")
            time.sleep(1)
            sys.exit()

        else:
            speak("Searching...")
            try:
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    speak("Got it")
                    print(output)
                    speak(output)
                except Exception as e:
                    res1 = wikipedia.summary(query, sentences=2)
                    speak("Got it")
                    speak("WIKIPEDIA SAYS -")
                    print(res1)
                    speak(res1)
            except Exception as e:
                print(e)
                speak("Sorry, i couldn't do that")
                print("Beta version -- 1.0.5")
                speak("I'm still at developing stage")
                speak("According to Google")
                wb.open(WebSiteLinks["google"] + "/search?q=" + str(query))

        time.sleep(1)
        speak("Next Command")


# mapping website links to their name
WebSiteLinks = {
    "yt": "https://www.youtube.com",
    "quora": "https://www.quora.com",
    "wiki": "https://en.wikipedia.org/wiki/",
    "google": "https://www.google.com",
    "g_mail": "https://www.gmail.com",
    "w_app": 'https://web.whatsapp.com/'
}

print("Established : 02/05/2021")
pyautogui.alert('Microphone will be accessed in the background')

# Main-function where the actual program starts
if __name__ == "__main__":
    while True:
        hot_word = HotWord()  # wakes-up if the user says these hot words
        if "wake up" in hot_word or "hey alpha" in hot_word or "alpha" in hot_word:
            tasksExcecutioner()
        elif "goodbye" in hot_word or "terminate" in hot_word:
            speak("Terminating")
            time.sleep(1)
            sys.exit()
        else:
            pass


# Note: This is not AI based program.
