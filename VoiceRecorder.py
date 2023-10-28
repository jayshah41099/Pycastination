# Requirement : pip install sounddevice
# command : python3 VoiceRecorder.py <duration>

import sounddevice
from scipy.io.wavfile import write
import sys

#sample_rate
fs=44100

# take recording time as input
second = int(sys.argv[1])
print("Recording ...\n")
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()
write("MyRecording.wav", fs, record_voice)
print(" Recording is done. check the MyRecording.wav file to listen recording!")
