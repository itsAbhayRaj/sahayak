import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from email.message import EmailMessage
import ssl
import random
import os
import smtplib
import wolframalpha
import pyjokes
from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound

win = Tk()
win.iconbitmap("icon.ico")
win.title("This is Sahayak")
win.geometry("1000x580")
# win.attributes('-fullscreen', True)
# win.resizable(False, False)
win.state("zoomed")

try:
    app=wolframalpha.Client("K4P5WE-36YLXEWVVH")
except:
    print("some features not working")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[-3].id)


def speak(phrase):
    engine.say(phrase)
    engine.runAndWait()


def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi am Sahayak. Please tell me how can I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    global greet
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        playsound('S:/Sahayak/s.wav')
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        greet = False

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("say tht again please...")
        greet = False
        start()
        return "None"
    return query


def specificCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        playsound('S:/Sahayak/s.wav')
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:

        speak("Oops please try again...")
        return "None"
    return query


def music():
    speak("Here you go with music")
    music_dir = "D:/New folder/Music (1)"
    songs = os.listdir(music_dir)
    print(songs)
    r = random.choice(songs)
    os.startfile(os.path.join(music_dir, r))


def weather():
    speak("okay please tell me the place")
    query = specificCommand()
    try:
            ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
            res = ap.query(f"weather of %s"%query)
            print(next(res.results).text)
            speak(next(res.results).text)
    except:
            speak("no internet")
            print("no internet")
            print(query)


def calc():
    speak("What to calculate .....")
    query = specificCommand()
    try:
        ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
        res = ap.query(f"calculate %s"%query)
        print(next(res.results).text)
        speak(next(res.results).text)
    except:
        print("not able to calculate")
        speak("not able to calculate")


def wiki():
    speak('What do you want to search on Wikipedia....')
    query = specificCommand()
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)
    print(query)


def google():
    speak("What do you want to google about....")
    query  = specificCommand()
    g_url = "https://www.google.com/search?q="
    webbrowser.open(g_url + query)


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)


def trivia():
    speak("Which Quiz you want to play.....")
    query = specificCommand().lower()

    if "science quiz " in query:
        speak("lets start ....")
        score = 0
        speak("which is the most abundant gas in earth atmosphere..")
        answer = takeCommand()
        if answer == "nitrogen ":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("which metal is the best conductor of electricity..")
        answer = takeCommand()
        if answer == "silver ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("who gave black hole theory")
        answer = takeCommand()
        if answer == "stephen hawking ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)

    elif "python quiz " in query:
        speak("lets start ....")
        score = 0
        speak("python developed in which year....")
        answer = takeCommand()
        if answer == "1991 ":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("which keyword is used in creating functions in python........")
        answer = takeCommand()
        if answer == "yes ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("what are instances of classes in python called.....")
        answer = takeCommand()
        if answer == "object ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)
    elif "math quiz " in query:
        speak("lets start ....")
        score = 0
        speak("which is the only even prime number....")
        answer = takeCommand()
        if answer == "2 ":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("longest side of right angled triangle........")
        answer = takeCommand()
        if answer == "hypotenuse ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("sides of the regular polygon are.....")
        answer = takeCommand()
        if answer == "equal ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)

    else:
        speak("Sorry this in not available yet. ")


query = Entry(win, font="Arial 24 bold")


def mail(query):
    speak("Whom should i send ....")

    def click():
        try:
            sender = 'pythonproject171@gmail.com'
            password = 'fchzlnnhwqxyaxis'
            receiver = query.get()
            speak("What will be the Subject.....")
            subject = specificCommand()
            speak("What should i send ....")
            body = specificCommand()

            em = EmailMessage()
            em['From'] = sender
            em['To'] = receiver
            em['subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(sender, password)
                smtp.sendmail(sender, receiver, em.as_string())
            speak("Sent")
        except:
            speak("oops Please try again.....")

    query.pack(side=TOP, fill=BOTH, expand=NO)
    button = Button(win, text="Enter",font="cooperblack 15 bold", command=click, fg="black", borderwidth=0, activebackground="cyan")
    button.place(x=590, y=657)


greet = 1
def start():

    if greet:
        greetme()


    query = takeCommand().lower()
    if 'wikipedia ' in query:
        speak('Searching Wikipedia...')
        # query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        print(query)

    elif "alexa" in query:
        speak(" hmm We are just friends....")
    elif "friends" in query:
        speak("I am an outsider struggling to get friends.")
    elif "what's your name" in query or "What is your name" in query:
        speak("My friends call me Sahayak")
    elif "who made you" in query or "who created you" in query:
        speak("I have been created by the team Codemons.")
    elif "how are you" in query:
        speak("Just struggling among famous assisstant ...")

    elif 'youtube' in query:
        speak("opening youtube")
        webbrowser.open("youtube.com")

    elif 'google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'spotify' in query:
        webbrowser.open("spotify.com")

    elif 'lms' in query:
        webbrowser.open("https://lms.bennett.edu.in/ilearn-support.php")

    elif 'play music' in query:
        speak("Here you go with music")
        music_dir = "D:/New folder/Music (1)"
        songs = os.listdir(music_dir)
        r = random.choice(songs)
        os.startfile(os.path.join(music_dir, r))

    elif 'time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strtime}")
        print(query)

    elif "calculate" in query:

        try:
            ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
            res = ap.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)
        except:
            print("not able to calculate")
            speak("not able to calculate")


    elif "weather" in query:
        try:
            ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
            res = ap.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)
        except:
            speak("no internet")
            print("no internet")
            print(query)

    elif "temperature" in query:
        try:
            ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
            res = ap.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)
        except:
            ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
            res = ap.query(query)
            print("no internet")
            speak("no internet")

    elif 'stop' in query:
        speak("Good bye It was nice interacting with you")
        quit()

    elif "search" in query:
        temp1 = query.replace(' ','+')
        temp2 = temp1.replace('search',' ')
        g_url = "https://www.google.com/search?q="
        webbrowser.open(g_url+temp2)
        print(query)

    elif "joke" in query:
        jokes = pyjokes.get_joke()
        speak(jokes)

    elif "what is" in query or "who is" in query:
        ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
        res = ap.query(query)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            speak("Didn't understood")
            print("No results")

    elif " science quiz " in query:
        print("not ")
        speak("lets start ....")
        score = 0
        speak("which is the most abundant gas in earth atmosphere..")
        answer = takeCommand()
        if answer == "nitrogen ":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("which metal is the best conductor of electricity..")
        answer = takeCommand()
        if answer == "silver ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("who gave black hole theory")
        answer = takeCommand()
        if answer == "stephen hawking ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)

    elif "python quiz " in query:
        speak("lets start ....")
        score = 0
        speak("python developed in which year....")
        answer = takeCommand()
        if answer == "1991 ":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("which keyword is used in creating functions in python........")
        answer = takeCommand()
        if answer == "yes ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("what are instances of classes in python called.....")
        answer = takeCommand()
        if answer == "object ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)
    elif "math quiz " in query:
        speak("lets start ....")
        score = 0
        speak("which is the only even prime number....")
        answer = takeCommand()
        if answer == "2 ":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("longest side of right angled triangle........")
        answer = takeCommand()
        if answer == "hypotenuse ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("sides of the regular polygon are.....")
        answer = takeCommand()
        if answer == "equal ":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)


