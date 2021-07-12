import cv2
import pytesseract
import numpy as np

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 

img = cv2.imread('newtest2.png')
gray = get_grayscale(img)
thresh = thresholding(gray)

# Adding custom options
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(thresh, config=custom_config)

text.splitlines()
text = text.split()
newarr = []
newarr2 = []

x = 0

def hasNumbers(str):
    return any(char.isdigit() for char in str)

for i in text:
    if x == 1:
        newarr.append(i)
    elif i == 'Home':
        x = 2
        print('hi')
    elif i == 'level' or i == 'Level':
        newarr.append(i)
        x = 1
    else:
        continue

for i in newarr:
    if '-' in i or "\\" in i or '>' in i or '<' in i:
        continue
    elif hasNumbers(i) == True:
        newarr2.append(i)
    elif 'Joe' not in i and 'KING' not in i and 'ice' not in i:
        continue
    else:
        newarr2.append(i)
    
    

print(newarr2)