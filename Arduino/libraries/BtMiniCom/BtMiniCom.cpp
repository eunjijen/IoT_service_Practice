#include "BtMiniCom.h"

BtMiniCom::BtMiniCom(int rx, int tx, btminicom_callback_t callback, 
long serial_bps, int lcd_addr)
  : MiniCom(serial_bps, lcd_addr), btSerial(rx, tx), callback(callback) {
}

void BtMiniCom::init() {
  MiniCom::init(); // 부모 메서드 호출
  btSerial.begin(9600);
}

String BtMiniCom::readLine(){ // \r\n를 제외한 문자열을 리턴
  String message="";

  while(btSerial.available()) { 
    char data = (char)btSerial.read(); 
    message+=data; 
    delay(5); //수신 끊김 방지 ***
  }
  message.trim();
  return message;
}

void BtMiniCom::send(String msg){
  btSerial.println(msg);
}

void BtMiniCom::run(){
  String msg = readLine();

  if(msg != "" && callback != NULL) {
    callback(msg);
  }
  MiniCom::run();
}
