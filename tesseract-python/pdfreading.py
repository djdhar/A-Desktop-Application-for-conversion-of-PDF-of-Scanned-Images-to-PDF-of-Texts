import cv2
import pdf2image
import pytesseract
import djdhar.imageloc as imageloc
import numpy
import sys
#Comment

import djdhar.pdfgenerator as gen
from pdf2image import convert_from_path, convert_from_bytes

def PtoCV(pil_image):
    open_cv_image = numpy.array(pil_image) 
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    return open_cv_image

i=0
pdfname = sys.argv[1]
images = convert_from_path(pdfname)
pages = []
for image in images:
    image = PtoCV(image)
    print("\n*************************:P********\nPage Numer = "+str(i+1)+"\n**********************************\n")
    pages.append([imageloc.Localize(image),len(image),len(image[0])])
    i=i+1
    #text = pytesseract.image_to_string(image, lang = 'eng')
    #print(text)
"""
i=0
for page in pages:
    print('\npage = '+str(i)+" , "+str(page[1])+" , "+str(page[2])+"\n\n")
    for info in page[0]:
        print(info[0]+" , "+str(info[1])+"\n")
    print('\n*********************************************\n')
"""

output = gen.GeneratePdf(pages,pdfname)
print("OCR PDF -> "+output+" ready !!")
