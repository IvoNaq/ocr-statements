from PIL import Image
import pytesseract
import cv2
from matplotlib import pyplot as plt
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

object = pytesseract.image_to_string(Image.open('images/test2.png')) 
print(object)
print(object[1])
#print(pytesseract.image_to_boxes(Image.open('images/test2.png')))

# Get verbose data including boxes, confidences, line and page numbers
#print(pytesseract.image_to_data(Image.open('images/test2.png')))

# Get information about orientation and script detection
#print(pytesseract.image_to_osd(Image.open('images/test2.png')))


# Get HOCR output
#hocr = pytesseract.image_to_pdf_or_hocr('images/test2.png', extension='hocr')

# Get ALTO XML output
#xml = pytesseract.image_to_alto_xml('images/test2.png')