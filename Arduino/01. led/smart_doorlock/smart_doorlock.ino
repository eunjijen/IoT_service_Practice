// 수행평가 
# include <Minicom.h>
# include <EEPROM.h>
# include <Servo.h>
# include <Keypad.h>
# include <LiquidCrystal_I2C.h>
# include <Led.h>

void receive_msg(String);
MiniCom com;
LiquidCrystal_I2C lcd(0x27, 16, 2);
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
String password = "#1231";  // 마지막에 *입력해서 true 리턴 

Led led(A0);
char state = _CLOSE;
int err_count = 0;
unsigned long last_input_time = 0;


void receive_msg(String msg) {
  input = msg;
  check();
}

void setup() {
  Serial.begin(9600);
  char passwordArr[6];  // password를 저장할 char 배열 선언
  password.toCharArray(passwordArr, 6);  // password 문자열을 char 배열로 변환
  
  // EEPROM에 한 글자씩 저장
  for(int i=0; i<6; i++) {
    EEPROM.write(i, passwordArr[i]);
  }

  lcd.clear();
  com.init();
  lcd.noBacklight();  // 평상시에는 lcd 백라이트 off
  lock.attach(3);
  lock.write(_CLOSE);
}

void open() {
  lcd.backlight();
  lock.write(_OPEN);
  com.print(1, "OPEN");
  state = _OPEN;  // 상태변수 변경
}

void close() {
  lock.write(_CLOSE);
  state = _CLOSE; 
  lcd.clear();
  lcd.noBacklight();  // 문이 열렸다가 닫힐 때 백라이트 off
}

void beep() {
  led.on();
  delay(100);
  led.off();
}

void longBeep() {  
  delay(500);
  for(int i = 0; i < 3; i++) {
    led.on();
    beep();
    delay(200);
    led.off();
  }
}

// *을 입력받았을 때 true (*은 포함하지 않는 문자열은 전역변수 input에 저장)
// 나머지 경우 false 리턴
boolean getline() {
  char key = keypad.getKey();  // 입력값을 받아
  int star = 0;  // 비밀번호 * 출력 초기화

  if (key) {
    lcd.backlight();  // key 누를때 백라이트 on
    beep();

    if (key == '*') {
      return true;
    }
    input += key; 
    star++;
    lcd.print('*') * star;  // 입력된 글자 수만큼 * 출력
    last_input_time = millis();  // 마지막 입력 시간
  }
  else {
    if(millis() - last_input_time > 3000) {  // 3초간 입력이 없으면 초기화, 백라이트 off
      lcd.clear();
      lcd.noBacklight();
    }
  }
  return false;
}

void check() {
  if(input == password) {
    open();
    SimpleTimer &timer  = com.getTimer();
    timer.setTimeout(3000, close); 
    err_count = 0; // 2번 틀리고 맞았다가 다시 한 번 틀리면(3번 누적) 1분간 입력 불가하므로 열리면 초기화
  }
  else {  
    err_count++;   
    if(err_count >= 3) {  // 3회 연속 틀렸을 때
      com.print(1, "Wait for 1 min");
      delay(60000);  // 1분간 입력 불가
      err_count = 0;
      lcd.noBacklight();  // 1분 지나면 백라이트 off --> 다시 입력 가능
    }
    lcd.clear();
    lcd.noBacklight();  // 실패했을 때 백라이트 off
    longBeep();
  }
  input = "";
}

void loop() {
  boolean result = getline();
  char passwordArr[6];
  // EEPROM에서 password 배열 불러오기
  for(int i=0; i<6; i++) {
    passwordArr[i] = EEPROM.read(i);
  }
  passwordArr[5] = '\0';  // 배열의 마지막에 null 문자 추가
  password = passwordArr;  // 배열을 String으로 변환

  if (result) {
    check();
  }
  com.run();
}
