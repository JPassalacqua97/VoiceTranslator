import googletrans
from googletrans import Translator

def trans(MyText, language):
    Language = language.lower()

    langDict = googletrans.LANGUAGES
    abrev = ""

    for lang in langDict.items():
        if Language == lang[1]:
            #print("Found the language")
            abrev = lang[0]
            break

    #print(abrev)

    translator = Translator()
    result = translator.translate(MyText, dest=abrev)
    print(Language+" Translation: ",result.text + "\n")
    return result.text

