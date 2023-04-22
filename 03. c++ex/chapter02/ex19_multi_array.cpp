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
            table[r][c] = (r + 1) * (c + 1); // ��� ���� ���ڸ�  ���� ���� ����
        }
    }

    for (r = 0; r < HEIGHT; r++)
    {
        for (c = 0; c < WIDTH; c++)
        {
            cout << table[r][c] << ", "; // �����ؼ� ������ ���� ,�� �����
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