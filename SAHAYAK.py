import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from email.message import EmailMessage
import ssl
from gtts import gTTS
from googletrans import Translator
import random
import os
import smtplib
import wolframalpha
import pyjokes
from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound as PS
win = Tk()
win.iconbitmap("icon.ico")
win.title("This is Sahayak")
win.geometry("1000x580")
# win.attributes('-fullscreen', True)
# win.resizable(False, False)
# win.state("zoomed")

try:
    app=wolframalpha.Client("K4P5WE-36YLXEWVVH")
except:
    print("some features not working")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

lang = {"albanian" : "sq", "arabic" : "ar",  "bengali" : "bn", "bosnian" : "bs", "bulgarian" : "bg",
        "catalan" : "ca", "chinese" : "zh-cn", "croatian" : "hr", "danish" : "da", "dutch" : "nl",
        "english" : "en", "estonian" : "et", "filipino" : "tl", "french" : "fr", "german" : "de",
        "greek" : "el", "gujarati": "gu", "hindi" : "hi", "hungarian" : "hu", "icelandic" : "is",
        "indonesian" : "id", "italian" : "it", "japanese" : "ja", "javanese" : "jw", "kannada" : "kn",
        "korean" : "ko", "latin" : "la", "latvian" : "lv", "malay" : "ms", "malayalam" : "ml",
        "marathi" : "mr", "myanmar" : "my", "nepali" : "ne", "norwegian" : "no", "polish" : "pl",
        "portuguese" : "pt", "romanian" : "ro", "russian" : "ru", "serbian" : "sr", "sinhala" : "si",
        "slovak" : "sk", "somali" : "so", "spanish" : "es", "swahili" : "sw", "swedish" : "sv",
        "tamil" : "ta", "telugu" : "te", "thai" : "th", "turkish" : "tr", "ukrainian" : "uk",
        "urdu" : "ur", "vietnamese" : "vi"}


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

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        PS('S:/Sahayak/s.wav')
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        speak("say that again please...")
        takeCommand()
        return "None"
    return query


def music():
    speak("Here you go with music")
    music_dir = "Music(1)"
    songs = os.listdir(music_dir)
    print(songs)
    r = random.choice(songs)
    os.startfile(os.path.join(music_dir, r))


def weather():
    speak("okay please tell me the place")

    ask = takeCommand()

    try:
            ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
            res = ap.query(f"weather of %s"%ask)
            print(next(res.results).text)
            speak(next(res.results).text)
    except:
            speak("no internet")
            print("no internet")
            print(ask)


def calc():
    speak("What to calculate .....")
    ask = takeCommand()
    try:
        ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
        res = ap.query(f"calculate %s"%ask)
        print(next(res.results).text)
        speak(next(res.results).text)

    except:
        print("not able to calculate")
        speak("not able to calculate")


def wiki():
    speak('What do you want to search on Wikipedia....')
    ask = takeCommand()
    results = wikipedia.summary(ask, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)
    print(ask)


def google():
    speak("What do you want to google about....")
    query  = takeCommand()
    g_url = "https://www.google.com/search?q="
    webbrowser.open(g_url + query)


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)


def trivia():
    speak("Which Quiz you want to play.....")
    query = takeCommand().lower()

    if "science quiz" in query:
        speak("lets start ....")
        score = 0
        speak("which is the most abundant gas in earth atmosphere..")
        answer = takeCommand()
        if answer == "nitrogen":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("which metal is the best conductor of electricity..")
        answer = takeCommand()
        if answer == "silver":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("who gave black hole theory")
        answer = takeCommand()
        if answer == "stephen hawking":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)

    elif "python quiz" in query:
        speak("lets start ....")
        score = 0
        speak("python developed in which year....")
        answer = takeCommand()
        if answer == "1991":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("which keyword is used in creating functions in python........")
        answer = takeCommand()
        if answer == "yes":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("what are instances of classes in python called.....")
        answer = takeCommand()
        if answer == "object":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)
    elif "math quiz" in query:
        speak("lets start ....")
        score = 0
        speak("which is the only even prime number....")
        answer = takeCommand()
        if answer == "2":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("longest side of right angled triangle........")
        answer = takeCommand()
        if answer == "hypotenuse":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("sides of the regular polygon are.....")
        answer = takeCommand()
        if answer == "equal":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)

    else:
        speak("Sorry this in not available yet.")


query = Entry(win, font="Arial 24 bold")


def mail(query):
    speak("Whom should i send ....")

    def click():
        try:
            sender = 'pythonproject171@gmail.com'
            password = 'fchzlnnhwqxyaxis'
            receiver = query.get()
            print(receiver)
            speak("What will be the Subject.....")
            subject = takeCommand()
            speak("What should i send ....")
            body = takeCommand()

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


