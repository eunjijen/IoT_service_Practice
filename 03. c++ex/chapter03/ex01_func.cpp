#include <iostream>
using namespace std;

int max(int x, int y) // max �Լ��� ���� (prototype)
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
    cout << "�Լ� call ��� : " << n << endl; // �Լ� call ��� : 3
    return 0;
}
