import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import sklearn

def test():
    X, y = make_blobs(n_samples=100, n_features=4, centers=2, cluster_std=3)
    x_Train, x_Test, y_Train, y_Test = train_test_split(X, y, test_size=0.2)
    KNN = KNeighborsClassifier()  
    KNN.fit(x_Train, y_Train)  
    Prediction = KNN.predict(x_Test)   
    print(Prediction)
    print(KNN.score(x_Test, y_Test))

class copy_KNN():
    def __init__(self, n_neighbors=5, Weights="uniform", Algorithm="Auto", leaf_size=30, p=2, metric=None, n_jobs=None):
        self.Neighbors=n_neighbors
        self.Weights=Weights
        self.Algorithm=Algorithm
        self.leaf_size=leaf_size
        self.p=p
        self.metric=metric

print(sklearn.__path__)


