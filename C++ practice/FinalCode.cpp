#include <iostream>     //輸入輸出程式庫
#include <string>       //標準字串程式庫
#include <stdio.h>      //標準字串程式庫
#include <ctime>        //C++內建時間模組
#include <random>       //亂數產生程式庫

using namespace std;    //使用標準程式庫std

class FinalCode//包裝方法
{
    private://私變數，不開放讀取使用的變數
    int num_min = 0;
    int num_max = 0;
    int num_ans = 0;

    public://公變數，反之
    int range_min = 0;
    int range_max = 0;

    FinalCode(int min, int max , int ans)//建構子(需要與class同名)，輸入的參數要做什麼內容
    {
        num_min = min;
        num_max = max;
        num_ans = ans;

        range_min = min;
        range_max = max;
    }
    //超出範圍
    bool OutOfRange(int guess)
    {
        return guess>range_max || guess<range_min;
    }
    //比答案大
    bool MoreThan(int guess)
    {
        if (guess>num_ans)
        {
            range_max = guess;
            return true;
        }
        else return false;
    }
    //比答案小
    bool LessThan(int guess)
    {
        if (guess<num_ans)
        {
            range_min = guess;
            return true;
        }
        else return false;
    }
    //猜中答案
    bool Correct(int guess)
    {
        if (guess==num_ans)
        {
        range_max = guess;
        range_min = guess;
        return true;
        }
        else return false;
    }
};

int main(void)
{
    const int min = 0;
    const int max = 100;

    mt19937 rg(time(NULL));
    uniform_int_distribution<int> dis(min+1, max-1);

    FinalCode cr(min, max, dis(rg));

    int guess = 0;

    do//先做邏輯在循環還變化
    {
        cout << "Please guess a number : \t" <<cr. range_min << " to " << cr.range_max << endl;
        cin >> guess;
        if(cr.OutOfRange(guess))
        {
            cout << "Enter Error" << endl;
            continue;
        }

        if(cr.MoreThan(guess))
        {
            continue;
        }
        else if(cr.LessThan(guess))
        {
            continue;
        }
        
        if(cr.Correct(guess))
        {
            cout << "congratulation!!";
            break;
        }
    }
    while(!cr.Correct(guess));//可在前方加!為反義詞
    {
        system("pause");
    }
    




    #pragma region 
    /*
    const int min_num = 0;
    const int max_num = 100;

    mt19937 rg(time(NULL));
    uniform_int_distribution<int> dis(min_num, max_num);

    int target = dis(rg);
    int guess = 0;

    for(int i=0; i<=10; i++)
    {
        cout << "guess number\t" << min_num << "~" << max_num << endl << endl;
        cin >> guess;
        if(guess==target)
        {
            cout << "Congratulations!!";
            break;
        }
        else
        {
            if(guess>target)
            {
                cout << "less than" << guess << endl;
            }
            else if(guess<target)
            {
                cout << "more than" << guess << endl;
            }
        }
        if(i==10)
        {
            cout << "you loss!!";
        }
    }*/
    
    #pragma endregion

    return 0;
}