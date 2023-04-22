#include <iostream>
#include <string>

using namespace std;

class Circle
{
public:
    int radius;
    string color;

    double calcArea()
    {
        return 3.14 * radius * radius; // 원의 면적
    }
};

int main(int argc, char const *argv[])
{
    Circle obj; // 객체 생성
    obj.radius = 100;
    obj.color = "blue";

    cout << "원의 면적 " << obj.calcArea() << endl;

    return 0;
}
