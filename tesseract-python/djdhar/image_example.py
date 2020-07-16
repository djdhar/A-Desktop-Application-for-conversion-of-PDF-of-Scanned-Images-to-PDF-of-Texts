from PIL import Image
import pytesseract
import cv2

def OCR(mat):
   return pytesseract.image_to_string(mat, lang = 'eng') 

"""
im = Image.open("sample1.jpg")
im = cv2.imread("sample1.jpg")
print(im)
text = pytesseract.image_to_string(im, lang = 'eng')

print(text)
"""
