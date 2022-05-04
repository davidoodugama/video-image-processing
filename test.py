import cv2
import numpy as np
import easyocr

def nothing(x):
    pass

#cap = cv2.VideoCapture(0)
# cv2.namedWindow("Trackbars")

# cv2.createTrackbar("L – H", "Trackbars", 0, 179, nothing)
# cv2.createTrackbar("L – S", "Trackbars", 0, 255, nothing)
# cv2.createTrackbar("L – V", "Trackbars", 0, 255, nothing)
# cv2.createTrackbar("U – H", "Trackbars", 179, 179, nothing)
# cv2.createTrackbar("U – S", "Trackbars", 255, 255, nothing)
# cv2.createTrackbar("U – V", "Trackbars", 255, 255, nothing)

while True:
    #_, frame = cap.read()
    img = cv2.imread("image.jpg")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#     l_h = cv2.getTrackbarPos("L – H", "Trackbars")
#     l_s = cv2.getTrackbarPos("L – S", "Trackbars")
#     l_v = cv2.getTrackbarPos("L – V", "Trackbars")
#     u_h = cv2.getTrackbarPos("U – H", "Trackbars")
#     u_s = cv2.getTrackbarPos("U – S", "Trackbars")
#     u_v = cv2.getTrackbarPos("U – V", "Trackbars")

    lower_blue = np.array([0, 0, 0])
    upper_blue = np.array([179,255,204])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    

#     result = cv2.bitwise_and(img, img, mask=mask)

#     cv2.imshow("img", img)
    cv2.imshow("mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()