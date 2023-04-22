#include <Button.h>
#include <Led.h>
# include <SimpleTimer.h>

SimpleTimer timer;
Led led(8);
Button btn(2);

int timer_id = -1; // interval을 위한 타이머 id 
// -1은 아직 배정되지 않았다는 의미

const int INTERVAL_NUM = 3; // 인터벌 값 개수
int intervals[] = {1000, 600, 300}; // 인터벌 목록
int interval_ix = 0;  // 현재 인터벌 값 인덱스

void blink() {
  led.toggle();
}

void check() {
  interval_ix = (interval_ix + 1) % INTERVAL_NUM;
  timer.deleteTimer(timer_id);
  timer_id = timer.setInterval(intervals[interval_ix], blink);
}

void setup() {
  btn.setCallback(check);
  timer_id = timer.setInterval(intervals[interval_ix], blink);
}

void loop() {
  btn.check();
  timer.run();
}
