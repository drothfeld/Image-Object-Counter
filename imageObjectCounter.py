# Dylan Rothfeld 09/29/2017
# Requires scikit-image installed to run
# For OSX use the command: "pip install scikit-image --user"

# Imports
from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt

im = io.imread('test00.jpg', as_grey=True)
val = filters.threshold_otsu(im)
drops = ndimage.binary_fill_holes(im < val)
plt.imshow(drops, cmap='gray')
plt.show()
