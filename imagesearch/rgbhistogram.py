# Author: Rahul Remanan
# Date: 20 June 2017
# Website: http://jomiraki.com/

# Import package dependencies
import numpy as np
import cv2

class RGBHistogram:
	def __init__(self, bins):
		# Number of bins for the histogram.
		self.bins = bins

	def describe(self, image):
		# Compute a 3D histogram in the RGB colorspace and normalize.
		hist = cv2.calcHist([image], [0, 1, 2],
			None, self.bins, [0, 256, 0, 256, 0, 256])
		hist = cv2.normalize(hist, hist)

		# Return the 3D histogram output as a flattened array.
		return hist.flatten()