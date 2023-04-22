#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    long fact = 1;
    int n;

    cout << "input number: ";
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        fact = fact * i;
    }

    cout << n << "! = " << fact << endl;
    // input number: 5
    // 5 ! = 120
    return 0;
}
