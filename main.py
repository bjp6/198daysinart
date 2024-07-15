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

print("Pins defined")

i2c = I2C(id=id, sda=sda, scl=scl)

print("i2c adress accepted")

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

    print("servos in position 0")
    
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

    utime.sleep(5)

    for i in range (180,-1, -1):
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
  
def ultra():
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
    distance = (timepassed * 0.0343) / 2
    print(timepassed)
    print("The distance from object is ",distance,"cm")
    if distance < 150:
        enter_zone()

while True:
    ultra()#reads the ultrasonic sensors and starts functions accordingly
    utime.sleep(1)

