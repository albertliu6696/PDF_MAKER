from picamera import PiCamera
from time import sleep

#{{{ Start and Cleanup Functions
def start(camera,res):
    camera.start_preview()
    camera.resolution = (res[0],res[1])
def finish(camera):
    camera.stop_preview()
    camera.close()
#}}}

def __init__():
    fpath = '/home/pi/Desktop/PDF_MAKER/'
    image_name = 'image'
    image_extension = '.jpg'
    image_cnter = 1
    resolution = [2592,1944]

    camera = PiCamera() #Create Camera Object
    start(camera,resolution)
    sleep(1)
    camera.capture(fpath+image_name+str(image_cnter)+image_extension)

    finish(camera)

__init__()

