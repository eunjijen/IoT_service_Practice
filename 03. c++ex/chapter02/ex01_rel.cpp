#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    bool b;

    b = (1 == 2); // 0

    cout << std::boolalpha; // �ο︰�� true, false�� ���

    cout << b << endl; // false

    return 0;
}
