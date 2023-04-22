#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int list[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int sum = 0;

    for (int i : list) // for 변수 : 범위
    {
        sum += i; // 리스트를 돌며 그 안의 모든 것을 더해
    }

    cout << sum << endl
         << endl;

    for (int &i : list)
    {
        cout << i << " ";
    }
    cout << endl;

    for (auto &i : list)
    {
        cout << i << " ";
    }

    return 0;
}

/*
55

1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
*/