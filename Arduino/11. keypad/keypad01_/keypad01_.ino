#include <BtMiniCom.h>
#include <Keypad.h>
#include <Led.h>
#include <Servo.h>

void receive_msg(String);

BtMiniCom com(13, 12, receive_msg);
Servo lock;    

const byte ROWS = 4;    // 행(rows) 개수
const byte COLS = 4;    // 열(columns) 개수
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
 
byte rowPins[ROWS] = {7, 6, 5, 4};      // R1, R2, R3, R4 단자가 연결된 핀 번호
byte colPins[COLS] = {8, 9, 10, 11};    // C1, C2, C3, C4 단자가 연결된 핀 번호

const int _OPEN = 90;
const int _CLOSE = 0;

Keypad keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);
String input = "";
String password = "1234";

Led led(A0);

int state = _CLOSE;

void receive_msg(String msg) {
  input = msg;
  check();
}


void setup() {
  com.init();
  com.print(0, "[[Door Lock]]");
  com.print(1, "CLOSE");
  lock.attach(3);
  lock.write(_CLOSE);
}


void open() {
  lock.write(_OPEN);
  com.print(1, "OPEN");
  state = _OPEN;
}

void close() {
  lock.write(_CLOSE);
  com.print(1, "CLOSE");
  state = _CLOSE;  
}

void beep() {
  led.on();
  delay(100);
  led.off();
}

void longBeep() {
  delay(1000);
  for(int i=0; i<5; i++) {
    beep();
    delay(100);
  }
}


// *을 입력받았을 때 true 
// (*을 포함하지 않는 문자열은 전역변수 input에 저장)
// 나머지 경우 false 리턴
boolean getLine() {
  char key = keypad.getKey();
  if (key) {
    beep(); // 효과음 출력
    if(key == '*') {
      return true;
    }
    input += key;
  }
  return false;
}

void check() {
  if(input == password) { // 문을 개방
    open();
    SimpleTimer &timer = com.getTimer();
    timer.setTimeout(3000, close);
  } else { // 경보 출력
    longBeep();
  }
  input = "";   
}

void loop() {
  boolean result =  getLine();
  if(result) {
    check();
  }
  com.run();
}
