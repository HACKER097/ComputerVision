# import the necessary packages
import cv2
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show some basic information on it
image = cv2.imread("new.jpeg")
print(f'Width: {image.shape[1]} pixels')
print(f'Height: {image.shape[0]} pixels')
print(f'Channels: {image.shape[1]}')

# show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

# save the image -- OpenCV handles converting file types automatically
cv2.imwrite("newimage.jpg", image)
