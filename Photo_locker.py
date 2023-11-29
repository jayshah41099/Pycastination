# requirement - pip install cryptography

from cryptography.fernet import Fernet
import sys

def Photo_locker(img):

    key = Fernet.generate_key()
    with open('key.key', 'wb') as f:
        f.write(key)

    fernet = Fernet(key)
    with open(img, 'rb') as f:
        photo = f.read()

    lock = fernet.encrypt(photo) 
    with open(img, 'wb') as lock_pic:
        lock_pic.write(lock)

    print (" your photo is locked!")

if __name__ == '__main__':
    img = sys.argv[1]
    Photo_locker(img)


