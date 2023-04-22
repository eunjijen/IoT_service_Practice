#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    string str;
    do
    {
        cout << "문자열을 입력하세요:";
        // getline(cin, str);
        cin >> str;

        cout << "사용자의 입력: " << str << endl;
    } while (str != "종료"); // 조건이 참일 동안 반복 (입력한 문자열이 종료가 아닐 경우 반복)

    return 0;
}