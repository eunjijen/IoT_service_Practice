#include <iostream>
using namespace std;

#define WIDTH 9
#define HEIGHT 3

int main()
{
    int table[HEIGHT][WIDTH];
    int r, c;

    for (r = 0; r < HEIGHT; r++)
    {
        for (c = 0; c < WIDTH; c++)
        {
            table[r][c] = (r + 1) * (c + 1); // 행과 열의 숫자를  곱한 값을 대입
        }
    }

    for (r = 0; r < HEIGHT; r++)
    {
        for (c = 0; c < WIDTH; c++)
        {
            cout << table[r][c] << ", "; // 대입해서 생성된 값에 ,를 찍어줌
        }
        cout << endl;
    }
    return 0;
}

/*
1, 2, 3, 4, 5, 6, 7, 8, 9,
2, 4, 6, 8, 10, 12, 14, 16, 18,
3, 6, 9, 12, 15, 18, 21, 24, 27,
*/