#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    for (int i = 1; i < 5; i++)
    {
        cout << "continue ���� ���� �ִ� ����" << endl;
        continue; // ���� ���� ��ü�� ������ �̵�
        cout << "continue ���� ���Ŀ� �ִ� ����" << endl;
        // continue���� ����� �̵�
    }
    return 0;
}

/*
continue ���� ���� �ִ� ����
continue ���� ���� �ִ� ����
continue ���� ���� �ִ� ����
continue ���� ���� �ִ� ����
*/