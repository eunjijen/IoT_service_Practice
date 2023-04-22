#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int number;
    cout << "input number:";
    cin >> number;

    switch (number)
    {
    case 0:
        cout << "zero\n"; // break가 없으면 다음 걸로 이동
    case 1:
        cout << "one\n";
    case 2:
        cout << "two\n";
    default:
        cout << "many\n";
        break;
    }
    return 0;
}
