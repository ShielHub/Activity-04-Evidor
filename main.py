import cv2

title1 = 'fixed'
fixedfp = 'angry bird.jpg'
image1 = cv2.imread(fixedfp, 1)

title2 = 'Input'
x = input("Enter a file path: ")
y = int(input("Enter a flag (1/0/-1): "))
image2 = cv2.imread(x, y)

cv2.imshow(title1, image1)
cv2.imshow(title2, image2)
cv2.waitKey(0)
cv2.destroyAllWindows()