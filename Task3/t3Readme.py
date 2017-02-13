==================================
Calculating an average of an array
==================================
Overview 
-------- 



In this function, we will input a numpy array as well as an “axis” argument. The objective of the function is to take an average along an axis: rows, columns, or the entire matrix. If 0 is the axis, then the function will return the average of rows. If 1 is the axis, the function will return the average of columns. If “None” is the input, the mean of all entries of the matrix is returned.

To illustrate how this function works by example, suppose we input a 2d-numpy array:



.. math::

	array=\begin{bmatrix}
	1&2&3\\
	3&4&5\\
	5&6&7\\
	\end{bmatrix}


If the input is 0, then the function will return the average of each row. For example, for the first row, if there are c columns, it will compute the summation of row 1 is 6 and will return the mean of row 1 is 2.

It will repeat this for each row and eventually return an array, of values for each row:

.. math::

	array=\begin{bmatrix}
	2\\
	4\\
	6\\
	\end{bmatrix}
If the input is 1, then the function will return the average of each column, with the same formula, except summing over the columns instead of rows and returning the respective standard deviations.

If the input is “None”, then the output will be a scalar that is the average of the entire matrix.
