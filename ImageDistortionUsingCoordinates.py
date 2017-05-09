import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = cv2.imread(str(sys.argv[1]))
rows,cols,ch = img.shape
oldCoordinate = [
			[int(sys.argv[2]),int(sys.argv[3])],
			[int(sys.argv[4]),int(sys.argv[5])],
			[int(sys.argv[6]),int(sys.argv[7])],
			[int(sys.argv[8]),int(sys.argv[9])]
		]

newCoordinate = [
			[int(sys.argv[10]),int(sys.argv[11])],
			[int(sys.argv[12]),int(sys.argv[13])],
			[int(sys.argv[14]),int(sys.argv[14])],
			[int(sys.argv[16]),int(sys.argv[15])]
		]

pts1 = np.float32(oldCoordinate)
pts2 = np.float32(newCoordinate)

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(5000,5000))

Image.fromarray(dst).save("distorted_picture.png")

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(dst),plt.title('Distorted')
plt.show()
