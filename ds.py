#!/usr/bin/python
import os
import time
import urllib2
import RPi.GPIO as GPIO

print("initial setup")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED1 = 22
LED2 = 19
door1 = 18
door2 = 21

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(door1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(door2, GPIO.IN, GPIO.PUD_UP)

GPIO.output(LED1, False)
GPIO.output(LED2, False)
os.system("gpio mode 6 out && gpio mode 5 out")

while True:
    try:
        urllib2.urlopen("http://www.google.com").close()
    except urllib2.URLError:
        print("Not Connected to internet")
        os.system("gpio write 6 0 && gpio write 5 1")
        time.sleep(1)
    else:
        print("Connected to internet")
        print("connecting to server ...")
        print("connected")
        os.system("gpio write 6 1 && gpio write 5 0")
        print("updating sensor state to server every 1 second")
        while True:
            if GPIO.input(door1) == False:
                GPIO.output(LED1, True)
                print("Door 1 is closed.")
                time.sleep(2)
            else:
                if GPIO.input(door1) == True:
                    GPIO.output(LED1, False)
                    print("Door 1 is open.")
                    time.sleep(2)
                if GPIO.input(door2) == False:
                    GPIO.output(LED2, True)
                    print("Door 2 is closed.")
                    time.sleep(2)
                else:
                    if GPIO.input(door2) == True:
                        GPIO.output(LED2, False)
                        print("Door 2 is open.")
                        time.sleep(2)
        i = 1
        t = 1
        while i >= 40:
            print(t)
            os.system("gpio readall")
            t = t + 1
            time.sleep(1)

        break               
GPIO.cleanup()
        


