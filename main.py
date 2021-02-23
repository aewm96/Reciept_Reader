#Learning OpenCV with Tutorials

import numpy as np
import cv2
import Picture_display

#Tutorial 1

#Load a colour Image in grey scale
image_1 = cv2.imread('/Users/aidan/Desktop/Reciept_Example.png', 0)

#Display the Image
cv2.imshow('image', image_1)

cv2.waitKey(0)

cv2.destroyAllWindows()

#Tutorial 2
#creating shapes with OpenCV

# #Create a black image
# image_2 = np.zeros((512,512, 3), np.uint8)
#
# #Create a diagonal blue line with thickness of 5px
# image_2 = cv2.line(image_2, (0,0), (511,511),(255,0,0),5)
#
# #Draw a rectangle
# image_2 = cv2.rectangle(image_2,(384,0),(510,128),(0,255,0),3)
#
# #draw a circle
# image_2 - cv2.circle(image_2,(447,63),63,(0,0,255),-1)
#
# #Draw an ellipse
# image_2 = cv2.ellipse(image_2, (256,256),(100,50),0,0,180,255,-1)
#
# #Draw a polygon
# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# pts = pts.reshape((-1,1,2))
# image_2 = cv2.polylines(image_2, [pts],True, (0,255,255))
#
# #Write text onto the image
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(image_2, 'OpenCV', (10, 500), font, 4, (255, 255, 255),2, cv2.LINE_AA)
#
# cv2.imshow('image_2', image_2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Tutorial 3
#Use the mouse as a paint brush
    #SIMPLE VERSION

# mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x,y),100,(0,0,255),-1)
#
# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
#
# while(1):
#     cv2.imshow('image',img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()

# COMPLEX VERSION
# drawing = False #True if the mouse is pressed
# mode = True     #If True, draw rectangle. Press'm' to toggle curve
# ix,iy = -1, -1
#
# # Mouse Callback Function
# def draw_circle(event, x, y, flags, param):
#     global ix, iy, drawing,mode
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix, iy = x, y
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv2.rectangle(image_4, (ix, iy), (x,y), (0,255,0),-1)
#             else:
#                 cv2.circle(image_4,(x,y), 5, (0,0,255), -1)
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv2.rectangle(image_4, (ix, iy),(x,y),(0,255,0),-1)
#         else:
#             cv2.circle(image_4, (x,y), 5, (0,0,255),-1)
#
# image_4 = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)
#
# while(1):
#     cv2.imshow('image', image_4)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break
#
# cv2.destroyAllWindows()



#Tutorial 4
#Tutorial 5
#Tutorial 6
#Tutorial 7
#Tutorial 8
#Tutorial 9
#Tutorial 10
#Tutorial 11
#Tutorial 12
#Tutorial 13

