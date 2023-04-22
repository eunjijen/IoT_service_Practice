const int NUM_STEP = 8;

// 4개의 순차점멸(LED 풀업 연결) 배열 이용
const int led_pin[4] = {3, 4, 5, 6}; // LED 연결 핀 번호

// LED 연결핀에 차례로 출력할 출력 값
const int led_out[NUM_STEP][4] = {
  {1, 0, 0, 0}, 
  {1, 1, 0, 0},
  {1, 1, 1, 0},
  {1, 1, 1, 1},
  {1, 1, 1, 0}, 
  {1, 1, 0, 0},
  {1, 0, 0, 0},
  {0, 0, 0, 0}
};

int out_no = 0; // 출력 값 출력 순서 번호(0-3)

void setup() {
  int n;

  for(n = 0;n < 4;n++){ 
    pinMode(led_pin[n], OUTPUT); // led_pin[n]번핀 출력 설정
    digitalWrite(led_pin[n], LOW); // led_pin[n]번핀 LOW 출력
  }
}

void loop() {
  int n;

  for(n = 0;n < 4;n++){ 
  // led_pin[n]번핀에 out_no 패턴 출력
    digitalWrite(led_pin[n], led_out[out_no][n]);
  }

  // out_no++; // 다음 출력 패턴 번호 설정
  // if(out_no == 4) out_no = 0; // 마지막 다음은 처음 패턴으로

  out_no = (out_no + 1) % NUM_STEP;

  delay(1000);
}

