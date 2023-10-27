# requirement : pip install plyer
# command : python3 Laptop_notification.py

import time
from plyer import notification

def main():
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break! It has been an hour!",
            timeout = 10
        )
        time.sleep(15) # change the value to 3600 for every hour notification
        # you can set up this in linux - crontab or windows - task manager for it to autorun every hour

if __name__ == "__main__":
    main()