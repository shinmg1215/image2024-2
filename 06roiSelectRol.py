#x,y,w,h = cv2.selectROI('img',img, False)
import cv2


def onMouse(event, x, y, flags, param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("lbutton dwown")
        print(x,y)
        x0 =x, y0 = y
    elif(event == cv2.EVENT_MOUSEOVE):
        #print("mouse move")
        #print(x,y)
        xx = 1
    elif (event == cv2.EVENT_LBUTTONUP):
        print("lbutton up")
        print(x,y)
        x1 = x, y1 = y


    img = cv2.imread('./img/sunset.jpg')
    cv2.imshow('img', img)
    cv2.setMouseCallback('img',onMouse)
    cv2.waitKey()
    cv2.destroyAllWindows()
