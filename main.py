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

"""trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)"""

sda = Pin(0)
scl = Pin(1)
id=0

i2c = I2C(id=id, sda=sda, scl=scl)

pca = pca9685.PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)

def enter_zone():
    """c = 0
    while c <= 3:
        servo.position(index=0, degrees=130)
        servo.position(index=1, degrees=130)
        servo.position(index=2, degrees=130)
        servo.position(index=3, degrees=130)
        servo.position(index=4, degrees=130)
        servo.position(index=5, degrees=130)
        servo.position(index=6, degrees=130)
        servo.position(index=7, degrees=130)
        servo.position(index=8, degrees=130)
        utime.sleep(2)
        servo.position(index=0, degrees=45)
        servo.position(index=1, degrees=45)
        servo.position(index=2, degrees=45)
        servo.position(index=3, degrees=45)
        servo.position(index=4, degrees=45)
        servo.position(index=5, degrees=45)
        servo.position(index=6, degrees=45)
        servo.position(index=7, degrees=45)
        servo.position(index=8, degrees=45)
        utime.sleep(2)
        c = c+1"""
        
    servo.position(index=0, degrees=0)
    servo.position(index=1, degrees=0)
    servo.position(index=2, degrees=0)
    servo.position(index=3, degrees=0)
    servo.position(index=4, degrees=0)
    servo.position(index=5, degrees=0)
    servo.position(index=6, degrees=0)
    servo.position(index=7, degrees=0)
    servo.position(index=8, degrees=0)
    
    """servo.position(index=0, degrees=0)
    servo.position(index=1, degrees=0)
    servo.position(index=2, degrees=0)
    servo.position(index=3, degrees=0)
    servo.position(index=4, degrees=0)
    servo.position(index=5, degrees=0)
    servo.position(index=6, degrees=0)
    servo.position(index=7, degrees=0)
    servo.position(index=8, degrees=0)
    utime.sleep(3)
    servo.position(index=0, degrees=180)
    servo.position(index=1, degrees=180)
    servo.position(index=2, degrees=180)
    servo.position(index=3, degrees=180)
    servo.position(index=4, degrees=180)
    servo.position(index=5, degrees=180)
    servo.position(index=6, degrees=180)
    servo.position(index=7, degrees=180)
    servo.position(index=8, degrees=180)
    utime.sleep(3)
    servo.position(index=0, degrees=0)
    servo.position(index=1, degrees=0)
    servo.position(index=2, degrees=0)
    servo.position(index=3, degrees=0)
    servo.position(index=4, degrees=0)
    servo.position(index=5, degrees=0)
    servo.position(index=6, degrees=0)
    servo.position(index=7, degrees=0)
    servo.position(index=8, degrees=0)"""
    
for i in range (0,180):
    servo.position(index=0, degrees=i)
    servo.position(index=1, degrees=i)
    servo.position(index=2, degrees=i)
    servo.position(index=3, degrees=i)
    servo.position(index=4, degrees=i)
    servo.position(index=5, degrees=i)
    servo.position(index=6, degrees=i)
    servo.position(index=7, degrees=i)
    servo.position(index=8, degrees=i)
    utime.sleep(0.030)   # move 1 degree and wait 20 milliseconds, relatively slow and smooth operation


  
"""def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print(timepassed)
    print("The distance from object is ",distance,"cm")
    if distance < 20:
        enter_zone()
""" 
while True:
    enter_zone()#when ultrasonic sensor is installed this should read ultra()
    utime.sleep(1)
