import PyPDF2
import sys

# pdf path or file
pdf_file = sys.argv[1]

# open pdf file to read the content
with open(pdf_file, 'rb') as pdf:
    pdf_reader = PyPDF2.PdfFileReader(pdf)

    # open a new word file to write pdf content
    with open('PdfToWord.docx', 'w') as doc:
        for page in range(pdf_reader.numPages):
            text = pdf_reader.getPage(page).extractText()
            doc.write(text)