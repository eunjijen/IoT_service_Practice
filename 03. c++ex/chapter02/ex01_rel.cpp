#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    bool b;

    b = (1 == 2); // 0

    cout << std::boolalpha; // 부울린을 true, false로 출력

    cout << b << endl; // false

    return 0;
}
