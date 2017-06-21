# Author: Rahul Remanan
# Date: 20 June 2017
# Website: http://jomiraki.com/

# USAGE
# python/python3 search_external.py -d/--dataset -i/--index index.cpickle -q/--query query.png

# Import package dependencies
from imagesearch.rgbhistogram import RGBHistogram
from imagesearch.searcher import Searcher
import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import os
try:
    # Python2
    import cPickle
except ImportError:
    # Python3
    import _pickle as cPickle

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images we just indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where we stored our index")
ap.add_argument("-q", "--query", required = True,
	help = "Path to query image")
args = vars(ap.parse_args())

query = args["query"]

if os.path.isfile(query):
    queryImage = cv2.imread(query)
    plt.imshow(cv2.cvtColor(queryImage, cv2.COLOR_BGR2RGB))
    plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
    plt.show()
    print ("query: %s" % (args["query"]))
else:
    print("The specified file does not exist")
    
# describe the query in the same way that we did in
# index.py -- a 3D RGB histogram with 8 bins per
# channel

desc = RGBHistogram([8, 8, 8])
queryFeatures = desc.describe(queryImage)

index = args["index"]
# Load the index perform the search.
with open(index, 'rb') as f:
  pickle_file = f.read()
index = cPickle.loads(pickle_file)
searcher = Searcher(index)
results = searcher.search(queryFeatures)

# Initialize the two montages to display search results --
# Images size: YxX pixels
X = 400
Y = 400
montageA = np.zeros((X * 5, Y, 3), dtype = "uint8") # x=400, y=400
montageB = np.zeros((X * 5, Y, 3), dtype = "uint8")

# Loop over the top ten results
for j in range(0, 10):
	# grab the result (we are using row-major order) and
	# load the result image
	(score, imageName) = results[j]
	path = args["dataset"] + "/%s" % (imageName)
	result = cv2.imread(path)
	print ("\t%d. %s : %.3f" % (j + 1, imageName, score))

	# check to see if the first montage should be used
	if j < 5:
		montageA[j * X:(j + 1) * X, :] = result

	# otherwise, the second montage should be used
	else:
		montageB[(j - 5) * X:((j - 5) + 1) * X, :] = result # x =400

# Disply search results.
plt.imshow(montageA)
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(montageB)
plt.xticks([]), plt.yticks([])
plt.show()