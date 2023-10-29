# requirement : pip install gofile
# command : python3 Cloud_Multi_Transfer.py <list of files to upload seperated by space>

try:
    import gofile as go
except ImportError:
    print("Please install the required module: pip install gofile")
    exit()

import sys

# Define a function to upload files to the cloud server and generate download links
def Store_Files(files):
    for file in files:
        # Get the current server from gofile
        cur_server = go.getServer()

        # Print the current server
        print(cur_server)

        # Upload the file to the cloud server
        url = go.uploadFile(file)

        # Print the link to download the file
        print(f"Download Link for {file}: {url['downloadPage']}")

def main():
    # Check if at least one file is provided as a command line argument
    if len(sys.argv) < 2:
        print("Please provide file(s) to upload.")
        exit()

    files = sys.argv[1:]  # Get all file names provided as arguments
    Store_Files(files)

if __name__ == "__main__":
    main()
