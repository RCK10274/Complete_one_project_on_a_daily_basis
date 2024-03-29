#include <iostream>     //inclode引入標準程式庫 輸入輸出的程式庫
#include <string>   //引入標準字串程式庫
#include <stdio.h> //標準函式庫


using namespace std;    //std是標準程式庫的命名空間有很多工具，";"為結束


#pragma region test data structure / getchar() 


int main(void)  //int為整數，void為虛無、空白值，main()中要輸入參數，但沒有特定參數要輸入時則輸入void
{
    char input='c';
    //cin >> input ;

    if(input == 'y')
    { 
        cout << "Enter 'y'";
        char exit = getchar();
    }
    else
    {
        cout << "Not correct \"command";
    }


#pragma region
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

#pragma endregion 此功能為折程式碼區塊