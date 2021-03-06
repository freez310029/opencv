import cv2

def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # cv2.circle(img,(x,y),100,(255,0,0),5)
        cv2.rectangle(img,(x,y),(x+100,y+100),(0,255,0),5)
#Import only if not previously imported
img = cv2.imread("./test.jpg")     #(flag = 0 or 1 or -1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)

while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(20) == 27:
        break
cv2.destroyAllWindows()