# Image-search
A basic image search engine using python

A modified fork of : http://code.activestate.com/recipes/180801-convert-image-format/ and www.pyimagesearch.com/tag/lord-of-the-rings/.

The search engine image database currently only supports .png files of 400x400 pixel resolution.
Use the included image_converter.py to convert/batch process images of other formats to .png.

The search engine has two modules, an indexer and a search module. The search module is divided into a database validation module and an external image search module. Both the indexer and the search modules are tested in Python 2.7 and Python 3.6.

The image converter is tested only in Python 2.7.

Python dependencies:
 1) OpenCV
 
 2) Pillow
 
 3) Numpy, Scipy, Matplotlib

Usage instructions for indexer module:
 
 python/python3 index.py -d/--dataset images -i/--index index.cpickle
 
Usage instructions for search result validation module:
 
 python/python3 search.py --dataset images --index index.cpickle
 
Usage instruction for external search module:
 
 python/python3 search_external.py -d/--dataset -i/--index index.cpickle -q/--query query.png

Usage instructions for creating a custom image dataset:
 
 For applying this search engine to a custom image set, use a collection of 400x400 pixel .png images.
 
Additional extras:
 
 1) An included dataset of 42 images of world's most valuable paintings (https://en.wikipedia.org/wiki/List_of_most_expensive_paintings), resized to 400x400 px and converted to .png format.
 
 2) A pickle file with the pre-generated search index.

Developer environment: AMD64 Ubuntu Linux, version 17.04 (http://releases.ubuntu.com/17.04/).
