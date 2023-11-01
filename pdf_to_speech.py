import PyPDF2, pyttsx3

# open pdf file to read
path = open('sample.pdf', 'rb')

# creating a pdf file reader object
pdfReader = PyPDF2.PdfFileReader(path)

# creating speeching instance
speak = pyttsx3.init()

# reading throgh the pages of file
for pages in range(pdfReader.numPages):
    text = pdfReader.getPage(pages).extractText()
    speak.say(text)
    

speak.runAndWait()
speak.stop()