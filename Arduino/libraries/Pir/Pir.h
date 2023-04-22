# pragma once

# include <Arduino.h>

typedef void (*pir_callback_t)();

class Pir {
  protected:
    int pin;
    int state;
    pir_callback_t on_f;  // 상승 엣지에서 호출할 함수
    pir_callback_t off_f;  // 하강 엣지에서 호출할 함수

  public:
    Pir(int pin);
    void setCallback(pir_callback_t on_f, pir_callback_t off_f);
    void check();
};


