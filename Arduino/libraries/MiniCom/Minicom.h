# pragma once

# include <Arduino.h>
# include <LiquidCrystal_I2C.h>
# include <SimpleTimer.h>

class MiniCom {
  protected:
    long serial_bps;  // Serial ?��?��
    LiquidCrystal_I2C lcd;
    SimpleTimer timer;
    bool no_lcd; // LCD ?��?�� ?���?

  public:
    MiniCom(long serial_bps = 115200, int lcd_addr = 0x27);
    void setNoLcd() { no_lcd = true;};
    void  init();
    void run();

    int setInterval(unsigned long interval, timer_callback f);
    SimpleTimer& getTimer() { return timer; }

    //LCD 출력 �??�� 메서?�� helper ?��?��
    void print(int row, String msg);
    void print(int row, String title, int value);
    void print(int row, String title1, int value1, String title2, int value2);
    void print(int row, String title, double value);
    void print(int row, String title1, double value1, String title2, double value2);
};