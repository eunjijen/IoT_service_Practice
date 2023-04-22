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
        cout << "zero\n";
        break; // break문을 만나면 switch문을 벗어나
    case 1:
        cout << "one\n";
        break;
    case 2:
        cout << "two\n";
        break;
    default:
        cout << "many\n";
        break;
    }

    return 0;
}
