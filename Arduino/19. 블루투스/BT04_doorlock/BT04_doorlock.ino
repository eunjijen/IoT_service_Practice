// 블루투스로 비밀번호를 입력하면 문이 열렸다가 3초뒤에 닫힘
// 비밀번호가 틀리면 led 깜빡임

# include <Servo.h>
# include <Keypad.h>
# include <BtMiniCom.h>
# include <Led.h>

void receive_msg(String);

BtMiniCom com(13, 12, receive_msg);
Servo lock;

const byte ROWS = 4;
const byte COLS = 4;
char keys [ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS] = {7, 6, 5, 4};
byte colPins[COLS] = {8, 9, 10, 11};

const int _OPEN = 90;
const int _CLOSE = 0;

Keypad keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);
String input = "";
String password = "1231";

Led led(A0);
char state = _CLOSE;

void receive_msg(String msg) {
  input = msg;  // 전역변수 input을 msg로 대체
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
  state = _CLOSE;  // 상태변수 변경
}

void beep() {
  led.on();
  delay(100);
  led.off();
}

void longBeep() {
  delay(1000);
  for(int i = 0; i < 5; i++) {
    led.on();
    beep();
    delay(200);
    led.off();
  }
}

// *을 입력받았을 때 true (*은 포함하지 않는 만자열은 전역변수 input에 저장)
// 나머지 경우 false 리턴
boolean getline() {
  char key = keypad.getKey();
  if (key) {
    beep();
    if (key == '*') {
      return true;
    }
    input += key;
  }
  return false;
}

void check() {
  if(input == password) {
    open();
    SimpleTimer &timer  = com.getTimer();
    timer.setTimeout(3000, close); 
  }
  else {  // 열려 있는 경우 시간 연장
    longBeep();
  }
  input = "";
}

void loop() {
  boolean result = getline();
  if (result) {
    check();
  }
  com.run();
}
