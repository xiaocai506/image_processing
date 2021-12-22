from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt
import math
from shapely.affinity import scale
from shapely.ops import transform
from shapely.geometry import Polygon
import json
 
# Opening JSON file
f = open('dh-tshirt-panel.json')
data = json.load(f)
d=data.keys()

print(f)


def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

width=0.955
b, h = 4.748, 4.233 


img = cv2.imread("T11.jpeg")
# plt.imshow(img)
# plt.show()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
(cnts, _) = contours.sort_contours(cnts)
cnts_1=cnts[0]
detected_circles = cv2.HoughCircles(gray,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
               param2 = 30, minRadius = 1, maxRadius = 40)
pixelsPerMetric = None

for c in cnts:
    if cv2.contourArea(c) < 100:
        continue
    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    box = perspective.order_points(box)
    (tl, tr, br, bl) = box
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)
    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
    if pixelsPerMetric is None:
        pixelsPerMetric = dB / width
        #print(pixelsPerMetric)
        #p=math.floor(pixelsPerMetric)
        #print(p)

p=44

h, b =  10.61, 8.58

xp1, yp1 = 5.57, 1.02
xp2, yp2 = 0, 10.61


cx1, cy1   = 5.44, 2.76
cx2, cy2   = 5.39, 3.17
cx3, cy3   = 5.35, 3.56
cx4, cy4   = 5.32, 3.96
cx5, cy5   = 5.30, 4.35
cx6, cy6   = 5.28, 4.75
cx7, cy7   = 5.28, 5.14
cx8, cy8   = 5.28, 5.53
cx9, cy9   = 5.30, 5.92
cx10, cy10 = 5.33, 6.37
cx11, cy11 = 5.37, 6.73
cx12, cy12 = 5.43, 7.11
cx13, cy13 = 5.51, 7.50
cx14, cy14 = 5.62, 7.89
cx15, cy15 = 5.76, 8.28
cx16, cy16 = 5.93, 8.68
cx17, cy17 = 6.17, 9.08
cx18, cy18 = 6.50, 9.47
cx19, cy19 = 6.74, 9.67
cx20, cy20 = 7.05, 9.89
cx21, cy21 = 7.46, 10.14

xcp1=math.ceil(xp1*p)
xcp2=math.ceil(xp2*p)


ycp1=math.ceil(yp1*p)
ycp2=math.ceil(yp2*p)



c1=math.ceil(h*p)
c2=math.ceil(b*p)


ccx1=math.ceil(cx1*p)
ccx2=math.ceil(cx2*p)
ccx3=math.ceil(cx3*p)
ccx4=math.ceil(cx4*p)
ccx5=math.ceil(cx5*p)
ccx6=math.ceil(cx6*p)
ccx7=math.ceil(cx7*p)
ccx8=math.ceil(cx8*p)
ccx9=math.ceil(cx9*p)
ccx10=math.ceil(cx10*p)
ccx11=math.ceil(cx11*p)
ccx12=math.ceil(cx12*p)
ccx13=math.ceil(cx13*p)
ccx14=math.ceil(cx14*p)
ccx15=math.ceil(cx15*p)
ccx16=math.ceil(cx16*p)
ccx17=math.ceil(cx17*p)
ccx18=math.ceil(cx18*p)
ccx19=math.ceil(cx19*p)
ccx20=math.ceil(cx20*p)
ccx21=math.ceil(cx21*p)



ccy1=math.ceil(cy1*p)
ccy2=math.ceil(cy2*p)
ccy3=math.ceil(cy3*p)
ccy4=math.ceil(cy4*p)
ccy5=math.ceil(cy5*p)
ccy6=math.ceil(cy6*p)
ccy7=math.ceil(cy7*p)
ccy8=math.ceil(cy8*p)
ccy9=math.ceil(cy9*p)
ccy10=math.ceil(cy10*p)
ccy11=math.ceil(cy11*p)
ccy12=math.ceil(cy12*p)
ccy13=math.ceil(cy13*p)
ccy14=math.ceil(cy14*p)
ccy15=math.ceil(cy15*p)
ccy16=math.ceil(cy16*p)
ccy17=math.ceil(cy17*p)
ccy18=math.ceil(cy18*p)
ccy19=math.ceil(cy19*p)
ccy20=math.ceil(cy20*p)
ccy21=math.ceil(cy21*p)



