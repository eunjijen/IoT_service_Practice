char soundInputPin = A0;
char ledLevel[8] = { 2, 3, 4, 5, 6, 7, 8, 9};


void setup() {
  // put your setup code here, to run once:
  for(int i=0; i<=7; i++) {
    pinMode(ledLevel[i], OUTPUT);
  }
}

void loop() {
  int soundInput = analogRead(soundInputPin);
  int soundLevel = map(soundInput, 50, 900, 0, 7);
  for(int i=0; i<=7; i++) {
    digitalWrite(ledLevel[i], LOW);
  }
  for(int i=0; i<=soundLevel; i++) {
    digitalWrite(ledLevel[i], HIGH);
  }

}