pic = Image.open("mainpic.png")
pic1 = Image.open("talk.png")
pic2 = Image.open("calc.png")
pic3 = Image.open("music.png")
pic4 = Image.open("weather.png")
pic5 = Image.open("trivia.png")
pic6 = Image.open("email.png")
pic7 = Image.open("wiki.png")
pic8 = Image.open("google.png")
pic9 = Image.open("user.png")
pic10 = Image.open("exit.png")
mainpic = pic.resize((win.winfo_screenwidth(), win.winfo_screenheight()))
talkP = pic1.resize((71, 71))
calcP = pic2.resize((76, 73))
musicP = pic3.resize((71, 81))
weatherP = pic4.resize((80, 65))
triviaP = pic5.resize((82, 74))
emailP = pic6.resize((75, 54))
wikiP = pic7.resize((83, 68))
googleP = pic8.resize((97, 90))
userP = pic9.resize((57, 75))
close = pic10.resize((103, 100))

image = ImageTk.PhotoImage(mainpic)
image1 = ImageTk.PhotoImage(talkP)
image2 = ImageTk.PhotoImage(calcP)
image3 = ImageTk.PhotoImage(musicP)
image4 = ImageTk.PhotoImage(weatherP)
image5 = ImageTk.PhotoImage(triviaP)
image6 = ImageTk.PhotoImage(emailP)
image7 = ImageTk.PhotoImage(wikiP)
image8 = ImageTk.PhotoImage(googleP)
image9 = ImageTk.PhotoImage(userP)
image10 = ImageTk.PhotoImage(close)


canvas = Canvas(win, borderwidth=0, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=image, anchor=NW)

talkButton = Button(win, image=image1, cursor="hand2", activebackground="cyan", command=start, borderwidth=0,
                    highlightthickness=0)
calcButton = Button(win, image=image2, cursor="hand2", activebackground="cyan", command=calc, borderwidth=0,
                    highlightthickness=0)
musicButton = Button(win, image=image3, cursor="hand2", activebackground="cyan", command=music,  borderwidth=0,
                     highlightthickness=0)
weatherButton = Button(win, image=image4, cursor="hand2", activebackground="cyan", command=weather,  borderwidth=0,
                       highlightthickness=0)
triviaButton = Button(win, image=image5, cursor="hand2", activebackground="cyan", command=trivia, borderwidth=0,
                      highlightthickness=0)
emailButton = Button(win, image=image6, cursor="hand2", activebackground="cyan", command=lambda: mail(query),  borderwidth=0,
                     highlightthickness=0)
wikiButton = Button(win, image=image7, cursor="hand2", activebackground="cyan", command=wiki, borderwidth=0,
                    highlightthickness=0)
googleButton = Button(win, image=image8, cursor="hand2", activebackground="cyan", command=google, borderwidth=0,
                      highlightthickness=0)
userButton = Button(win, image=image9, cursor="hand2", activebackground="cyan", command=username, borderwidth=0,
                    highlightthickness=0)
exitButton = Button(win, image=image10, cursor="hand2", activebackground="gray", command=win.destroy,  borderwidth=0,
                    highlightthickness=0)

talkButton.place(x=42, y=440)
calcButton.place(x=133, y=290)
musicButton.place(x=240, y=157)
weatherButton.place(x=410, y=90)
triviaButton.place(x=586, y=65)
emailButton.place(x=770, y=98)
wikiButton.place(x=931, y=169)
googleButton.place(x=1047, y=282)
userButton.place(x=1147, y=435)
exitButton.place(x=580, y=530)


win.mainloop()

