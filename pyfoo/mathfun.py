import numpy as np

def scale(x):
    """ Centers the vector by subtracting it's mean and scales by the standart error
    :param x: numeric vector
    :type x: numpy.array or list of numbers

    :returns: scaled vector of the same length with zero mean and deviation equal to 1
    :rtype: numpy.array
    """
    return (x - np.mean(x)) / np.std(x)
