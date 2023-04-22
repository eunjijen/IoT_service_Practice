const int var_pin = A0;
int analog_val;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int digital_val;
  float ff;

  digital_val = analogRead(var_pin);
  digital_val = map(digital_val, 0, 1023, 1023, 0);

  Serial.print("Input Voltage(0~5V) = ");
  Serial.println(ff);

  Serial.print("Digital Value(0~1023) = ");
  Serial.println(digital_val);
  Serial.println("-------------------------------------------");

  delay(1000);
}
