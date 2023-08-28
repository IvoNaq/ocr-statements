from PIL import Image
import pytesseract
import cv2
from matplotlib import pyplot as plt
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

print(pytesseract.image_to_string(Image.open('images/test.png')))
print(pytesseract.image_to_boxes(Image.open('images/test.png')))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open('images/test.png')))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open('images/test.png')))


# Get HOCR output
hocr = pytesseract.image_to_pdf_or_hocr('images/test.png', extension='hocr')

# Get ALTO XML output
xml = pytesseract.image_to_alto_xml('images/test.png')