list1 = [(0,0),(xcp1, ycp1),(ccx1, ccy1),(ccx2, ccy2),(ccx3, ccy3),(ccx4, ccy4),(ccx5, ccy5),(ccx6, ccy6),(ccx7, ccy7),(ccx8, ccy8),(ccx9, ccy9)
,(ccx10, ccy10),(ccx11, ccy11),(ccx12, ccy12),(ccx13, ccy13),(ccx14, ccy14),(ccx15, ccy15),(ccx16, ccy16),(ccx17, ccy17),(ccx18, ccy18),(ccx19, ccy19),(ccx20, ccy20),(ccx21, ccy21),(c2,c1),(xcp2, ycp2),(0,0)]


# c1 = math.ceil(pixelsPerMetric * float(h))
# c2 = math.ceil(pixelsPerMetric * float(b))
# list1 = [(1610+0, 770+0),(1610+0 + c1, 770+0),(1610+0 + c1, 770+0 + c2),(1610+0, 770+c2)] 



#list1 = [(250+0,500+0),(250+0,500+c2),(250+c1,500+c2),(250+ccx6,500+ccy6),(250+ccx5,500+ccy5),(250+ccx4,500+ccy4),(250+ccx3,500+ccy3),(250+ccx2,500+ccy2),(250+ccx1,500+ccy1),(250+c3,500+0)]

# list1=[(950+c2,1520+ycp1),(950+xcp2,1520+ycp2),(950+ccx1,1520+ccy1),(950+ccx2,1520+ccy2),(950+ccx3,1520+ccy3),(950+ccx4,1520+ccy4),(950+ccx5,1520+ccy5),(950+ccx6,1520+ccy6),(950+ccx7,1520+ccy7),(950+ccx8,1520+ccy8),(950+ccx9,1520+ccy9),(950+ccx10,1520+ccy10),(950+ccx11,1520+ccy11),(950+ccx12,1520+ccy12),(950+ccx13,1520+ccy13),(950+ccx14,1520+ccy14),(950+ccx15,1520+ccy15),(950+ccx16,1520+ccy16)
#        ,(950+ccx17,1520+ccy17),(950+ccx18,1520+ccy18),(950+ccx19,1520+ccy19),(950+ccx20,1520+ccy20),(950+0,1520+c1),(950+c2,1520+c1)]
'''
panelPoints=[]
new_points=[]

#coordinates=Polygon([(c2,ycp1),(xcp2,ycp2),(ccx1,ccy1),(ccx2,ccy2),(ccx3,ccy3),(ccx4,ccy4),(ccx5,ccy5),(ccx6,ccy6),(ccx7,ccy7),(ccx8,ccy8),(ccx9,ccy9),(ccx10,ccy10),(ccx11,ccy11),(ccx12,ccy12),(ccx13,ccy13),(ccx14,ccy14),(ccx15,ccy15),(ccx16,ccy16)
#       ,(ccx17,ccy17),(ccx18,ccy18),(ccx19,ccy19),(ccx20,ccy20),(0,c1),(c2,c1)])

#list1=[(c2,ycp1),(xcp2,ycp2),(ccx1,ccy1),(ccx2,ccy2),(ccx3,ccy3),(ccx4,ccy4),(ccx5,ccy5),(ccx6,ccy6),(ccx7,ccy7),(ccx8,ccy8),(ccx9,ccy9),(ccx10,ccy10),(ccx11,ccy11),(ccx12,ccy12),(ccx13,ccy13),(ccx14,ccy14),(ccx15,ccy15),(ccx16,ccy16)
#       ,(ccx17,ccy17),(ccx18,ccy18),(ccx19,ccy19),(ccx20,ccy20),(0,c1),(c2,c1)]

#list1=[(184, 0), (40, 43), (47, 63), (54, 78), (60, 93), (65, 111), (68, 125), (72, 143),
#       (75, 163), (77, 175), (76, 187), (74, 199), (72, 213), (70, 224), (68, 234), (66, 246), (61, 257), (58, 265), (51, 278), (42, 288), (33, 295), (24, 301), (0, 311), (184, 311)]


Q1 = scale(coordinates, xfact = -1, origin = (1, 0))
panelPoints=(list((Q1.exterior.coords)))
panelPoints.reverse()
#print(panelPoints)




mav_val=0
for points in panelPoints:
    if points[0]<mav_val:
        mav_val=points[0]
    
for points in panelPoints:
    point_x=points[0]-mav_val
    point_y=points[1]
    new_points.append((point_x, point_y))
    
print('\n\n')
print(new_points)

'''




