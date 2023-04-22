#include <Led.h>

#include <TimerOne.h>

boolean led_val = LOW;
Led led(9);

void setup() {
  // 타이머1 인터럽트 설정 및 동작 시작
  Timer1.initialize(50000); // 500ms 주기 설정
  Timer1.attachInterrupt(flash); // 인터럽트 함수 지정
}

void loop() {

}

// 타이머1 인터럽트 함수, 500ms 마다 자동 실행
void flash() {
  led_val = !led_val; // LED 출력 변수 반전
  led.setValue(led_val);
}