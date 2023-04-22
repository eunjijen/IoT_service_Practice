#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    bool b;
    int x = 3;
    int y = 3;

    cout << std::boolalpha;

    b = (x == 3) && (y == 3);
    cout << b << endl; // true

    y = 2;
    b = (x == 3) && (y == 3);
    cout << b << endl; // false

    b = (x == 3) || (y == 3);
    cout << b << endl; // true

    x = 2;
    b = (x == 3) || (y == 3);
    cout << b << endl; // false

    b = !(x == 3);
    cout << b << endl; // true

    return 0;
}
