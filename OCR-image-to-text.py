import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\OCR\tesseract.exe"

def convert():
    image = Image.open('image.jpg')
    text = pytesseract.image_to_string(image)
    print(text)
    
convert()


