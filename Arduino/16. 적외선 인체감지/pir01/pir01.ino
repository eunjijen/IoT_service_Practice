# include <Minicom.h>
# include <Led.h>

MiniCom com;
Led led(8);
int pir_pin = 7;
int pirState = LOW;
int val = 0;


void setup() {
  // put your setup code here, to run once:
  com.init();
  com.print(0, "[[Motion]]");
  pinMode(pir_pin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  com.run();
  val = digitalRead(pir_pin);
  if(val == HIGH) {
    if(pirState == LOW) {
      com.print(1, "Motion detected!");
      pirState = HIGH;
    }
  } else {
    if(pirState == HIGH) {
      com.print(1, "Motion ended!");
      pirState = LOW;
    }
  }
  led.setValue(val);
}
