import cv2
import numpy as np
import djdhar.image_example as image_example

def binarize(gray):
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    return thresh1

def Localize(img):
    #img = cv2.imread(s)
    """
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    linek = np.zeros((11,11),dtype=np.uint8)
    linek[5,...]=1
    x=cv2.morphologyEx(gray, cv2.MORPH_OPEN, linek ,iterations=1)
    gray-=x
    kernel = np.ones((5,5), np.uint8)
    ret2,gray = cv2.threshold(gray,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    gray = cv2.dilate(gray, kernel, iterations=1) 
    contours2, hierarchy = cv2.findContours(gray,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    """
    backup=img.copy()
    #np.copy(backup, img)
    retu = []
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
    
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)) 
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    
    kernel = np.ones((1,60), np.uint8)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel,iterations=3)
    
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)) 
    dilation = cv2.dilate(closing, rect_kernel, iterations = 1)
    contours2, hierarchy = cv2.findContours(closing, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE) 

    x=0
    otsu = binarize(gray)
    print("\n Total phrases = "+str(len(contours2))+"\n")
    while x<len(contours2):
        (start_x,start_y,width,height)= cv2.boundingRect(contours2[x])
        print("Phrase Number = "+str(x))
        mymat = otsu[start_y:start_y+height, start_x:start_x+width]
        retu.append([image_example.OCR(mymat),[start_x,start_y,width,height]])
        cv2.rectangle(backup, (start_x,start_y),(width+start_x,height+start_y),(0,0 ,255), 2)
        x=x+1
    #cv2.imwrite('temp.png',backup)
    return retu