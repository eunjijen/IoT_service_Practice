#pragma once
#include <Arduino.h>

class Melody
{
protected:
  int pin;           // 핀번호
  int *notes;        // 음계 배열
  int *durations;    // 박자 배열
  int length;        // 음의 개수
  int cur_ix;        // 현재 연주하는 음의 인덱스
  long old_time;     // 이전 시간
  int note_duration; // 현재 연주하는 음의 길이
  boolean b_play;    // 연주 여부
public:
  Melody(int pin, int *notes, int *durations, int length);
  void play();
  void stop();
  int toggle(bool bpause = false);
  void replay(); // 정지된 곳에서 다시 시작
  int getNote(); // 현재 재생 음
  void run();
};
