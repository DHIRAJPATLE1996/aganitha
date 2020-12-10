
import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as inputs:
    print("speak.....")
    listening = recognizer.listen(inputs)
    print("wait...")
    try:
        print("Did you say: "+recognizer.recognize_google(listening,language))
    except:
         print("please speak again")
