# Python program to read image using OpenCV

# importing OpenCV(cv2) module
import cv2
import numpy as np 

# Save image in set directory
# Read RGB image
Template = cv2.imread('./img/ex1.png')
gray_image = cv2.cvtColor(Template, cv2.COLOR_BGR2GRAY) 
test_img = cv2.imread('./img/ex2.png')
test_gray = cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)


## Basic template,
THREE = gray_image[100:175,215:290]
SEVEN = gray_image[100:175,290:365]
SIX = gray_image[100:175,365:440]
FOUR = gray_image[100:175,440:515]
NINE = gray_image[100:175,590:665]
ONE = gray_image[100:175,740:815]
EIGHT = gray_image[100:175,965:1040]
FIVE = gray_image[100:175,1265:1340]
TWO = gray_image[175:250,815:890]

Templates = [ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]


# print(ONE[20:50,20:40])
# print(TWO[20:50,20:40])

def cos_similarity(v1,v2):
    # Cosine Similiarity 
    v1 = np.array(v1[25:50,25:50])
    v2 = np.array(v2[25:50,25:50])
    numerator = np.sum(v1 * v2)
    demoninator = np.sqrt(np.sum(v1**2) * np.sum(v2**2))
    return numerator / demoninator

def euclidean_similarity(v1,v2):
    v1 = np.array(v1[25:50,25:50])
    v2 = np.array(v2[25:50,25:50])
    return np.sqrt(np.sum((v1-v2)**2))

def manhattan_distance(v1,v2):
    v1 = np.array(v1[25:50,25:50])
    v2 = np.array(v2[25:50,25:50]) 
    return np.abs(np.sum(v1-v2))

def template_matching(img):
    """
    input : apple image
    output: matrix 
    Given image, extract the numbers on the apples and make it matrix 
    """
    mat = np.zeros((9,18))
    row_initial = 100 
    col_initial = 215 
    increment = 75 
    for i in range(9):
        for j in range(18):
            num = img[row_initial+increment*i:row_initial+increment*(i+1), col_initial+increment*j:col_initial+increment*(j+1)]
            temp = [] 
            for t in Templates:
                temp.append(euclidean_similarity(num,t))
            number = np.argmin(temp) + 1 
            mat[i,j] = number 
    return mat 




    