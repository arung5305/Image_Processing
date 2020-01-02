import numpy as np
import glob
import shutil
import os
from PIL import Image
import math
import scipy.misc
import cv2

#src_dir = "C:\\Users\\bhuiy\\Desktop\\Full AREDS data for Comp4\\Cropped\\2010"
t1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\RGB\\Training\\1"
t4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\RGB\\Training\\4"
v1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\RGB\\Validation\\1"
v4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\RGB\\Validation\\4" 


# green only
gt1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\JUSTGREEN\\Training\\1"
gt4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\JUSTGREEN\\Training\\4"
gv1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\JUSTGREEN\\Validation\\1"
gv4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\JUSTGREEN\\Validation\\4" 


#rgb -- median
mt1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\RGBMedian\\Training\\1"
mt4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\RGBMedian\\Training\\4"
mv1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\RGBMedian\\Validation\\1"
mv4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\RGBMedian\\Validation\\4" 


#Histogramequal
ht1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\Histogramequal\\Training\\1"
ht4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\Histogramequal\\Training\\4"
hv1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\Histogramequal\\Validation\\1"
hv4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\Histogramequal\\Validation\\4" 


#GREENSOBEL
st1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\GREENSOBEL\\Training\\1"
st4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\GREENSOBEL\\Training\\4"
sv1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\GREENSOBEL\\Validation\\1"
sv4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\GREENSOBEL\\Validation\\4" 


#GreenMedian
gmt1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\GreenMedian\\Training\\1"
gmt4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\GreenMedian\\Training\\4"
gmv1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\GreenMedian\\Validation\\1"
gmv4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\GreenMedian\\Validation\\4" 



#Cropped-RGB
ct1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\Cropped-RGB\\Training\\1"
ct4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\Cropped-RGB\\Training\\4"
cv1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\Cropped-RGB\\Validation\\1"
cv4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\Cropped-RGB\\Validation\\4" 


#ContrastStretchingAndMedian
cmt1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\ContrastStretchingAndMedian\\Training\\1"
cmt4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\ContrastStretchingAndMedian\\Training\\4"
cmv1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\ContrastStretchingAndMedian\\Validation\\1"
cmv4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\ContrastStretchingAndMedian\\Validation\\4" 


#ContrastStretching
cst1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\ContrastStretching\\Training\\1"
cst4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\ContrastStretching\\Training\\4"
csv1 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\ContrastStretching\\Validation\\1"
csv4 = "C:\\Users\\bhuiy\\Desktop\\Perfect dataset\\ContrastStretching\\Validation\\4" 







for jpgfile in glob.iglob(os.path.join(t1,"*.jpg")):
    #print(os.path.basename(jpgfile))
    #img = cv2.imread(jpgfile)
    img = Image.open(jpgfile)
    img = np.array(img)
    #img1 = cv2.Laplacian(img[...,1],cv2.CV_64F)
    #img2 = img[...,1]
    greenOnly = img[...,1]
    dst_dir = 
    scipy.misc.imsave(os.path.join(dst_dir,os.path.basename(jpgfile)), greenOnly)
    rgbnorm = img
    print(rgbnorm.shape)
    for i in range (0,250):
        for j in range (0,250):
            den = rgbnorm[i][j][0] + rgbnorm[i][j][1] + rgbnorm[i][j][2]
            if den == 0:
                den = 1
            r = rgbnorm[i][j][0] / den
            g = rgbnorm[i][j][1] / den
            b = rgbnorm[i][j][2] / den
            rgbnorm[i][j][0] = r
            rgbnorm[i][j][1] = g
            rgbnorm[i][j][2] = b
    img2 = cv2.cvtColor(img,cv2.COLOR_RGB2XYZ)
    for i in range (0,250):
        for j in range (0,250):
            den = img2[i][j][0] + img2[i][j][1] + img2[i][j][2]
            if den == 0:
                den = 1
            r = img2[i][j][0] / den
            g = img2[i][j][1] / den
            b = img2[i][j][2] / den
            img2[i][j][0] = r
            img2[i][j][1] = g
            img2[i][j][2] = b
    #img3 = cv2.Canny(img,10,100)
    scipy.misc.imsave(os.path.join(dst_dir,os.path.basename(jpgfile)), rgbnorm)
    #break;
