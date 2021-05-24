import speech_recognition as sr

def recognize(filename):

    testFile = sr.AudioFile(filename)

    r = sr.Recognizer()

    with testFile as source:
        audio = r.record(source)

    return r.recognize_google(audio,language="ru-RU")