from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass
import sys

def Password_protected(file):

    pdfwriter = PdfFileWriter()
    pdf = PdfFileReader(file)

    for page_num in range(pdf.numPages):
        pdfwriter.addPage(pdf.getPage(page_num))

    password = getpass.getpass(prompt="Enter Password to lock a file: ")
    pdfwriter.encrypt(password)

    with open(file, 'wb') as f:
        pdfwriter.write(f)

    print ("Now file is password protected")

def main():
    file = sys.argv[1]
    Password_protected(file)

if __name__ == '__main__':
    main()