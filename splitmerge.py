import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#split
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red  = cv.merge([blank,blank,r]) 

cv.imshow('Blue', blue)
cv.imshow('Red', green)
cv.imshow('Green', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)
