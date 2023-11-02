import pywhatkit as kit
import cv2
from PIL import Image, ImageDraw, ImageFont

''' 
# this is with pywhatkit library, sometimes it gives api error so below is the new method
def handwritten(Handwritten):

    try:
        kit.text_to_handwriting(Handwritten, save_to="handwritten.png")
        img = cv2.imread("handwritten.png")
        cv2.imshow("Handwritten Text", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("An error occurred:", e)

'''

# Function to generate handwritten text
def generate_handwritten_text(text, font_size=60):
    # Create an image object
    image = Image.new("RGB", (500, 200), "white")
    draw = ImageDraw.Draw(image)

    # Select a font and set font size
    font = ImageFont.load_default()

    # You can also load custom fonts by providing the path to the font file
    # font = ImageFont.truetype("path/to/font.ttf", font_size)

    draw.text((10, 10), text, fill="black", font=font)
    
    # Save the handwritten text image
    image.save("handwritten_text.png")

def main():
    text = input("Enter your text to convert in Handwriting : ")
    generate_handwritten_text(text)

if __name__ == '__main__':
    main()


