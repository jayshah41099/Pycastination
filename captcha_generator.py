# requirement: pip install captcha & pip install PIL
# command : python3 captcha_generator.py

from captcha.image import ImageCaptcha
from PIL import Image, ImageDraw
import string
import random

# generate a 6 charcter captcha text 
def generate_catcha_text(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# generates easy for scanner to read captcha
def Captcha_as_image(image_width = 300, image_height = 100, save_path = 'captcha.png'):
    image = ImageCaptcha(width=image_width, height=image_height)
    captcha_text = generate_catcha_text()
    image.generate(captcha_text)
    image.write(captcha_text, save_path)
    return captcha_text

# generates difficult for scanner to read captcha
def create_noisy_text(text, output_path):
    image = ImageCaptcha()
    captcha = image.generate(text)
    noisy_image = Image.open(captcha)
    noisy_image = noisy_image.convert("RGB")
    
    draw = ImageDraw.Draw(noisy_image)
    for _ in range(50):  # Adding random noise
        x = random.randint(0, 299)
        y = random.randint(0, 99)
        draw.point((x, y), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        
    noisy_image.save(output_path)
    return noisy_image

def main():
    # generates easy for scanner to read captcha
    CaptchaImage = Captcha_as_image()
    print(" CAPTCHA text: ", CaptchaImage)
    
    # generates difficult for scanner to read captcha
    captcha_text = generate_catcha_text()
    noisy_image = create_noisy_text(captcha_text,'Captcha1.png')
    print(" CAPTCHA text: ", captcha_text)
    
if __name__ == "__main__":
    main()