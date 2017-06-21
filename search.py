# Author: Rahul Remanan
# Date: 20 June 2017
# Website: http://jomiraki.com/

# USAGE
# python/python3 search.py --dataset images --index index.cpickle

# Import package dependencies
from imagesearch.searcher import Searcher
import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
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
args = vars(ap.parse_args())

index = args["index"]
# Load search index and perform image search.
with open(index, 'rb') as f:
  pickle_file = f.read()
index = cPickle.loads(pickle_file)
searcher = Searcher(index)

# Test loop
for (query, queryFeatures) in index.items():
	# Perform the search using the current query.
    results = searcher.search(queryFeatures)
	# Load the query image and display it.
    path = args["dataset"] + "/%s" % (query)
    queryImage = cv2.imread(path)
    plt.imshow(queryImage)
    plt.xticks([]), plt.yticks([]) # Hide the tick values on X and Y axis.
    plt.show()
    print ("query: %s" % (query))
           

	# Initialize the two montages to display the search results.
	# Display the top 10 results with 5 images per output.
	# Images size: YxX pixels
    X = 400
    Y = 400
    montageA = np.zeros((X * 5, Y, 3), dtype = "uint8") # X = 400, Y =400
    montageB = np.zeros((X * 5, Y, 3), dtype = "uint8")

	# Loop over the top ten results.
    for j in range(0, 10):
		# grab the result using row-major order and load the result image
        (score, imageName) = results[j]
        path = args["dataset"] + "/%s" % (imageName)
        result = cv2.imread(path)
        print ("\t%d. %s : %.3f" % (j + 1, imageName, score))

		# check to see if the first montage should be used
        if j < 5:
            montageA[j * X:(j + 1) * X, :] = result

		# otherwise, the second montage should be used
        else:
            montageB[(j - 5) * X:((j - 5) + 1) * X, :] = result

# Display search results.    
plt.imshow(montageA)
plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(montageB)
plt.xticks([]), plt.yticks([])
plt.show()