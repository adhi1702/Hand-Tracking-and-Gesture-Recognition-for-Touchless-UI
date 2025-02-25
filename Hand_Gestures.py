import cv2
import time
import numpy as np
import pyautogui
from Hand_Tracker_Module import handDetector

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    screenWidth, screenHeight = pyautogui.size()
    smoothening = 5
    plocX, plocY = 0, 0
    clocX, clocY = 0, 0

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        
        if len(lmList) != 0:
            x1, y1 = lmList[8][1:] # Index finger tip
            x2, y2 = lmList[12][1:] # Middle finger tip

            fingers = detector.fingersUp()

            # Moving Mode: Only Index Finger is up
            if fingers[1] == 1 and fingers[2] == 0:
                x3 = np.interp(x1, (75, 640 - 75), (0, screenWidth))
                y3 = np.interp(y1, (75, 480 - 75), (0, screenHeight))

                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening

                pyautogui.moveTo(screenWidth - clocX, clocY)
                plocX, plocY = clocX, clocY

            # Clicking Mode: Index and Middle Fingers are up
            if fingers[1] == 1 and fingers[2] == 1:
                length, img, lineInfo = detector.findDistance(8, 12, img)
                if length < 40:
                    pyautogui.click()

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()