# Dylan Rothfeld 09/29/2017
# Requires scikit-image installed to run
# For OSX use the command: "pip install scikit-image --user"

# Imports
from skimage import io, filters, measure
from scipy import ndimage
import matplotlib.pyplot as plt
import logging
import sys

# Checking script arguments
displayImage = False
filename = sys.argv[-1]
if len(sys.argv) == 3:
    if sys.argv[1] == '-d':
        displayImage = True
    # Invalid parameter entered
    else:
        logging.error('Invalid parameter used: ' + sys.argv[1])
        quit()

if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
    # Running image analysis
    image = io.imread(filename, as_grey=True)
    value = filters.threshold_otsu(image)
    objects = ndimage.binary_fill_holes(image < value)
    labels = measure.label(objects)
    print('Image: %s' %(filename))
    print('Objects: %f' %(labels.max()))
    print('Coverage: %f' %(objects.mean()))
    # Showing image
    if displayImage:
        plt.imshow(objects, cmap='gray')
        plt.show()
else:
    logging.error('No correct image file was specified of type: .png .jpg .jpeg')
