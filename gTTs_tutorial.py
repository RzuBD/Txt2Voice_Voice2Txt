from gtts import gTTS
import os

# only works online

with open("E:\\myTutorials\\NLP\\nlpenv\\frenchtext.txt", "r") as textfile:
    text = textfile.read().replace("\n", ".")
voice = gTTS(text, lang="fr", slow=False)
voice.save("newvoice.mp3")
os.system("newvoice.mp3")

# text = 'Hi arezou jaan this is gtts and only works online'
# voice = gTTS(text = text, lang ='en', slow = False)
# voice.save('myvoice_gtts.mp3')
# os.system('myvoice_gtts.mp3')
