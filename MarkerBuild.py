import cv2
import cv2.aruco as aruco


def ar_detector(img, draw=True):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    aruco_param = aruco.DetectorParameters_create()
    corners, ids, rejected = aruco.detectMarkers(gray_image, aruco_dict, parameters=aruco_param)

    # draw the border and id on the marker
    if draw:
        aruco.drawDetectedMarkers(img, corners, ids)
    return corners, ids


### corners and ids examples ###
""" 
corners = [array([[[510., 150.],
                   [578., 150.],
                   [576., 214.],
                   [508., 213.]]], dtype=float32), 
           array([[[440., 147.],
                   [505., 146.],
                   [504., 211.],
                   [439., 210.]]], dtype=float32)] ~ gives corner values of the squares
        
ids = [[9] [0]] ~ two ids (0 and 9) detected
"""
