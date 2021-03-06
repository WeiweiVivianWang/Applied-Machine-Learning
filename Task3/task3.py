"""Created on Tue Feb  7 14:25:07 2017

@author: weiweiwang

"""

import numpy
#a = numpy.array([[1, 2], [3, 4]])



def compute(x,axis = 0):
    """Computes mean and standard deviation of a numpy-array dataset.
    
    This function computes the mean and standard deviation of a dataset along
    the specified axis.
    
    Parameters
    ----------

        x:   
            Numpy Array
            Dataset presented as a numpy array.
    
    
        axis: 
            None or int or tuple of ints, optional. Axis or axes along which the 
            means are computed. The default is to compute the mean of the flattened
            array.
        
    
    Returns
    --------
        type: Numpy array with mean and variance based on the axis selction.
    
    
    Examples
    --------
    >>> a = numpy.array([[1, 2], [3, 4]])
    >>> compute(a,None)
    (2.5, 1.1180339887498949)
    
    
    
    """
    if axis == 1:
        return numpy.mean(x,axis = 1),numpy.std(x,axis = 1)
    elif axis == None:
        return numpy.mean(x),numpy.std(x)
    else:
        return numpy.mean(x,axis = 0),numpy.std(x,axis = 0)
    
    


    