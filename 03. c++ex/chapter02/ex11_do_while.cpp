#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    string str;
    do
    {
        cout << "���ڿ��� �Է��ϼ���:";
        // getline(cin, str);
        cin >> str;

        cout << "������� �Է�: " << str << endl;
    } while (str != "����"); // ������ ���� ���� �ݺ� (�Է��� ���ڿ��� ���ᰡ �ƴ� ��� �ݺ�)

    return 0;
}