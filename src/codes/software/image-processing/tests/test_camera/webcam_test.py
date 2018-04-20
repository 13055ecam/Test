#import RPi.GPIO as GPIO
import time
import cv2
#----------

#GPIO.cleanup()

#GPIO.setmode(GPIO.BCM) 
#GPIO.setup(4, GPIO.OUT) 

# Create an object called camera and connect the firt camera to the computer
camera = cv2.VideoCapture(0)

#GPIO.output(4, GPIO.LOW)
#time.sleep(1)
#GPIO.output(4, GPIO.HIGH)


# Take a photo and save it in the current folder 
return_value, image = camera.read()
cv2.imwrite('opencv'+'.png', image)

#GPIO.output(4,GPIO.LOW)
#GPIO.cleanup()


