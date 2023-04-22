# include "Button.h"

Button::Button(int pin):pin(pin) {
  pinMode(pin, INPUT_PULLUP); 
  callback = NULL;
}

void Button::setCallback(button_callback_t callback) {
  this -> callback = callback;
}

// 누른 경우에 H, 땐 경우에 L을 리턴
int Button::read() {
  return !digitalRead(pin);
}

// polling 방식으로 버튼이 눌러졌는지 체크
void Button::check() {
  bool o_sw, n_sw;

  o_sw = read();
  delay(10);
  n_sw = read();

  if(o_sw == 0 && n_sw == 1) {
    if(callback != NULL) {
      callback();
    }
  }

}


