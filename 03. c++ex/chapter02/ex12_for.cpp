#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int sum = 0;
    for (int i = 0; i <= 10; i++)
    {
        sum += i;
    }

    cout << "1���� 10���� ������ �� = " << sum << endl;
    // 1���� 10���� ������ �� = 55
    return 0;
}