import numpy as np
import cv2

### Bozuk Para tanımlama programı için 25 cm kalibrasyon ayarı yapılmıştır.

cap = cv2.VideoCapture(0) # webcam için 1

while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
        
    circles = cv2.HoughCircles(gray_blur,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)
    
    if(circles is not None):
        circles = np.uint16(np.around(circles))
        change = 0
        for i in circles[0,:]:
                cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                cv2.circle(frame, (i[0], i[1]),2, (0,0,255), 3)
                radius = i[2]
                area = round(3.14*(radius**2))
                
                if(area >= 4500):
                    change = change + 1
                elif((area >= 3610) and (area < 4440)):
                    change = change + 0.5
                elif((area >= 2600) and (area < 3580)):
                    change = change + 0.25
                elif((area >= 2200) and (area< 2580)):
                    change = change + 0.10
                elif((area >= 1810) and (area< 2200)):
                    change = change + 0.05
                elif((area >= 1810) and (area< 1200)):
                    change = change + 0.01
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Total value: " + str("%.2f" % round(change,2)) + " TL "
        cv2.putText(frame, text, (0,400), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('Coin Detection',frame)
    cv2.waitKey(1)


cap.release()
cv2.destroyAllWindows()

