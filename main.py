import cv2
from PIL import ImageGrab
import numpy as np
screen_box = (700, 300, 1400, 900)

def read_screen(vartices):
    while(True):
        screen = ImageGrab.grab(bbox=vartices)
        image = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
        cv2.imshow('screen',image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def recognize_content():
    pass

def recognize_object():
    pass

def input_keys():
    pass

if '__name__' == '__main__':
    read_screen(screen_box)
