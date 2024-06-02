#This will be my main file for the 198 cards project
from machine import Pin, I2C
import pca9685
from servo import Servos
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/bjp6/198daysinart"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()
sda = Pin(0)
scl = Pin(1)
id=0

i2c = I2C(id=id, sda=sda, scl=scl)

pca = pca9685.PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)
servo.position(index=0, degrees=0)
servo.position(index=1, degrees=0)
servo.position(index=2, degrees=0)
servo.position(index=3, degrees=0)
