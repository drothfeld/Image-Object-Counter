# Dylan Rothfeld 09/29/2017
# Requires scikit-image installed to run
# For OSX use the command: "pip install scikit-image --user"

# Imports
from skimage import io, filters, measure
from scipy import ndimage
import matplotlib.pyplot as plt
import logging, time, sys

# Default values
logging.getLogger().setLevel(logging.INFO)
start_time = time.time()
displayImage = False
filename = sys.argv[-1]
ignoreFiles = ["imageObjectCounter.py", "runObjectCounter.sh", "object_counter_data.txt", "README.md"]

# Checking script arguments
if filename in ignoreFiles:
    quit()
if len(sys.argv) == 3:
    if sys.argv[1] == '-d':
        displayImage = True
    # Invalid parameter entered
    else:
        logging.error('Invalid parameter used: %s' %(sys.argv[1]))
        quit()

if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
    # Running image analysis
    image = io.imread(filename, as_grey=True)
    value = filters.threshold_otsu(image)
    objects = ndimage.binary_fill_holes(image < value)
    labels = measure.label(objects)
    # Writing to file
    runtime = time.time() - start_time
    with open('object_counter_data.txt', 'a') as output:
        output.write('Filename: %s | ' %(filename))
        output.write('Objects: %d | ' %(labels.max()))
        output.write('Coverage: %f | ' %(objects.mean()))
        output.write('Runtime: %f\n' %(runtime))
    logging.info('FILE:(%s) successfully finished in %f seconds'%(filename, runtime))
    # Showing image
    if displayImage:
        plt.imshow(objects, cmap='gray')
        plt.show()
else:
    logging.error('FILE:(%s) is not a valid file of type: .png .jpg .jpeg' %(filename))
