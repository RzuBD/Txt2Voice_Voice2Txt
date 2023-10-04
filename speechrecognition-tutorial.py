import speech_recognition as sr
import pyaudio

source = sr.Recognizer()

with sr.Microphone() as microphone:
    print('please say something')
    your_voice = source.listen(microphone)
    print('Time out')
Text = source.recognize_google(your_voice, language='en-US' )
print(Text)
print(source.recognize_google(your_voice, language = 'en'))