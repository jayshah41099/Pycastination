import time

def stopwatch(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print (timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

        print("stop")
    
def main(): 
    num = int(input("set your StopWatch in seconds : "))
    stopwatch(num)

if __name__ == '__main__':
    main()