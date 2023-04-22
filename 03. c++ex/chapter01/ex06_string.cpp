#include <iostream>
#include <string> // 문자열 사용할 때 반드시 필요

using namespace std;

int main(int argc, char const *argv[])
{
    string s1 = "Good";
    string s2 = "Morning";
    string s3 = s1 + " " + s2 + "!";
    cout << s3 << endl;

    string s4 = "Good";
    string s5 = "Bad";
    bool b = (s4 == s5);
    cout << b << endl; // result : 0

    // string s6 = "Good" + "Morning" + "!"; 이렇게 쓰면 에러

    return 0;
}
