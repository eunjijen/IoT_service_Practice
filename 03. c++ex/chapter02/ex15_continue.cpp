#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    for (int i = 1; i < 5; i++)
    {
        cout << "continue 문장 전에 있는 문장" << endl;
        continue; // 현재 루프 몸체의 끝으로 이동
        cout << "continue 문장 이후에 있는 문장" << endl;
        // continue문은 여기로 이동
    }
    return 0;
}

/*
continue 문장 전에 있는 문장
continue 문장 전에 있는 문장
continue 문장 전에 있는 문장
continue 문장 전에 있는 문장
*/