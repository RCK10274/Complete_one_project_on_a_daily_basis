#include <iostream>     //輸入輸出程式庫
#include <string>       //標準字串程式庫
#include <stdio.h>      //標準字串程式庫
#include <ctime>        //C++內建時間模組
#include <random>       //亂數產生程式庫

using namespace std;    //使用標準程式庫std

int main(void)
{

    const int min = 0;
    const int max = 100;

    int range_min = min;
    int range_max = max;

    mt19937 rg(time(NULL));
    uniform_int_distribution<int> dis(min+1, max-1);
    int target = dis(rg);
    int guess = 0;

    do//先做邏輯在循環還變化
    {
        cout << "Please guess a number : \t" << range_min << " to " << range_max << endl;
        cin >> guess;
        if(guess>range_max || guess<range_min)
        {
            cout << "Enter Error" << endl;
            continue;
        }

        if(guess>target)
        {
            range_max = guess;
            continue;
        }
        else if(guess<target)
        {
            range_min = guess;
            continue;
        }
        
        if(guess==target)
        {
            cout << "congratulation!!";
            break;
        }
    }
    while(guess!=target);
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