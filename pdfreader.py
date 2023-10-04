import pyttsx3
import PyPDF2
speaker = pyttsx3.init()
book = open('1-1100-Words-You-Need-to-Know.pdf','rb')
Reader = PyPDF2.PdfReader(book)
pages = len(Reader.pages)
print(pages)
for num in range(50, pages):
    page = Reader.pages[num]
    text = page.extract_text()
    speaker.setProperty('rate',120)
    speaker.say(text, )
    speaker.runAndWait()