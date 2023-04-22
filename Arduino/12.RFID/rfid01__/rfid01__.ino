#include <SPI.h>
#include <MFRC522.h>
#include <Led.h>
#include <Servo.h>
#include <MiniCom.h>
#include <Button.h>
#include <EEPROM.h>

#define RST_PIN   9   // reset핀은 9번으로 설정
#define SS_PIN    10  // SS핀은 10번으로 설정
                      // SS핀은 데이터를 주고받는 역할의 핀( SS = Slave Selector )
Led led(6);
Servo door;
byte myId[4] = {0, };  // 등록된 ID

MiniCom com;
MFRC522 mfrc(SS_PIN, RST_PIN);   // MFR522 객체 생성
Button btn(2);

void beep() {
  led.on();
  delay(100);
  led.off();
}

boolean compare(byte uid[]) {
  // myId와 uid를 비교
  for(int i=0; i<4; i++) {
    if( uid[i] != myId[i]) {
      return false;
    }
  }
  return true;
}

void registerId(byte uid[]) {
  for(int i=0; i<4; i++) {
    myId[i] = uid[i];
    EEPROM.write(i, uid[i]);
  }

  // 등록 성공 효과음
  delay(1000);
  for(int i=0; i<2; i++) {
    beep();
    delay(100);
  }
}


void open() {
  door.write(90);
  com.print(1, "Open");
}

void close() {
  door.write(0);
  com.print(1, "Close");

}


void setup(){
  com.init();
  SPI.begin();
  mfrc.PCD_Init(); 

  for(int i=0; i<4; i++) {
    myId[i] = EEPROM.read(i);
  }

  door.attach(3);
  door.write(0);
  com.print(1, "Close");
}

void loop(){
  com.run();
  if ( !mfrc.PICC_IsNewCardPresent() || !mfrc.PICC_ReadCardSerial() ) {   
    // 태그 접촉이 되지 않았을때 또는 ID가 읽혀지지 않았을때
    delay(500); 
    return;
  } 
  beep();

  if(btn.read()) {  // 등록
    registerId(mfrc.uid.uidByte);
  } else {  // 검사
    boolean result = compare(mfrc.uid.uidByte);
    if(result) {
      open();
      SimpleTimer &timer = com.getTimer();
      timer.setTimeout(3000, close);
    } 
  }

}
