import cv2
from PIL import ImageGrab
import numpy as np
import pytesseract as ptr

screen_box = (700, 300, 1400, 900)

def read_screen(vartices):
    screen = ImageGrab.grab(bbox=vartices)
    return screen
        
def display_screen(image_array):
    image = cv2.cvtColor(np.array(image_array), cv2.COLOR_BGR2GRAY)
    while True:
        cv2.imshow('screen',image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

def read_text_from_screen(screen):
    read_text = ptr.image_to_string(screen)
    return read_text


def recognize_content():
    
    pass

def recognize_object():
    pass

def input_keys():
    pass

if '__name__' == '__main__':
    screen = read_screen(screen_box)
    display_screen(screen)
