#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int n = 10;

    while (n > 0)
    {
        cout << n << " ";
        n--;
    }

    cout << "fire!" << endl;

    // 10 9 8 7 6 5 4 3 2 1 fire!
    return 0;
}
