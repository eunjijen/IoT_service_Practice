#include <iostream>
#include <string>

using namespace std;

class Car
{
public:
    int speed;
    int gear;
    string color;

    void speedUp()
    {
        speed += 10;
    }

    void speedDown()
    {
        speed -= 10;
    }
};

int main(int argc, char const *argv[])
{
    Car car1;

    car1.speed = 80;
    car1.gear = 3;
    car1.color = "red";

    car1.speedUp();
    car1.speedDown();

    return 0;
}
