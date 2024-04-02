#include <iostream>     //inclode引入標準程式庫 輸入輸出的程式庫
#include <string>   //引入標準字串程式庫
#include <stdio.h> //標準函式庫

using namespace std;    //std是標準程式庫的命名空間有很多工具，";"為結束


int main(void)  //int為整數，void為虛無、空白值，main()中要輸入參數，但沒有特定參數要輸入時則輸入void
{

    #pragma region //for 迴圈
    for(int i=1;i<10;i+=1)//for(初始值; 結束條件; 遞增次數)
    {
        for(int j=1;j<10;j+=1)
        {
            cout << j << "X" << i << "=" << i*j << "\t";
        }
        cout << endl;
    }

    #pragma endregion

    #pragma region //while迴圈
    /*
    int num = 0;
    while (num<=10)//連續的判斷式
    {
        cout <<endl<< num;
        num += 1;
    }
    */
    #pragma endregion

    #pragma region //Switch case 同 if else 為判斷式

    /*
    int num = 1;

    switch (num)//以num變數的值做判斷
    {
        case 1://如果num是1則
            cout << "NUM is 1";
            break;
        
        default://設定條件外的輸出
            cout << "unknow";
            break;
    }
    */

    #pragma endregion

    #pragma region //if else判斷式
        /* 
        char input = 'N';
        //cin >> input ;
        if(input == 'y' || input == 'Y')
        { 
            cout << "Enter 'y'";
            //char exit = getchar();
        }
        else if(input == 'N' || input == 'n')
        {
            cout << "Enter 'N'";
        }
        else
        {
            cout << "Not correct command";
        }
        */
    #pragma endregion

    #pragma region //資料結構
        /*getchar()測試與資料結構
        int number = 3;
        bool boolean = true; //預設false
        char chartxt = 'A'; //單引號包住要宣告的字元，預設false
        long longnumber = 4L;   //C#會強制加上L，C++可加可不加，建議標L
        float floatnumber = 3.0F;   //C#可加可不加F，建議標F
        double doublenumber = 4.6; //

        cout << endl << "你好這個世界" << endl <<"Hellow World\nI am learning C++" <<endl ; 
        cout<iostream>標準庫的功能， endl/\n是換行符號<string>的標準功能
        cout << "Exit when enter any button........." <<endl;
        char end = getchar();   //<stdio.h>的功能
        */
    #pragma endregion
        

        return 0;
}
