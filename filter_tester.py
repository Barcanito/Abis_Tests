from operator import truediv

import cv2
import numpy as np

# Load the image
cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	filter_index = 31
	#apply MedianBlur to reduce noise
	median_blurred = cv2.medianBlur(img, filter_index)
	gaussian_blurred = cv2.GaussianBlur(img, (filter_index,filter_index), 0)



	cv2.imshow('Original', img)
	cv2.imshow('Median Blurred', median_blurred)
	cv2.imshow('Gaussian Blurred', gaussian_blurred)

	# Wait for the user to press 'ESC' to exit
	if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the 'ESC' key
		break
cv2.waitKey(0)
cv2.destroyAllWindows()
