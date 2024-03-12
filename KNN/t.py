import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import sklearn


class EfficientKNN:
    def __init__(self, n_neighbors=5, weights="uniform", p=2):
        self.n_neighbors = n_neighbors
        self.weights = weights
        self.p = p

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        distances = self.minkowski_distance(X, self.X_train)
        # 获取最近邻的索引
        nearest_idx = np.argsort(distances, axis=1)[:, :self.n_neighbors]
        
        # 基于最近邻的索引计算预测
        predictions = np.array([np.bincount(self.y_train[nearest]).argmax() for nearest in nearest_idx])
        return predictions

    def minkowski_distance(self, X1, X2):
        # 计算 Minkowski 距离
        return np.sum((np.abs(X1[:, np.newaxis] - X2) ** self.p), axis=2) ** (1 / self.p)

    def score(self, X, y):
        # 计算准确率
        predictions = self.predict(X)
        return np.mean(predictions == y)

X, y = make_blobs(n_samples=10000, n_features=4, centers=3, cluster_std=5)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


K = EfficientKNN()
K.fit(X_train, y_train)
print(K.predict(X_test))