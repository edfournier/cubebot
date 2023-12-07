#include <ESP32Servo.h>
#define SERVO1 23
#define SERVO2 18
#define BEAT 800

#define TL 1
#define TU 95

Servo arm; 
Servo table;  

void open() {
  arm.write(20);
  delay(BEAT);
}

void shut() {
  arm.write(80);
  delay(BEAT);
}

void flip() {
  arm.write(170);
  delay(BEAT);
  for (int i = 170; i >= 60; i -= 10) {
      arm.write(i); 
      delay(15);
  }
  delay(BEAT);
  arm.write(80); 
  delay(BEAT);
}

void turn(int angle) {
  table.attach(SERVO2);
  table.write(angle);
  delay(BEAT);
  table.detach();
  delay(BEAT);
}

void right() {
  open();
  turn(TU);
  shut();
  flip(); 
  flip();
  flip();
  open();
  turn(TL);
  shut();
  turn(TU);
  flip();
  open();
  turn(TL);
  shut();
}

void up() {
  flip();
  turn(TU);
  open();
  turn(TL);
  shut();
  flip();
  flip();
  flip();
}

void front() {
  flip();
  flip();
  turn(TU);
  open();
  turn(TL);
  shut();
  flip();
  flip();
}

void right_prime(){
  open();
  turn(TU);
  shut();
  flip();
  flip();
  flip();
  turn(TL);
  open();
  turn(TU);
  shut();
  flip();
  open();
  turn(TL);
  shut();
}

void front_prime(){
  flip();
  flip();
  open();
  turn(TU);
  shut();
  turn(TL);
  flip();
  flip();
}

void up_prime(){
  flip();
  open();
  turn(TU);
  shut();
  turn(TL);
  flip();
  flip();
  flip();
}


void setup() {
  Serial.begin(115200);
  arm.attach(SERVO1);
  arm.write(80); 
  table.attach(SERVO2);
  table.write(2);
  delay(BEAT);
  table.detach();
  delay(3000);
  /*
  right();
  up();
  front();
  front();
  up();
  right();
  up();
  */
  up_prime();
  right_prime();
  front_prime();
}

String moves = "";

void loop() {
  if (moves.length() > 0) {
    for (int i = 0; i < moves.length(); i += 2) {
      Serial.println(moves[i]);
      switch (moves[i]) {
        case 'F':
          front();
          break;
        case 'U':
          up();
          break;
        case 'R':
          right();
          break;
        case 'f':
          front_prime();
          break;
        case 'u':
          up_prime();
          break;
        case 'r':
          right_prime();
          break;
      }

    }
    exit(1);
  }
  else if (Serial.available()) {
    moves = Serial.readString();
  }
}
