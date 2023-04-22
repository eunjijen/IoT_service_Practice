# include <Minicom.h>

MiniCom com;

int mSensor = A0;
int ledPin = 11;

void setup() {
  com.init();
  com.print(0, "[[Sound]]");
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int readValue = analogRead(mSensor);
  int lightValue = readValue / 4;

  Serial.print("Read Value = ");
  Serial.println(readValue);
  Serial.print("Light Value = ");
  Serial.println(lightValue);
  
  analogWrite(ledPin, lightValue);
  com.print(1, "R:", readValue, "L:", lightValue);
  delay(200);
}
