#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int x = 10; // 원본 데이터
    int &r = x;

    r = r + 10;
    cout << r << endl; // 20
    cout << x << endl; // 20, r을 가지고 원본을 수정함

    return 0;
}
