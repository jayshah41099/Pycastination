# requirement : pip install gofile
# command : python3 Cloud_Multi_Transfer.py <file>

try:
    import gofile as go
except ImportError:
    print(" Compler the requiremnt : pip install gofile")
    exit()

import sys

# define a function that takes a file you want to share
def Store_Files(file):

    # Get the cureent server from gofile
    cur_server = go.getServer()

    # print the current server
    print(cur_server)

    # upload the file on cloud server
    url = go.uploadFile(file)

    # print the link to download the file
    print("Download Link: ", url["downloadPage"])

def main():
    file = sys.argv[1]
    Store_Files(file)

if __name__ == "__main__":
    main()