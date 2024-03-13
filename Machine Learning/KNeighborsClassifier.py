import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import time

def test():
    
    KNN = KNeighborsClassifier()  
    KNN.fit(x_Train, y_Train)  
    Prediction = KNN.predict(x_Test)   
    #print(Prediction)
    print(KNN.score(x_Test, y_Test))

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
        train_y = np.concatenate((self.y, np.empty(X.shape[0])))
        train_data = np.vstack((self.X, X))

        self.pre_ans = np.zeros(train_data.shape[0]) #預測答案
        if self.metric==None:
            distance = self.minkowski_distance(train_data[:, np.newaxis, :], train_data[np.newaxis,: ,:]) #自己對應自己的距離為X[j for j in range(X.shape[1])][i]
            distance = distance*self.get_weights(train_data)
            
            nearst_index = np.argsort(distance)[::, 1:self.Neighbors+1] #取得每row前N短的距離, 因為會包含自己所以index+1
            for i, mask in enumerate(nearst_index):
                unquie_ , counts = np.unique(train_y[mask], return_counts=True)
                self.pre_ans[i]=unquie_[np.argmax(counts)] #取得前N近的資料重複最多的答案
        
        return self.pre_ans[-X.shape[0]:]

    def score(self, X, y):
        """
        X:測試資料
        y:測試答案
        """
        pre = self.predict(X)
        corroct = np.sum(pre==y)
        return corroct/len(y)

def main_KNN():
    
    KNN = KNN_classifier()
    KNN.fit(x_Train, y_Train)
    print(KNN.score(x_Test, y_Test))


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


