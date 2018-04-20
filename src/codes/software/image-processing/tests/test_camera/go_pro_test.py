from goprocam import GoProCamera
from goprocam import constants
#import RPi.GPIO as GPIO
import time
#----------

#GPIO.cleanup()

#GPIO.setmode(GPIO.BCM) 
#GPIO.setup(4, GPIO.OUT) 

# Connect GoPro
gpCam = GoProCamera.GoPro()

#GPIO.output(4, GPIO.LOW)
#time.sleep(1)
#GPIO.output(4, GPIO.HIGH)

# Take a photo and save it in the current folder 
gpCam.downloadLastMedia(gpCam.take_photo(0)) 

#GPIO.output(4,GPIO.LOW)
#GPIO.cleanup()


