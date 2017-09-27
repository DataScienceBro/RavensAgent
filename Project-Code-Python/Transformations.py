import numpy as np

# set of transformation functions that return the confidence of said transformation


 # check to see if whole image is the same
identical = lambda imgA, imgB, threshold: np.count_nonzero(imgA - imgB) < threshold

# check to see if whole image is flipped vertically
vertFlip = lambda imgA, imgB, threshold: np.count_nonzero(imgA - np.flipud(imgB)) < threshold

# check to see if whole image is flipped horizontally
horizFlip = lambda imgA, imgB, threshold: np.count_nonzero(imgA - np.fliplr(imgB)) < threshold

# check to see if whole image is rotated 90deg
rot90 = lambda imgA, imgB, threshold: np.count_nonzero(imgA - np.rot90(imgB, k = 1)) < threshold

# check to see if whole image is rotated 180deg
rot180 = lambda imgA, imgB, threshold: np.count_nonzero(imgA - np.rot90(imgB, k = 2)) < threshold

# check to see if whole image is rotated 270deg
rot270 = lambda imgA, imgB, threshold: np.count_nonzero(imgA - np.rot90(imgB, k = 3)) < threshold


ruleFuncs = {'identical': identical, 'verFlip': vertFlip, 'horizFlip': horizFlip, 'rot90': rot90, 'rot180': rot180, 'rot270': rot270}