def start():
    greetme()

    asked = takeCommand().lower()

    if 'wikipedia' in asked:
        speak('Searching Wikipedia...')
        # asked = asked.replace("wikipedia", "")
        results = wikipedia.summary(asked, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        print(asked)

    elif "alexa" in asked:
        speak(" hmmmmmmm We are just friends....")
    elif "friends" in asked:
        speak("I am an outsider struggling to get friends.")
    elif "what's your name" in asked or "what is your name" in asked:
        speak("My friends call me Sahayak")
    elif "who made you" in asked or "who created you" in asked:
        speak("I have been created by the team Codemons.")
    elif "how are you" in asked:
        speak("Just struggling among famous assistant ...")

    elif 'youtube' in asked:
        speak("opening youtube")
        webbrowser.open("youtube.com")

    elif 'google' in asked:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in asked:
        webbrowser.open("stackoverflow.com")

    elif 'spotify' in asked:
        webbrowser.open("spotify.com")

    elif 'lms' in asked:
        webbrowser.open("https://lms.bennett.edu.in/ilearn-support.php")

    elif 'play music' in asked:
        speak("Here you go with music")
        music_dir = "Music (1)"
        songs = os.listdir(music_dir)
        r = random.choice(songs)
        os.startfile(os.path.join(music_dir, r))

    elif 'time' in asked:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strtime}")
        print(asked)

    elif "calculate" in asked:

        try:
            ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
            res = ap.query(asked)
            print(next(res.results).text)
            speak(next(res.results).text)
        except:
            print("not able to calculate")
            speak("not able to calculate")

    elif "weather" in asked:
        try:
            ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
            res = ap.query(asked)
            print(next(res.results).text)
            speak(next(res.results).text)
        except:
            speak("no internet")
            print("no internet")
            print(asked)

    elif "temperature" in asked:
        try:
            ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
            res = ap.query(asked)
            print(next(res.results).text)
            speak(next(res.results).text)
        except:
            ap = wolframalpha.Client("K4P5WE-36YLXEWVVH")
            res = ap.query(asked)
            print("no internet")
            speak("no internet")

    elif 'stop' in asked:
        speak("Good bye It was nice interacting with you")
        quit()

    elif "search" in asked:
        temp1 = asked.replace(' ','+')
        temp2 = temp1.replace('search',' ')
        g_url = "https://www.google.com/search?q="
        webbrowser.open(g_url+temp2)
        print(asked)

    elif "joke" in asked:
        jokes = pyjokes.get_joke()
        speak(jokes)

    elif "science quiz" in asked:

        speak("lets start ....")
        score = 0
        speak("which is the most abundant gas in earth atmosphere..")
        answer = takeCommand()
        if answer == "nitrogen":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("which metal is the best conductor of electricity..")
        answer = takeCommand()
        if answer == "silver":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("who gave black hole theory")
        answer = takeCommand()
        if answer == "stephen hawking":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)
    elif "translate" in asked:
        speak("what do you want to translate...")
        og_lang = takeCommand()
        speak("the language In which  you want to convert.")
        dest_lang = takeCommand().lower()
        while (dest_lang not in lang):
            speak("Language in which you are trying to convert is currently unavailable.")
            speak("Please try different language.")
            dest_lang = takeCommand().lower()

        dest_lang = lang.get(dest_lang)


        translation = Translator().translate(og_lang, dest=dest_lang)
        converted_text = translation.text


        converted_audio = gTTS(text=converted_text, lang=dest_lang, slow=False)


        converted_audio.save("converted_language.mp3")
        PS("converted_language.mp3")
        os.remove("converted_language.mp3")

    elif "python quiz" in asked:
        speak("lets start ....")
        score = 0
        speak("python developed in which year....")
        answer = takeCommand()
        if answer == "1991":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("which keyword is used in creating functions in python........")
        answer = takeCommand()
        if answer == "def":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("what are instances of classes in python called.....")
        answer = takeCommand()
        if answer == "object":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)
    elif "math quiz" in asked:
        speak("lets start ....")
        score = 0
        speak("which is the only even prime number....")
        answer = takeCommand()
        if answer == "2":
            speak("well done ..... correct answer")
            score+=10
        else:
            speak("oops that's not the correct answer")

        speak("longest side of right angled triangle........")
        answer = takeCommand()
        if answer == "hypotenuse":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak("sides of the regular polygon are.....")
        answer = takeCommand()
        if answer == "equal":
            speak("well done ..... correct answer")
            score += 10
        else:
            speak("oops that's not the correct answer")
        speak(f"You scored %s out 0f 30"%score)
    else:
        speak("Sorry I am not familiar with that expression")


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
canvas.pack(fill=BOTH, expand=True)
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


#win.bind("<Configure>",event)
win.mainloop()
