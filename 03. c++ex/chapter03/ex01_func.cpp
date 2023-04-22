#include <iostream>
using namespace std;

int max(int x, int y) // max 함수의 원형 (prototype)
{
    if (x > y)
        return x;
    else
        return y;
}

int main(int argc, char const *argv[])
{
    int n;
    n = max(2, 3);
    cout << "함수 call 결과 : " << n << endl; // 함수 call 결과 : 3
    return 0;
}
