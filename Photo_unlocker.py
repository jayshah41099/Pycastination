# requirement - pip install cryptography
from cryptography.fernet import Fernet
import sys

def Photo_unlocker(img):

    with open('key.key', 'rb') as f:
        key = f.read()

    fernet = Fernet(key)
    with open(img, 'rb') as f:
        Photo = f.read()

    unlock = fernet.decrypt(Photo)
    with open(img, 'wb') as Unlock_photo: 
        Unlock_photo.write(unlock)

    print(" your photo is unlocked")

if __name__ == '__main__':
    img = sys.argv[1]
    Photo_unlocker(img)

