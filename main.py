from machine import Pin, I2C
import pca9685
import utime
from servo import Servos
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

#OTA Updater for use when the pico is fully installed in our project
firmware_url = "https://raw.githubusercontent.com/bjp6/198daysinart/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

us1_trigger = Pin(3, Pin.OUT)
us1_echo = Pin(2, Pin.IN)
us2_trigger = Pin(4, Pin.OUT)
us2_echo = Pin(5, Pin.IN)

sda = Pin(0)
scl = Pin(1)
id=0

i2c = I2C(id=id, sda=sda, scl=scl)

pca = pca9685.PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)

def ultra1():
    print('starting to measure uv sensor 1')
    us1_trigger.low()
    utime.sleep_us(2)
    us1_trigger.high()
    utime.sleep_us(5)
    us1_trigger.low()
    while us1_echo.value() == 0:
        signaloff = utime.ticks_us()
    while us1_echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance1 = (timepassed * 0.0343) / 2
    print ('distance1',distance1)
    return distance1

def ultra2():
    print('starting to measure uv sensor 2')
    us2_trigger.low()
    utime.sleep_us(2)
    us2_trigger.high()
    utime.sleep_us(5)
    us2_trigger.low()
    while us2_echo.value() == 0:
        signaloff = utime.ticks_us()
    while us2_echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance2 = (timepassed * 0.0343) / 2
    print ('distance2',distance2)
    return distance2

    
while True:
    if ultra1()<50 or ultra2() < 50:
        servo.position(index=0, degrees=180)
        servo.position(index=1, degrees=180)
        servo.position(index=2, degrees=180)
        servo.position(index=3, degrees=180)
        servo.position(index=4, degrees=180)
        servo.position(index=5, degrees=180)
        servo.position(index=6, degrees=180)
        servo.position(index=7, degrees=180)
        servo.position(index=8, degrees=180)
        utime.sleep(10)
        print('end phase 180')
        
    if ultra1()<50 or ultra2() < 50:
        servo.position(index=0, degrees=0)
        servo.position(index=1, degrees=0)
        servo.position(index=2, degrees=0)
        servo.position(index=3, degrees=0)
        servo.position(index=4, degrees=0)
        servo.position(index=5, degrees=0)
        servo.position(index=6, degrees=0)
        servo.position(index=7, degrees=0)
        servo.position(index=8, degrees=0)
        utime.sleep(10)
        print('end phase 0 second time')
        
    if ultra1()<50 or ultra2() < 50:
        servo.position(index=0, degrees=180)
        utime.sleep(2)
        servo.position(index=8, degrees=180)
        utime.sleep(2)
        servo.position(index=1, degrees=180)
        utime.sleep(2)
        servo.position(index=7, degrees=180)
        utime.sleep(2)
        servo.position(index=2, degrees=180)
        utime.sleep(2)
        servo.position(index=6, degrees=180)
        utime.sleep(2)
        servo.position(index=3, degrees=180)
        utime.sleep(2)
        servo.position(index=5, degrees=180)
        utime.sleep(2)
        servo.position(index=4, degrees=180)
        utime.sleep(5)
                
    while ultra1() > 50 and ultra2() > 50:
        #end position
        servo.position(index=0, degrees=45)
        utime.sleep(1)
        servo.position(index=1, degrees=135)
        utime.sleep(1)
        servo.position(index=2, degrees=45)
        utime.sleep(1)
        servo.position(index=3, degrees=135)
        utime.sleep(1)
        servo.position(index=4, degrees=45)
        utime.sleep(1)
        servo.position(index=5, degrees=135)
        utime.sleep(1)
        servo.position(index=6, degrees=45)
        utime.sleep(1)
        servo.position(index=7, degrees=135)
        utime.sleep(1)
        servo.position(index=8, degrees=45)
        utime.sleep(1)
