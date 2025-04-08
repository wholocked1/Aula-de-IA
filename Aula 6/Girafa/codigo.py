import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

img = cv2.imread('./GIRAFA.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Filtro de ruído (bluring)
img_blur = cv2.blur(img,(5,5))

#Convertendo para preto e branco (RGB -> Gray Scale -> BW)
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_RGB2GRAY)
a = img_gray.max()
_, thresh = cv2.threshold(img_gray, a/2+100, a,cv2.THRESH_BINARY_INV)

#preparando o "kernel"
kernel = np.ones((12,12), np.uint8)

img_dilate = cv2.dilate(thresh,kernel,iterations = 1)
img_erode = cv2.erode(thresh,kernel,iterations = 1)
img_open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
img_close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# contorno
contours, hierarchy = cv2.findContours(
                                   image = img_close,
                                   mode = cv2.RETR_TREE,
                                   method = cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)
img_copy = img.copy()
final = cv2.drawContours(img_copy, contours, contourIdx = -1,
                         color = (255, 0, 0), thickness = 2)


#plot imagens
imagens = [img,img_blur,img_gray,img_dilate, img_erode, img_open, img_close,final]
formatoX = math.ceil(len(imagens)**.5)
if (formatoX**2-len(imagens))>formatoX:
    formatoY = formatoX-1
else:
    formatoY = formatoX
for i in range(len(imagens)):
    plt.subplot(formatoY, formatoX, i + 1)
    plt.imshow(imagens[i],'gray')
    plt.xticks([]),plt.yticks([])
plt.show()
plt.imshow(final)
