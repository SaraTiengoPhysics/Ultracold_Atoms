import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#here I define all the functions


# load_image: function which loads image file and returns content as a
# matrix / array (numpy array). The resulting data is the ratio of the 
# intensity with atoms divided by the intensity without atoms:
# imageData(x,y)=I(x,y)/I_0(x,y)
def load_image(filename, size_x, size_y):
    with open(filename, 'rb') as fid:
        imageData = np.fromfile(fid, np.float32).reshape(size_x, size_y).T
        return imageData

#column_density: function which calculate the column density for each
#pixel of the image
#RETURN: a 2D matrix with column density values 
def column_density(data,cross_section):
    dim = np.shape(data) #image dimensions 
    n = np.zeros((dim[0],dim[1]))  #initialize column density matrix 
    n = - np.log(data) * 1/cross_section
    return n
    
#non-linear fit function-GAUSSIAN
#parameters: offset, n0=centre column density, x0, sigma_x
def gauss(x,offset, n0, x0,sigma_x):
    return offset + n0*np.exp(-(x-x0)**2/(2*sigma_x**2))

#non-linear fit function-PARABOLA
#parameters: a=g, b=v0, c=x0
def parabola(x,a,b,c):
    return (1/2)*a*x**2 + b*x +c

#non-linear fit function-GAUSSIAN 2D
#parameters: offset, n0=centre column density, x0, y0, sigma_x, sigma_y
def twoD_Gaussian(X,  offset, n0, xo, yo, sigma_x, sigma_y):
    (x,y) = X
    a = 1/(2*sigma_x**2)
    b = 1/(2*sigma_y**2)
    g = offset + n0*np.exp( - (a*((x-xo)**2) + b*((y-yo)**2)))
    return g.ravel()
