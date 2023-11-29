# requirement: pip install winshell

import winshell

def main():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)

        print ("Recycle bin is emptied now")

    except: 
        print(" Recycle bin is already empty!")

if __name__ == '__main__':
    main()