import cv2

cascade = 'cars.xml'
video = 'video1.avi'

cap = cv2.VideoCapture(video)
car_cascade = cv2.CascadeClassifier(cascade)

while True:
	_,frame = cap.read()
	if type(frame) == type(None):
		break

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cars = car_cascade.detectMultiScale(frame,1.3,1)

	for (x,y,w,h) in cars:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)

	cv2.imshow('video', frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		break
cv2.destroyAllWindows()