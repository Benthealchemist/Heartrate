# Ben Woodington 28th November 2018; Dept. of Chemical Engineering and Biotechnology, University of Cambridge

from time import sleep
import time
import serial
import datetime
import datetime as dt
import numpy as np
import hr_plotter


ser = serial.Serial('/dev/tty.usbmodem14201', 9600)

MAX_HISTORY = 250
# Keep a log of previous values for 250 'logs'

history = []
TOTAL_BEATS = 30
# pulse_graph=[]

# This should be moved into its own .py file
def calculate_bpm(beats):
    beats = beats[-TOTAL_BEATS:]
    beat_time = beats[-1] - beats[0]
    if beat_time:
        bpm = (len(beats) / (beat_time)) * 60
        # print ("%d bpm" % bpm)
        ts = time.time() #reactivate this only if  time stamp is needed
        print (datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d, %H:%M:%S, ')+ ("%d bpm" % bpm)) #reactivate this only if  time stamp is needed
        # print (bpm)
        # live_plotter()

def detect():
    history = []
    beats = []
    beat = False

    while True:
         v = ser.readline()
         if v:
             v3=int(v); #if you want to convert to float you c  an use "float" instead of "int"
             v3=v3+5;
             # print(v3)

         # print(v)
         # sleep(.01)

             history.append(v3)
             history = history[-MAX_HISTORY:]

             minima, maxima = min(history), max(history)

             threshold_on = (minima + maxima * 3) //4   # 3/4
             threshold_off = (minima + maxima) // 2      # 1/2

             if v3 > threshold_on and beat == False:
                 beat = True
                 beats.append(time.time())
                 beats = beats[-TOTAL_BEATS:]
                 calculate_bpm(beats)
             if v3 < threshold_off and beat == True:
                  beat = False




# Use this to test pulse detection with your Ardunio in Bash in stead of the above if loop
             # if v3 > threshold_on:
             #     print ("PULSE")
             #
             # if v3 < threshold_off:
             #     print ("0")
# initialise the fucntion
detect()
