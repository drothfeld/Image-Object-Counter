# Dylan Rothfeld 09/29/2017
# Requires scikit-image installed to run
# For OSX use the command: "pip install scikit-image --user"

# Imports
from skimage import io, filters, measure
from scipy import ndimage
import matplotlib.pyplot as plt
import logging
import sys

# Checking Script Arguments
displayImage = False
filename = sys.argv[-1]
if len(sys.argv) == 3:
    if sys.argv[1] == '-d':
        displayImage = True
    # Invalid parameter entered
    else:
        logging.error(' | Invalid parameter used: ' + sys.argv[1])
        quit()

if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
    # Running Image Analysis
    logging.info(' | Image file successfully read.\n')
    im = io.imread(filename, as_grey=True)
    val = filters.threshold_otsu(im)
    drops = ndimage.binary_fill_holes(im < val)
    if displayImage:
        plt.imshow(drops, cmap='gray')
        plt.show()
else:
    logging.error(' | No correct image file was specified of type: .png .jpg .jpeg\n')
