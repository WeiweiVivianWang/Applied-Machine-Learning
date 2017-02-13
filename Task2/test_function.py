import numpy
def div():
	return float(2)/float(8)

def numpydiv():
    return numpy.array(2,)/float(8)
#file = read('/Users/weiweiwang/Desktop/homework-i-WeiweiVivianWang/import.txt')

import io
import string
#chars = 0
#with io.open('/Users/weiweiwang/Desktop/homework-i-WeiweiVivianWang/input.txt','r',encoding = "UTF-8") as in_file:
#    for line in in_file:
#        chars += len(line.splitlines())
        
def count():
    
    word=0     
    data = io.open('input.txt', 'r', encoding = "UTF-8").read()
    for i in data.split():
        word += len(i)
        
    return word

def knnscore():
    

    from sklearn.model_selection import cross_val_score
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import datasets
    iris = datasets.load_iris()

    X = iris.data
    y = iris.target

    val_score = []
    neighbors = numpy.arange(1, 15, 2)
    for i in neighbors:
        knn = KNeighborsClassifier(n_neighbors = i)
        scores = cross_val_score(knn, X, y, cv = 5)
        val_score.append(numpy.mean(scores))
        best_n_neighbors = neighbors[numpy.argmax(val_score)]
        best_val_score = max(val_score)
        
    return best_val_score

        


def test_div():
	assert div()==0.25
           
def test_numpydiv():
    assert numpydiv()==0.25
                   
                   
def test_count():
    assert count()==6
                  
                   
def test_score():
    assert knnscore()>=0.7                  
