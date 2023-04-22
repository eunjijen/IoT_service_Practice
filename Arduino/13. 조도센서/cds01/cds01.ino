# include <Minicom.h>
# include <Analog.h>

MiniCom com;
Analog cds(A0, 0, 100);

void check() {
  int value = cds.read();
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
