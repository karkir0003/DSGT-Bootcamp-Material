from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np


def get_iris_dataset():
    iris = datasets.load_iris()
    X, y = iris.data[:, [0, 1]], iris.target
    df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
    return df

def perform_train_test_split():
    df = get_iris_dataset()
    """
    Perform a train/test split. Return a tuple in the format (X_train, X_test, Y_train, Y_test)
    """
    #YOUR CODE HERE
    pass

def instantiate_models():
    """
    Fill in the blanks to instantiate the models using scikit learn. Return a tuple in the format:
    (SVM model, Decision Tree model, MLP model, KNN Model)
    
    Fill in the blanks as shown
    """
    #YOUR CODE HERE
    svm = ____
    dt = _____
    mlp = ______
    knn = ______
    return (svm, dt, mlp, knn)

def fit_models():
    """
    For each model from the instantiate_model() function, fit the models. 
    
    Fill in the blanks as ashown
    """
    svm, dt, mlp, knn = instantiate_models()
    X_train, X_test, Y_train, Y_test = perform_train_test_split()
    svm.____(_________)
    dt.____(__________)
    mlp.____(_________)
    knn.____(_________)
    return (svm, dt, mlp, knn) #return fitted models


def accuracy_at_least_90():
    """
    Choose a model from the instantiate_models function. Play around with the hyperparameters (eg: turning the dials and 
    knobs) from the instantiate_models() function and get the accuracy to at least 0.9.
    
    Recommended link to help you: https://scikit-learn.org/stable/supervised_learning.html
    
    The above link contains documentation to the scikit-learn library you are using
    
    Fill in the blanks
    
    Return format is tuple of the form (model, accuracy)
    """
    X_train, X_test, Y_train, Y_test = perform_train_test_split()
    
    svm, dt, mlp, knn = _______________
    
    model = ________ #put your chosen model here
    
    ______._____(__________) #once you pick a model, what do you need to do to train it?
    
    _____ = ______._____(______) #once you fit a model, how do you predict
    
    return ______________ #Return tuple format (model, accuracy). Look at sklearn.metrics to see how to calculate accuracy
    
    
    
