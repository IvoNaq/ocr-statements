import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'images/Selection_021.png'

reader = easyocr.Reader(['es'], gpu = False)
result = reader.readtext(IMAGE_PATH)
print(result)