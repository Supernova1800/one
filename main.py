import Rpi.GPIO as GPIO
from gpiozero import Button, LED, PWMLED
from picamera import PiCamera
from time import sleep
from lobe import ImageModel

# Load Lobe TF model
# --> Change model file path as needed
model = ImageModel.load('/home/pi/Lobe/model')

n=1
while True:
    if n==1:
        #take_photo()
        # Run photo through Lobe TF model
        result = model.predict_from_file('/home/pi/Pictures/image.jpg')
        # --> Change image path
        print(result.prediction)
        n=n+1
    else:
        break
        # Pulse status light
        #white_led.pulse(2,1)
    sleep(1)
