"""
import cv2
image = cv2.imread("/Users/nasa/downloads/folder/OpenCv/pika.png")

start_point = (0,0)
end_point = (250,250)
color = (0,255,0)
thickness = 9

lined_image = cv2.line(image,start_point,end_point,color,thickness)

cv2.imshow("Pika with line", lined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
image = cv2.imread("/Users/nasa/downloads/folder/OpenCv/pika.png")

start_point = (20,20)
end_point = (250,250)
color = (255,0,0)
thickness = 2

rect_image = cv2.rectangle(image,start_point,end_point,color,thickness)

cv2.imshow("Pika with rectangle", rect_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
image = cv2.imread("/Users/nasa/downloads/folder/OpenCv/pika.png",0)

start_point = (100,50)
end_point = (125,80)
color = (0,0,0)
thickness = -1

black_image = cv2.rectangle(image,start_point,end_point,color,thickness)

cv2.imshow("Pika with black_rect", black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
image = cv2.imread("/Users/nasa/downloads/folder/OpenCv/pika.png")

center_coords = (120,50)
r = 20
color = (255,0,0)
thickness = 2

circle_image = cv2.circle(image,center_coords,r,color,thickness)

cv2.imshow("Pika with circle", circle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
import cv2
image = cv2.imread("/Users/nasa/downloads/folder/OpenCv/pika.png")

center_coords = (120,100)
r = 30
color = (0,0,255)
thickness = -1

circle_image = cv2.circle(image,center_coords,r,color,thickness)

cv2.imshow("Pika with circle", circle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
