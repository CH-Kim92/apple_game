# Python program to read image using OpenCV

# importing OpenCV(cv2) module
import cv2
from matching import template_matching

# Save image in set directory
# Read RGB image
img = cv2.imread('./img/ex1.png')
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
apple_matrix = template_matching(gray_image)

print(apple_matrix)