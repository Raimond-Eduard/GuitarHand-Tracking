import cv2
import numpy as np
'''
img = cv2.imread('TestImage.jpg')
original = img
allLines = img
cv2.imshow('Original', img)
cv2.waitKey(0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', img)
cv2.waitKey(0)
img = cv2.Canny(img, 50, 150, apertureSize=3)
cv2.imshow('Canny', img)
cv2.waitKey(0)
img = cv2.Sobel(img, cv2.CV_8UC1, 2, 0)
cv2.imshow('Sobel', img)
cv2.waitKey(0)

lines = cv2.HoughLinesP(img, 1, np.pi/180, threshold=100, minLineLength=10, maxLineGap=10)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(allLines, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('All lines', allLines)
cv2.waitKey(0)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        # Calculate the slope of the line
        slope = (y2 - y1) / (x2 - x1 + 1e-6)  # Add a small value to avoid division by zero
        # Filter lines with slope within a threshold (considered vertical)
        if abs(slope) > 0.5:  # Adjust the threshold as needed
            cv2.line(original, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('Finish', original)
cv2.waitKey(0)
'''

image = cv2.imread('TestImage.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise, if necessary
gray_blurred = cv2.Canny(gray,50, 150, apertureSize=3)

# Use Hough Circle Transform to detect circles
circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                           param1=200, param2=30, minRadius=1, maxRadius=0)

# If circles are detected, draw them on the original image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        # Draw the circle outline
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        # Draw the center of the circle
        cv2.circle(image, (x, y), 2, (0, 0, 255), 3)

# Display the result
cv2.imshow('Detected Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()