#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int x = 10; // ���� ������
    int &r = x;

    r = r + 10;
    cout << r << endl; // 20
    cout << x << endl; // 20, r�� ������ ������ ������

    return 0;
}
