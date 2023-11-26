import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print (timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("\n\t !!!!!! TIME IS UP !!!!!!!")

def main():
    num = int(input("Set your timer (in seconds): "))
    countdown(num)

if __name__ == '__main__':
    main()