img=cv2.line(img, list1[0], list1[1], (0,255,0), 2)
img=cv2.line(img, list1[1], list1[2], (0,255,0), 2)
img=cv2.line(img, list1[2], list1[3], (0,255,0), 2)
img=cv2.line(img, list1[3], list1[4], (0,255,0), 2)

img=cv2.line(img, list1[4], list1[5], (0,255,0), 2)

img=cv2.line(img, list1[5], list1[6], (0,255,0), 2)
img=cv2.line(img, list1[6], list1[7], (0,255,0), 2)
img=cv2.line(img, list1[7], list1[8], (0,255,0), 2)
img=cv2.line(img, list1[8], list1[9], (0,255,0), 2)
img=cv2.line(img, list1[9], list1[10], (0,255,0), 2)
img=cv2.line(img, list1[10], list1[11], (0,255,0), 2)
img=cv2.line(img, list1[11], list1[12], (0,255,0), 2)
img=cv2.line(img, list1[12], list1[13], (0,255,0), 2)
img=cv2.line(img, list1[13], list1[14], (0,255,0), 2)
img=cv2.line(img, list1[14], list1[15], (0,255,0), 2)
img=cv2.line(img, list1[15], list1[16], (0,255,0), 2)
img=cv2.line(img, list1[16], list1[17], (0,255,0), 2)
img=cv2.line(img, list1[17], list1[18], (0,255,0), 2)
img=cv2.line(img, list1[18], list1[19], (0,255,0), 2)
img=cv2.line(img, list1[19], list1[20], (0,255,0), 2)
img=cv2.line(img, list1[20], list1[21], (0,255,0), 2)
img=cv2.line(img, list1[21], list1[22], (0,255,0), 2)
img=cv2.line(img, list1[22], list1[23], (0,255,0), 2)
img=cv2.line(img, list1[23], list1[24], (0,255,0), 2)
img=cv2.line(img, list1[24], list1[0], (0,255,0), 2)
'''
img=cv2.line(img, list1[25], list1[26], (0,255,0), 2)
img=cv2.line(img, list1[26], list1[27], (0,255,0), 2)
img=cv2.line(img, list1[27], list1[28], (0,255,0), 2)
img=cv2.line(img, list1[28], list1[29], (0,255,0), 2)
img=cv2.line(img, list1[29], list1[30], (0,255,0), 2)
img=cv2.line(img, list1[30], list1[31], (0,255,0), 2)
img=cv2.line(img, list1[31], list1[32], (0,255,0), 2)
img=cv2.line(img, list1[32], list1[33], (0,255,0), 2)
img=cv2.line(img, list1[33], list1[34], (0,255,0), 2)
img=cv2.line(img, list1[34], list1[35], (0,255,0), 2)
img=cv2.line(img, list1[35], list1[36], (0,255,0), 2)
img=cv2.line(img, list1[36], list1[37], (0,255,0), 2)
img=cv2.line(img, list1[37], list1[38], (0,255,0), 2)
img=cv2.line(img, list1[38], list1[39], (0,255,0), 2)
img=cv2.line(img, list1[39], list1[40], (0,255,0), 2)
img=cv2.line(img, list1[40], list1[41], (0,255,0), 2)
img=cv2.line(img, list1[41], list1[42], (0,255,0), 2)
img=cv2.line(img, list1[42], list1[43], (0,255,0), 2)
img=cv2.line(img, list1[43], list1[44], (0,255,0), 2)
img=cv2.line(img, list1[44], list1[45], (0,255,0), 2)
img=cv2.line(img, list1[45], list1[46], (0,255,0), 2)
img=cv2.line(img, list1[46], list1[47], (0,255,0), 2)
img=cv2.line(img, list1[47], list1[48], (0,255,0), 2)
img=cv2.line(img, list1[48], list1[49], (0,255,0), 2)
img=cv2.line(img, list1[49], list1[50], (0,255,0), 2)
img=cv2.line(img, list1[50], list1[51], (0,255,0), 2)
img=cv2.line(img, list1[51], list1[52], (0,255,0), 2)
img=cv2.line(img, list1[52], list1[53], (0,255,0), 2)
img=cv2.line(img, list1[53], list1[54], (0,255,0), 2)
img=cv2.line(img, list1[54], list1[0], (0,255,0), 2)
'''
cv2.imshow('no-coin-1.jpg', img)
k=cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
