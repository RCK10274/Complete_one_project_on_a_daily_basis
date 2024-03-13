#this file is my funtions for practicing Machine_learn.
#In order to prevent forgetting, I need to record it.
import numpy as np
import pandas as pd

#------------------------------------------------------------------------------------------

def drop_null_column(df):#刪除缺失值的整筆資料,null與None視為等價,可用同個方式刪除
    
    df.replace(r'^\s*$', np.nan, regex=True, inplace=True)#將所有為空白或是複數個空白的值轉換成null;
    #regex正則r'^\s*$'表示初始(^)為空白(" ")並出現0~n次(*)到結束($)
    df = df.dropna()#刪除缺失值的方法,可設定axis=1為刪列,預設axis=0刪行,subset=["指定欄位"]
    df.isnull()#檢查每格資料是否為空值,要用的話記得回傳
    df.fillna(10)#將df中所有null改成10,要用的話記得回傳
    return df
#------------------------------------------------------------------------------------------

def ceiling_floor(df, col):#天花板與地板法 IOR找出極端值
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    #極端值定義 Q1 - 1.5IQR 或是高於 Q3 + 1.5IQR 的值。
    lower_limit = Q1 - 1.5 * IQR #極端值(下限)
    upper_limit = Q3 + 1.5 * IQR #極端值(上限)

    extreme_values = df[(df[col] < lower_limit) | (df[col] > upper_limit)].index
    max_ = df[col].drop(index=extreme_values).max()
    min_ = df[col].drop(index=extreme_values).min()
    df[col][(df[col] < lower_limit)]=min_
    df[col][(df[col] > upper_limit)]=max_
    

    return df
#------------------------------------------------------------------------------------------

class Normalization:#資料正規化 Data Normalization
    def __init__(self, row):
        self.row = row

    def Min_Max(self):#極值正規化
        return (self.row-self.row.min())/(self.row.max()-self.row.min())
    
    def Z_Score(self):#Z_Score正規化
        return (self.row-self.row.mean())/self.row.std()
    
#------------------------------------------------------------------------------------------
    
class Data_discretization:#離散化數據-裝箱法
    def __init__(self) -> None:
        pass

    def width_fountion(self,nums):#等寬分類
        #定義:使用者所給定之箱子個數n下，依據排序過後資料數值之最大值與最小值切割成n個等寬箱子
        nums = np.sort(nums)
        n = int(input("輸入寬度"))
        width = (nums[-1]-nums[0])/n
        n_min = nums.min()
        n_max = n_min+width
        init_data = []
        while n_max!=nums[-1]+width:
            data_index = np.where((n_min<=nums) & (nums<=n_max))
            init_data.append(nums[data_index])
            n_min = n_max+1
            n_max += width
        return init_data

    def deep_fountion(self,nums):#等深分類
        #定義:在使用者所給定之箱子個數n下，依據資料的數量切割成n個數量相等箱子
        nums = np.sort(nums)
        n = int(input("輸入深度"))
        deep = round(len(nums)/n)
        start = 0
        end = deep
        deep_list = []
        while True:
            deep_list.append(nums[start:end])
            start = end
            end = start+deep
            if end>len(nums)-1:
                end = len(nums)
                deep_list.append(nums[start:end])
                break
        return deep_list
    
#------------------------------------------------------------------------------------------

class Sampling:#取樣
    def __init__(self, df):
        self.df =df

    def random_sample(self, n=None, frac=None):#隨機取樣, frac=抽取數據%數,也可以直接寫抽取數量

        if n is not None:
            sampled_df = self.df.sample(n=n)
        elif frac is not None:
            sampled_df = self.df.sample(frac=frac)
        else:
            raise ValueError("Either n or frac must be provided.")
        return sampled_df
    
    def stratified_sample(self, column, n=None, f=None):#分層取樣
        def s_sample(df, n_samples=None, frac=None):
            return df.sample(n=n_samples, frac=frac)
        stratified__df = self.df.groupby(column).apply(s_sample, n_samples=n, frac=f).reset_index(drop=True)
        return stratified__df

def one_hot(df, col_name, font_name):
    one_hot_df = pd.get_dummies(df[col_name], prefix=font_name) #prefix為前缀
    return one_hot_df

#------------------------------------------------------------------------------------------

if __name__=="__main__":
    data_path = r""
    df = pd.read_csv(data_path)
    #-----------------------------------------------


