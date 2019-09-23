#!/usr/bin/python3

import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import os

#SETUP-----------------------------------------
Set_Humidity = 70

sensor = Adafruit_DHT.DHT11


GPIO.setmode(GPIO.BCM)

#number of plants + 1
num = 3

#Enter pins for sensors

DHT_pin = [0,3,4]
humidity = [0]
temperature = [0]

#Humidity Control Pins

Plant_1 = 14

GPIO.setup(Plant_1, GPIO.OUT)
GPIO.output(Plant_1, GPIO.LOW)

print("Waiting for sensor to settle...")

time.sleep(2)

#Update readings---------------------------------- 
for i in range(1,num):
    
    time.sleep(2)
    
    humidity_tmp, temperature_tmp = Adafruit_DHT.read_retry(sensor, DHT_pin[i])
    
    humidity.append(humidity_tmp)
    temperature.append(temperature_tmp)
    
for i in range(1,num):
   
    if humidity is not None and temperature is not None:
        print(' Plant number {0:d} Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(i,temperature[i], humidity[i]))
    else:
        i -= i
        
#Control based on readings------------------------------------------------
        
for i in range(1,num):
    
    time.sleep(2)
    
    if humidity[i] < Set_Humidity:
        print(' Plant {0:d} needs humidty'. format(i))
        
    else:
        print("Plant humidity is okay")