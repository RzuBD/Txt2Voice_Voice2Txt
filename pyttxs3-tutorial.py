import pyttsx3 

text2speech = pyttsx3.init()
mywords = input('write some thing I will read it for you\n')
rate = text2speech.getProperty('rate')
text2speech.setProperty('rate',140)
text2speech.say(mywords)
text2speech.runAndWait()