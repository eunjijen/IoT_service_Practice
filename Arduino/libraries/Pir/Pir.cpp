# include "Pir.h"
Pir::Pir(int pin): pin(pin) {
  pinMode(pin, INPUT);
  state = LOW;
  on_f = NULL;
  off_f = NULL;
}

void Pir::setCallback(pir_callback_t on_f, pir_callback_t off_f) {
  this -> on_f = on_f;
  this -> off_f = off_f;
}

void Pir::check() {
  int val = digitalRead(pin);
  if(val == HIGH) {
    if(state == LOW) {
      state = HIGH;
      if(on_f != NULL) {
        on_f();
      }
    }
  } else {
    if(state == HIGH) {
      state = LOW;
      if(off_f != NULL) {
        off_f();
      }
    }
  }
}