import Rpi.GPIO as GPIO
from gpiozero import Button, LED, PWMLED
from picamera import PiCamera
from time import sleep
from lobe import ImageModel
import cv2

#usb camera
cam = cv2.videocapture(0) #number 0 represents main camera when using multiple camera change number to 1,2,3...etc
ret , img =cam.read()
cv2.imwrite("path/to/imagefolder/image_name.extension_name",img)

#to show the image
if ret:
    cv2.imshow("output folder name",img)
    cv2.waitKey(0) #delay
cam.release()

# Load Lobe TF model
# --> Change model file path as needed
model = ImageModel.load('/home/pi/Lobe/model')
result = model.predict_from_file('path/to/file.jpg')
pritnt(result.predection)
