import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split, cross_val_score
import sklearn
from sklearn.model_selection import GridSearchCV
import time

def test():
    
    KNN = KNeighborsClassifier(5)  
    KNN.fit(x_Train, y_Train)  
    Prediction = KNN.predict(x_Test)   
    #print(Prediction)
    print(KNN.score(x_Test, y_Test))

    #param_grid = {'n_neighbors': np.arange(1, 31), 'weights': ['uniform', 'distance']}
    #grid_search = GridSearchCV(KNN, param_grid, cv=5)
    #grid_search.fit(X, y)
    #print(grid_search.best_params_)  
    #print(grid_search.score(x_Test, y_Test))
#----------------------------------------------------------------------------------------
    
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
        self.X=X
        self.y=y
     
        self.pre_ans = np.zeros(X.shape[0]) #預測答案
        if self.metric==None:
            distance = self.minkowski_distance(X[:, np.newaxis, :], X[np.newaxis,: ,:]) #自己對應自己的距離為X[j for j in range(X.shape[1])][i]
            distance = distance*self.get_weights(X)
            
            nearst_index = np.argsort(distance)[::, 1:self.Neighbors+1] #取得每row前N短的距離, 因為會包含自己所以index+1
            for i, mask in enumerate(nearst_index):
                unquie_ , counts = np.unique(y[mask], return_counts=True)
                self.pre_ans[i]=unquie_[np.argmax(counts)] #取得前N近的資料重複最多的答案


    def get_weights(self, X):
        if self.Weights=="uniform":
            
            return np.ones(X.shape[0])
        
        elif self.Weights=="distance":
            distances = self.minkowski_distance(X[:, np.newaxis, :], self.X[np.newaxis, :, :])
        
            return 1/np.sum(distances, axis=1)

    def minkowski_distance(self, X1, X2): #回傳個別向量與其他向量的每一個距離, 回傳結果輸入(5,2)則回傳(5,5)每個向量的距離
        
        return np.sum((np.abs(X1-X2)**self.p), axis=2)**(1/self.p)
    
    def predict(self, X): #預測訓練資料的答案
        """
        X:訓練資料
        """
        y= self.y
        train_y = np.concatenate((self.y, np.empty(X.shape[0])))
        train_data = np.vstack((self.X, X))
        self.fit(train_data, train_y)
        
        return self.pre_ans[-X.shape[0]:]

    def score(self, X, y):
        """
        X:測試資料
        y:測試答案
        """
        pre = self.predict(X)
        corroct = np.sum(pre==y)
        
        return corroct/len(y)


def grid(model):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    best_score_manual = 0
    best_params_manual = {}

    for n_neighbors in np.arange(1, 31):
        for weights in ['uniform', 'distance']:
            model_obj = model(n_neighbors=n_neighbors, weights=weights)
            scores = cross_val_score(model_obj, X_train, y_train, cv=5)
            mean_score = scores.mean()    
            if mean_score > best_score_manual:
                best_score_manual = mean_score
                best_params_manual = {'n_neighbors': n_neighbors, 'weights': weights}

    return best_params_manual, best_score_manual

def main_KNN():
    
    KNN = KNN_classifier()
    KNN.fit(x_Train, y_Train)
    #print(KNN.predict(x_Test))
    #print(y_Test)
    print(KNN.score(x_Test, y_Test))
    #print(KNN.get_weights(x_Train))



#數據
X, y = make_blobs(n_samples=1000, n_features=4, centers=3, cluster_std=5)
x_Train, x_Test, y_Train, y_Test = train_test_split(X, y, test_size=0.2)
str = time.time()
end = time.time()

#--------------------------------------------------------------------------
print("我的:")
str = time.time()
main_KNN()#我的
end = time.time()
print(end-str)

#--------------------------------------------------------------------------
print("sklearn的:")
str2 = time.time()
test()#sklearn的
end2 = time.time()
print(end2-str2)


