import speech_recognition as SR
from googletrans import Translator
from gtts import gTTS
from playsound import playsound as PS
import os

# A dictionary containing all the languages as key and codes of the language as value
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

# Capture voice which takes command through microphone
def input_commands():
	recognizer = SR.Recognizer()
	with SR.Microphone() as mic:
		print("Speak Now")
		recognizer.adjust_for_ambient_noise(mic)
		audio = recognizer.listen(mic)
	try:
		input_query = recognizer.recognize_google(audio, language = "en-in")
		print(f"'{input_query}'")
	except Exception:
		print("Say again please...")
		input_query = input_commands()
	return input_query

# Input from user and make it to lowercase
og_lang = input_commands()

def destination_language():
	print("The language in which you want to convert:")
	
    # Input destination language in which the user wants to translate
	dest_lang = input_commands()
	return dest_lang.lower()

dest_lang = destination_language()

# Mapping it with the code
while (dest_lang not in lang):
	print("Language in which you are trying to convert is currently unavailable.")
	print("Please try different language.")
	print()
	dest_lang = destination_language()

dest_lang = lang.get(dest_lang)

# Translating from mic to dest
translation = Translator().translate(og_lang, dest = dest_lang)
converted_text = translation.text

# Using Google-Text-to-Speech ie, gTTS() method to speak the translated text into the
# destination language which is stored in dest_lang.
# Also, we have given 3rd argument as False because by default it speaks very slowly
converted_audio = gTTS(text = converted_text, lang = dest_lang, slow = False)

# Using save() method to save the translated speech in converted_language.mp3
converted_audio.save("converted_language.mp3")

# Using OS module to run the translated voice.
PS("converted_language.mp3")
os.remove("converted_language.mp3")
print(converted_text)