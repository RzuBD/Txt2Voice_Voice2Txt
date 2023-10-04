import pyttsx3

engine = pyttsx3.init()

text = "ok arezou jaan. good night and have sweet dreams. tommorow is a great day"
voices = engine.getProperty("voices")
engine.setProperty("rate", 140)

for voice in voices:
    t = voice.id
engine.setProperty("voice", id)
engine.say(text)
engine.save_to_file('text', 'text20.mp3')
# engine.save_to_file('hello', 'HelloSound.mp3')

# engine.save_to_file(text, "test.mp3")
# os.rename("test.mp3", "folder/nameIwanttogive.mp3")مس



engine.runAndWait()
