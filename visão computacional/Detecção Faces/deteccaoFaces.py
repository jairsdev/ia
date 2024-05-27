import cv2

img = cv2.imread("workplace-1245776_1920.jpg")
"""cv2.imshow("imagem", img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
"""cv2.imshow("imagem cinza", imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

detections = detector.detectMultiScale(imgGray)
print(detections)

for x, y, w, h in detections:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0))

cv2.imshow("faces detectadas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()