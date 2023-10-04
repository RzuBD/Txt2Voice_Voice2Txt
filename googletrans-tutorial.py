# import speech_recognition as sr 
# r = sr.recognizer()


from googletrans import Translator

translator = Translator()

language = ['en', 'fr', 'es', 'it', 'de', 'ru']
text = input('what text would you like to translate')
for l in language:
    # tr = Translator(provider = 'libre', from_lang='en', to_lang=language)
    translation = translator.translate(text, dest =l, src='en')
    print(f'{l}:>> {translation.text}')
    