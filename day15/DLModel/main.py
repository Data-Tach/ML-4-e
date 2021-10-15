
import cv2

cap = cv2.VideoCapture("Roads - 1952.mp4")

# Object detection from stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=500)



while True:
    ret, frame = cap.read()
    height, width,_ = frame.shape

    # print(height,width)

    # Extract the field of intrest
    roi = frame[150:,320:]
    # print(roi)

    # Object dection
    mask = object_detector.apply(roi)
    _,mask = cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    
    countor, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in countor:
        # Calculate the area and eleminate small areas
        area = cv2.contourArea(cnt)
        if area > 100:
            # cv2.drawContours(roi,[cnt],-1,(0,255,0))
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),3)

    

    cv2.imshow("Roi",roi)
    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)


    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()