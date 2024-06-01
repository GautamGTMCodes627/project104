import cv2
img = cv2.imread("solar-system.jpg")

text_to_show = "Sun"
cv2.putText(img, text_to_show, (20, 220), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color=(0,0,0))

text_mercury = "Mercury"
cv2.putText(img, text_mercury, (110, 220), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.7, color=(0,0,180))

text_venus = "Venus"
cv2.putText(img, text_venus, (200, 220), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color=(0,0,255))

text_earth = "Earth"
cv2.putText(img, text_earth, (300, 220), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color=(0,0,255))

text_mars = "Mars"
cv2.putText(img, text_mars, (400, 220), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color=(0,0,255))

text_jupiter = "Jupiter"
cv2.putText(img, text_jupiter, (500, 220), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color=(0,0,255))

text_saturn = "Saturn"
cv2.putText(img, text_saturn, (770, 220), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color=(0,0,255))

text_uranus = "Uranus"
cv2.putText(img, text_uranus, (900, 220), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color=(0,0,255))

text_neptune = "Neptune"
cv2.putText(img, text_neptune, (1100, 220), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color=(0,0,255))

cv2.imshow("output", img)
cv2.waitKey(0)
