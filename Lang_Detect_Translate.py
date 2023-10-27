# requirement : pip install googletrans
# command : python3 Lang_Detect_Translate.py 'Hello! C’est gratuit.'
# it can detect language other tahn english in a sentence. it also translate. 

from googletrans import Translator
import sys

input_text = sys.argv[1]

translator= Translator()

translation = translator.translate(input_text)

#print(translation)
print(f" Detected Language : ({translation.src}) ")
print(f"{translation.origin} ({translation.src}) ---> {translation.text} ({translation.dest})")




