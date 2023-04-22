#include <Key.h>
#include <Keypad.h>
#include <Minicom.h>

MiniCom com;

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

Keypad keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  com.init();
  com.print(0, "[[Keypad Test]]");
}

void loop() {
  char key = keypad.getKey();

  if (key) {
    String str(key);
    com.print(1, str);
  }
}
