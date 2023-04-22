#include "Ultra.h"

Ultra::Ultra(int echo, int trig) : echo(echo), trig(trig)
{
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  on_f = NULL;
  off_f = NULL;
  state = false;
  threshold = 0;
}

int Ultra::getDistance()
{
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  // echo 핀 입력으로부터 거리를 cm 단위로 계산
  // y = 0.034 * x / 2 = 0.017 * x cm --> 실수 연산
  int distance = pulseIn(echo, HIGH) / 58;
  return distance;
}

void Ultra::setThreshold(int t, ultra_callback_t on_f, ultra_callback_t off_f)
{
  threshold = t;
  this->on_f = on_f;
  this->off_f = off_f;
}

int Ultra::run()
{
  int distance = getDistance();
  if (!state && distance <= threshold)
  { // 기준 거리내로 진입한 경우
    state = true;
    if (on_f != NULL)
    {
      on_f();
    }
    delay(1000);
    // 기준 거리를 벗어난 경우
  }

  else if (state && (distance == 0 || distance > (threshold + 2)))
  {
    state = false;
    if (off_f != NULL)
    {
      off_f();
    }
    delay(1000);
  }

  if (distance == 0 || distance > threshold)
  {
    return 0;
  }

  return distance;
}
