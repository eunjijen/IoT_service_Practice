# include <Minicom.h>
# include <Analog.h>
# include <PWMLed.h>

MiniCom com;
Analog cds(A0, 0, 255);
PWMLed led(9);

void check() {
  int value = cds.read();
  if(value > 100) {

    led.setValue(value);
  } else {
    led.off();
  }
  com.print(1, "Illu: ", value);
}

void setup() {
  // put your setup code here, to run once:
  com.init();
  com.setInterval(100, check);
  com.print(0, "[[CDS Test]]");
}

void loop() {
  // put your main code here, to run repeatedly:
  com.run();
}
