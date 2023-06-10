# import the necessary packages
# user created library "imutils" contains a handful of “convenience” methods to more easily
# perform common tasks like translation, rotation, and resizing (and with less code).
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# NOTE: Translating (shifting) an image is given by a NumPy matrix in the form:
# [[1, 0, shiftX], [0, 1, shiftY]]
# You simply need to specify how many pixels you want to shift the image in the X and Y
# let's translate the image 25 pixels to the right and 50 pixels down
# Now that we have our translation matrix defined, the actual translation takes place using the
# cv2.warpAffine function. The first argument is the image we wish to shift and the second
# argument is our translation matrix M. Finally, we manually supply the dimensions (width and
# height) of our image as the third argument.
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)

# now, let's shift the image 50 pixels to the left and 90 pixels up, we
# accomplish this using negative values
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
