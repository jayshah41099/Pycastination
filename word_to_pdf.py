# requirement: pip install reportlab
# command: python3 sample.txt

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
import sys

# Choose the paper size (Letter or A4)
page_width, page_height = A4  # Change to A4 if needed

# Create a new PDF file
pdf_file = canvas.Canvas("sample.pdf", pagesize=(page_width, page_height))

# input file
input_text = sys.argv[1]

# Open and read the text from a text file
with open(input_text, "r") as file:
    text = file.read()

# Calculate the width and height of the text box
text_width = page_width - 2 * inch  # Leave a 1-inch margin on both sides
text_height = page_height - 2 * inch  # Leave a 1-inch margin at the top and bottom

# Set the font name and size
font_name = "Helvetica"  # You can change the font name
font_size = 12

# Create a text object to handle text formatting
text_object = pdf_file.beginText(inch, page_height - inch)
text_object.setFont(font_name, font_size)
text_object.setTextOrigin(inch, page_height - inch)
text_object.textLines(text)
pdf_file.drawText(text_object)

# Save and close the PDF file
pdf_file.save()
