import cv2

img = cv2.imread('/home/silvia/PycharmProjects/alex_video/roi.png')

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binario = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)

desfoque = cv2.GaussianBlur(binario, (5, 5), 0)
cv2.imshow('teste', desfoque)


cv2.waitKey(0)
cv2.destroyAllWindows()