# Author: Rahul Remanan
# Date: 20 June 2017
# Website: http://jomiraki.com/

# Import package dependencies
import numpy as np

class Searcher:
	def __init__(self, index):
		# Store the search index.
		self.index = index

	def search(self, queryFeatures):
		# Initialize dictionary of results.
		results = {}

		# Loop over the index.
		for (k, features) in self.index.items():
			# compute the chi-squared distance between the features in index and query.
			# chi-squared distance is normally used to compare histograms in computer vision.
			d = self.chi2_distance(features, queryFeatures)

			# now that we have the distance between the two feature
			# vectors, we can udpate the results dictionary -- the
			# key is the current image ID in the index and the
			# value is the distance we just computed, representing
			# how 'similar' the image in the index is to our query
			results[k] = d

		# Sort results, so that smaller distances (more relevant images) are at the front of the list.
		results = sorted([(v, k) for (k, v) in results.items()])

		# Return the results.
		return results

	def chi2_distance(self, histA, histB, eps = 1e-10):
		# Compute the chi-squared distance.
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])

		# Return the chi-squared distance.
		return d