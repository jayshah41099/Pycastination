# you can change the fps value to higher for faster and to lower for slower recording
# it require to take screenshot and compile it togetther in video. installation : scort for screent shot
# linux installation : sudo apt-get install scort
# terminal command : python3 Screen_Recorder.py <recording_duration>

import cv2
import numpy as np
import pyautogui
import sys

# set screen resolution to record
screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)

# video filename
output_filename = "screen_recording.mp4"

# set the frames per second for recording
fps = 10.0

#Define the codec and create videowriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_filename, fourcc, fps, resolution)

#define the recording duration in seconds
recording_duration = sys.argv[1]

# start the screen recording
for _ in range(int(fps * recording_duration)):
    #capture the screen
    screen = pyautogui.screenshot()

    #convert the screenshot to a numpy array and BGR format for OpenCV
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    #write the frame to ouput video
    out.write(frame)

# release the VideoWriter
out.release()
