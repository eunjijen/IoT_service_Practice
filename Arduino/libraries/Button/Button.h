# pragma once

# include <Arduino.h>

// 매개변수 없는 void 함수에 대한 포인터를 button_callback_t로 정의
typedef void (*button_callback_t)();

class Button {
protected:
  int pin;
  button_callback_t callback; // callback 함수에 대한 포인터

public:
  Button(int pin); 
  void setCallback(button_callback_t callback); 
  int read();
  void check();
};