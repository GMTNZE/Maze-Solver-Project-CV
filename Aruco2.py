import cv2
import numpy as np



vid = cv2.VideoCapture(0)
while (True):
    ret, frame= vid.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dictionary = cv2.aruco.Dictionary(cv2.aruco.DICT_4X4_250, 28)
    parameters = cv2.aruco.DetectorParameters()
    markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)
    for corner in markerCorners:
        centerX = (corner[0][0][0] + corner[0][1][0] + corner[0][2][0] + corner[0][3][0]) / 4
        centerY = (corner[0][0][1] + corner[0][1][1] + corner[0][2][1] + corner[0][3][1]) / 4
        center = (int(centerX), int(centerY))
        cv2.circle(frame, center, 3, 255, -1)
    if markerCorners:
        for ids, corners in zip(markerIds, markerCorners):
            cv2.polylines(
                frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv2.LINE_AA
            )
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            top_left = corners[1].ravel()
            bottom_right = corners[2].ravel()
            bottom_left = corners[3].ravel()
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
vid.release()
cv2.destroyAllWindows()

    