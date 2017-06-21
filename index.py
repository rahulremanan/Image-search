# Author: Rahul Remanan
# Date: 20 June 2017
# Website: http://jomiraki.com/

# USAGE
# python/python3 index.py -d/--dataset images -i/--index index.cpickle

# Import package dependencies
from imagesearch.rgbhistogram import RGBHistogram
import argparse
import glob
import cv2
try:
    # for Python2
    import cPickle
except ImportError:
    # for Python3
    import _pickle as cPickle

# Construct the argument parser and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

# Initialize the index dictionary to store the images. 
# The 'key' of the dictionary is the image filename and the 'value' is the computed features.
index = {}

# Initialize image descriptor by creating a 3D RGB histogram with 8 bins per channel.
desc = RGBHistogram([8, 8, 8])

# Use glob to grab the image paths and loop over them.
for imagePath in glob.glob(args["dataset"] + "/*.png"):
	# Extract our unique image ID (i.e. the filename)
    k = imagePath[imagePath.rfind("/") + 1:]

	# Load the image, describe it using RGB histogram and update the index.
    image = cv2.imread(imagePath)
    X = 400
    Y = 400
    resized_image = cv2.resize(image, (X, Y)) # Image size of YxX 
    features = desc.describe(resized_image)
    index[k] = features
    
# Image indexing and write index to disk.
f = open(args["index"], "wb")
f.write(cPickle.dumps(index, protocol=2))
f.close()

# Display index size.
print ("done...indexed %d images" % (len(index)))