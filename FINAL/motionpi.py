from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2

vs = VideoStream(src=1).start()
time.sleep(2)
firstFrame = None
min_area = 500
while True:
    frame = vs.read()
    text = "Unoccupied"

    frame = imutils.resize(frame, width = 500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21),0)

    if firstFrame is None:
        firstFrame = gray
        continue

    frameDelta = cv2.absdiff(firstFrame,gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations = 2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)

    for x in cnts:
        if cv2.contourArea(x) < min_area:
            continue

        (x,y,w,h) = cv2.boundingRect(x)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"

    cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("Security Feed", frame)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Frame Delta", frameDelta)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
vs.stop()
cv2.destroyAllWindows()
