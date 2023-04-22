# include <Minicom.h>
# include <DHT.h>

MiniCom com;
DHT dht11(12, DHT11); 

void check() {
  float fh, fc, ff;

  // DHT11 온습도 센서 읽기
  fh = dht11.readHumidity();
  fc = dht11.readTemperature();
  ff = dht11.readTemperature(true);

  if(isnan(fh) || isnan(fc) || isnan(ff)) {
    com.print(1, "Failed!!");
    return;
  }
  com.print(1, "T:", fc, " H:", fh);
}

void setup() {
  // put your setup code here, to run once:
  com.init();
  com.setInterval(2000, check);
  dht11.begin();
  com.print(0, "[[DHT11]]");
  com.print(1, "Preparing DHT11");
}

void loop() {
  // put your main code here, to run repeatedly:
  com.run();
}
