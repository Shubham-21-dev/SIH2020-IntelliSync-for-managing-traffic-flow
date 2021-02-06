import cv2
import datetime
cap=cv2.VideoCapture("mydataset.mp4")

#Reading two consecutive frames using cap instance

ret,frame1=cap.read()
ret,frame2=cap.read()

#checking if the video is opened using cap instance
while cap.isOpened():
    diff=cv2.absdiff(frame1,frame2)
    # It gives pixel difference of first frame to second frame
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    # converting color from RGB to GRAY
    blur=cv2.GaussianBlur(gray,(5,5),0)
    #removing the noise present on image
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    #defining a thresholding value and applying Binary thresholding
    dilated=cv2.dilate(thresh,None,iterations=3)
    #filling the holes
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    c=0
    for countour in contours:
        (x,y,w,h)=cv2.boundingRect(countour)
        if cv2.contourArea(countour)<300:
            continue
        c=int(c+1)
        if(c<=5):
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 255), 2)
    st="Density: "+str(len(contours))
    s="Density: "+str(c)
    datet=str(datetime.datetime.now())
    #taking current date and time using datetime liabrary
    cv2.putText(frame1,datet,(100,300),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
    #Displaying date and time on window
    cv2.putText(frame1,s,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),3)

    #cv2.drawContours(frame1,contour,-1,(0,255,0),2)
    cv2.imshow("feed",frame1)
    frame1=frame2
    ret,frame2 =cap.read()
    if cv2.waitKey(40)==27:
        break
cv2.destroyAllWindows()
cap.release()
