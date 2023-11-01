# command : python3 Secure_password_genrator.py <password length>

try:
    import random
    import string
    import sys
except ImportError:
    print("ImportError") 

def generate_password(length):

    # define character pool for password generation
    charcters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    # random charcter selection for password
    password = ''.join(random.choice(charcters) for _ in range(length))

    return password

def main():
    password_length = int(sys.argv[1])
    Pass = generate_password(password_length)
    print("Generated Password:", Pass)

if __name__ == '__main__':
    main()



