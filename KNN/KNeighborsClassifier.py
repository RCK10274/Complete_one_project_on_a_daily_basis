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

class KNN_classifier():
    def __init__(self, n_neighbors=5, Weights="uniform", Algorithm="Auto", leaf_size=30, p=2, metric=None, n_jobs=None):
        
        self.Neighbors=n_neighbors #鄰近值
        self.Weights=Weights #權重, 預設"uniform"為權重相等, 'distance'對較近鄰加大權重, 較遠鄰反之
        self.Algorithm=Algorithm #演算法, 有{'auto', 'ball_tree', 'kd_tree', 'brute'}選項, 預設"auto"
        self.leaf_size=leaf_size #數據結構(樹)構成的速度, 引響樹的建構與資料的查詢
        self.p=p #距離度量的方式, 預設為2(歐基里德距離), 1為(曼哈頓距離)
        self.metric=metric #距離算法預設'minkowski', 可替換其他自製的funtion
        self.n_jobs=n_jobs #預設None, 意味單核心執行, -1為使用所有可用處理器, 並行計算只適用於查找相鄰點的任務

    def fit(self, X, y):#訓練資料
        """
        X:訓練資料
        y:答案
        """

        self.k_nearest_indexs = np.zeros((X.shape[0], self.Neighbors))#儲存每筆資料離其他資料距離的前3小索引值
        for i in range(X.shape[0]):
            pre_x_ = X[i]
            distance = self.minkowski_distance(X, pre_x_)
            k_nearest_index = np.argsort(distance)[1:self.Neighbors+1]
            self.k_nearest[i]=k_nearest_index

    def get_weights(self, X):
        
        if self.Weights=="uniform":
            return np.ones(X.shape[0])
        
        elif self.Weights=="distance":
            get_weight = np.ones(X.shape[0])
            for i in range(X.shape[0]):
                get_weight[i]=1/
            return get_weight

    def minkowski_distance(self, X1, X2):
        return np.sum(np.abs(X1-X2)**self.p)**(1/self.p)
    
    def predict(self, X):#預測訓練資料的答案
        """
        X:訓練資料
        """




    def score(self, X, y):
        """
        X:測試資料
        y:測試答案
        """

print(sklearn.__path__)