import cv2

img = cv2.imread("pessoas.jpg")
detecter = cv2.CascadeClassifier("fullbody.xml")
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

detection = detecter.detectMultiScale(imgGray, 1.002, minSize=(60, 60), maxSize=(1000, 200))
print(detection)

for x, y, w, h in detection:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0))

cv2.imshow("imagem detecção", img)
cv2.waitKey(0)
cv2.destroyAllWindows()