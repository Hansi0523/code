# 無聊做做
import cv2
import numpy as np



def mouse_actitive(event, x, y, flag, param):
    if flag == cv2.EVENT_FLAG_LBUTTON:
        for x in range(0, 500, 5):
            for y in range(0, 500, 5):
                cv2.rectangle(image, (x, y), (x + 3, y + 3), (255, 255, 255), cv2.FILLED)


image = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow("title")
while True:
    cv2.setMouseCallback("title", mouse_actitive)
    cv2.imshow("title", image)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
