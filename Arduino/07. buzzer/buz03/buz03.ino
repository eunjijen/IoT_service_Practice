#include <Melody.h>
#include "pirates.h" 

Melody melody(9, notes, durations, length);

void setup() {
  melody.play();
}

void loop() {
  melody.run();
}
