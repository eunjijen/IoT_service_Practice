const int buzzer_pin = 9; // 부저 연결핀

void setup() 
{
  pinMode(buzzer_pin, OUTPUT); // 부저 연결핀 출력 설정
}

void loop() 
{
  digitalWrite(buzzer_pin, HIGH);
  delay(2000);
  digitalWrite(buzzer_pin, LOW);
  delay(2000);
}
