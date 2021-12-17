import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit   # as an example for importing curve_fit function

# First: Define functions
#
# load_image: function which loads image file and returns content as a
# matrix / array (numpy array). The resulting data is the ratio of the 
# intensity with atoms divided by the intensity without atoms:
# imageData(x,y)=I(x,y)/I_0(x,y)

def load_image(filename, size_x, size_y):
    with open(filename, 'rb') as fid:
        imageData = np.fromfile(fid, np.float32).reshape(size_x, size_y).T
        return imageData

# Define parameters
myfilename='A_Thermal_5.bin'
resolution_x=300   # number of pixels in x direction
resolution_y=1000  # number of pixels in y direction

# Now load the data from one image
data = load_image(myfilename,resolution_x,resolution_y)

# output the picture on the screen
plt.imshow(data)
plt.show()

# Now you can do fitting. For 1D / 2D fitting in python, a typical function 
# that people use is curve_fit() from the scipy package (see import section, above)
