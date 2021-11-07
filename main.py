from MarkerBuild import *
from MarkerClass import *

# using default or only camera
cap = cv2.VideoCapture(0)

# physical marker length in mm
length = 66

while True:
    success, img = cap.read()
    height, width, _ = img.shape

    # detecting the marker and giving it an instance of the marker class
    corners, ids = ar_detector(img)
    marker = Marker(corners, ids)

    # calculate inches and write on cv2
    if marker.average_length != 0:
        inches = int(((1536 / marker.average_length) + 1.5) * (length / 66))
        cv2.putText(img, str(inches) + " in", (30, 55), cv2.QT_FONT_NORMAL, 1, (204, 209, 72), 2, cv2.LINE_AA)

        gap = int(marker.centroid[0] - (width / 2))
        cv2.putText(img, str(abs(gap)), (width - 35, height - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (204, 209, 72), 1,
                    cv2.LINE_AA)
        if gap > 0:
            cv2.putText(img, '>', (width - 25, height - 16), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (204, 209, 72), 1,
                        cv2.LINE_AA)
        elif gap < 0:
            cv2.putText(img, '<', (width - 25, height - 16), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (204, 209, 72), 1,
                        cv2.LINE_AA)

    cv2.imshow("Team 1493", img)
    cv2.waitKey(1)
