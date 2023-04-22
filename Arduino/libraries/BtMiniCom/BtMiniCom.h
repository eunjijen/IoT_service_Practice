#pragma once

#include <Arduino.h>
#include <SoftwareSerial.h>
#include <Minicom.h>

typedef void (*btminicom_callback_t)(String message);

class BtMiniCom : public MiniCom
{
protected:
  SoftwareSerial btSerial;
  btminicom_callback_t callback; // 메시지 수신시 호출할 콜백 함수 포인터
public:
  BtMiniCom(int rx, int tx, btminicom_callback_t callback = NULL,
            long serial_bps = 115200, int lcd_addr = 0x27);
  void init();
  String readLine();     // \r\n를 제외한 문자열을 리턴
  void send(String msg); // 메시지 전송
  void run();
};
