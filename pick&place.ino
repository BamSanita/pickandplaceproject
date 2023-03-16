#include <Stepper.h>
const int stepsPerRevolution1 = 180;
const int stepsPerRevolution2 = 140;
Stepper myStepper1 = Stepper(stepsPerRevolution1, 22, 26, 24, 28);
Stepper myStepper2 = Stepper(stepsPerRevolution2, 7, 51, 8, 53);
#define pinzccw 10
#define pinzcw 11
#define pinyccw 9
#define pinycw 6
#define pinxccw 5
#define pinxcw 3
#define relaymotor 49
#define reedx 35
#define reedy 31
#define reedz 33
#define reedxx 37
#define reedyy 39
#define stepPin 45 
#define dirPin 43 
#define enPin 41
int datareedx;
int datareedy;
int datareedz;
int datareedxx;
int datareedyy;
void setup()
{
  pinMode(pinyccw, OUTPUT);
  pinMode(pinycw, OUTPUT);
  pinMode(pinzccw, OUTPUT);
  pinMode(pinzcw, OUTPUT);
  pinMode(pinxccw, OUTPUT);
  pinMode(pinxcw, OUTPUT);
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
  pinMode(enPin,OUTPUT);
  digitalWrite(enPin,LOW);
  pinMode(relaymotor, OUTPUT);
  pinMode(reedx, INPUT_PULLUP);
  pinMode(reedz, INPUT_PULLUP);
  pinMode(reedy, INPUT_PULLUP);
  pinMode(reedxx, INPUT_PULLUP);
  pinMode(reedyy, INPUT_PULLUP);

  Serial.begin(115200);
  Serial.setTimeout(50);
}

void loop()
{     
      if(Serial.available()>0){
      char a = Serial.read();
      if(a == 'r'){
      String b = Serial.readString();
      float i =0.0;
      float n = b.toFloat();
      for(int i = n; i >=0; i--) {
          digitalWrite(dirPin,HIGH);
          digitalWrite(stepPin,HIGH);  
          delayMicroseconds(200); 
          digitalWrite(stepPin,LOW); 
          delayMicroseconds(200); 
        }
        a =0;
        delay(200); 
                }
      if(a == 't'){
      String b = Serial.readString();
      float i =0.0;
      float n = b.toFloat();
      for(int i = n; i >=0; i--) {
          digitalWrite(dirPin,LOW);
          digitalWrite(stepPin,HIGH); 
          delayMicroseconds(200); 
          digitalWrite(stepPin,LOW); 
          delayMicroseconds(200); 
        }
        a =0;
        delay(200); 
                }
      if(a == 'c'){
      String b = Serial.readString();
      float i =0.0;
      float n = 1315;
      while(n>i){
//        Serial.println(n);
        digitalWrite(pinxcw,1);
        delay(1);
        digitalWrite(pinxcw,0);
        delay(1);
        n-=1.0;
                }
//      Serial.println("o");
      a="x1";
                  }
   
      if(a == 'l'){
          Serial.println("aaa");
        float i =0.0;
        float n = 1.0;
        while(n>i){
          digitalWrite(pinxccw,1);
          delay(1);
          digitalWrite(pinxccw,0);
          delay(1);
          Serial.println(datareedx);
          n+=1.0;
          datareedx = digitalRead(reedx);
          if (datareedx == 0 ){
            n=0.0;
            }
              }
                }

      if(a == 'k'){
          Serial.println("aaa");
        float i =0.0;
        float n = 1.0;
        while(n>i){
          digitalWrite(pinycw,1);
          delay(1);
          digitalWrite(pinycw,0);
          delay(1);
          Serial.println(datareedy);
          n+=1.0;
          datareedy = digitalRead(reedy);
          if (datareedy == 0 ){
            n=0.0;
            }
              }
                }
                  
   if(a == 'q'){
        float i =0.0;
        float n = 1060.0;
        while(n>i){
          digitalWrite(pinzcw,1);
          delay(1);
          digitalWrite(pinzcw,0);
          delay(1);
          n-=1.0;
              }
              n=0.0;
                }
                
    if(a == 'h'){
        float i =0.0;
        float n = 1.0;
        while(n>i){
          digitalWrite(pinzccw,1);
          delay(1);
          digitalWrite(pinzccw,0);
          delay(1);
          n+=1.0;
          datareedz = digitalRead(reedz);
          if (datareedz == 0 ){
            n=0.0;
            }
                }
                }
                
      if(a == 'y'){
      String b = Serial.readString();
      float i =0.0;
      float n = b.toFloat();
      //analogWrite(9,125);
      //delay(100);
      //analogWrite(9,0);
      while(n>i){
//        Serial.println(n);
        digitalWrite(pinyccw,1);
        delay(1);
        digitalWrite(pinyccw,0);
        delay(1);
        n-=1.0;
                }
//     Serial.println("y");
      
      a=0;
                }
      if(a == 'u'){
      String b = Serial.readString();
      float i =0.0;
      float n = b.toFloat();
      while(n>i){
//        Serial.println(n);
        digitalWrite(pinycw,1);
        delay(1);
        digitalWrite(pinycw,0);
        delay(1);
        n-=1.0;
                }
      Serial.println("u");
      a="y1";
                }
     if(a == 'z'){
      String b = Serial.readString();
      float i =0.0;
      float n = b.toFloat();
      //analogWrite(9,125);
      //delay(100);
      //analogWrite(9,0);
      while(n>i){
//        Serial.println(n);
        digitalWrite(pinzccw,1);
        delay(1);
        digitalWrite(pinzccw,0);
        delay(1);
        n-=1.0;
                }
     
      Serial.println(digitalRead(reedyy));
      a=0;
                }
      if(a == 'i'){
      String b = Serial.readString();
      float i =0.0;
      float n = b.toFloat();
      //analogWrite(9,125);
      //delay(100);
      //analogWrite(9,0);
      while(n>i){
//        Serial.println(n);
        digitalWrite(pinzcw,1);
        delay(1);
        digitalWrite(pinzcw,0);
        delay(1);
        n-=1.0;
                }
      Serial.println(digitalRead(reedxx));
      a="z1";
                }
    if(a == 'x'){
      String b = Serial.readString();
      float i =0.0;
      float n = b.toFloat();
      while(n>i){
//          }
        digitalWrite(pinxccw,1);
        delay(1);
        digitalWrite(pinxccw,0);
        delay(1);
        n-=1.0;
                }
     
      Serial.println(digitalRead(reedx));
      a=0;
                }
      if(a == 'o'){
      String b = Serial.readString();
      float i =0.0;
      float n = b.toFloat();
      //analogWrite(9,125);
      //delay(100);
      //analogWrite(9,0);
      while(n>i){
//        Serial.println(n);
        digitalWrite(pinxcw,1);
        delay(1);
        digitalWrite(pinxcw,0);
        delay(1);
        n-=1.0;
                }
//      Serial.println("o");
      a="x1";
                }
      if(a == 'a'){
    digitalWrite(relaymotor,1);
    }
      if(a == 'd'){
    digitalWrite(relaymotor,0);
    }

   datareedx = digitalRead(reedx);
   if(datareedx == 0){
      float i =0.0;
      float n = 1030;
      while(n>i){
        digitalWrite(pinxcw,1);
        delay(1);
        digitalWrite(pinxcw,0);
        delay(1);
        n-=1.0;
                }
      a="x1";
      Serial.println(datareedx);
    
    }
    datareedy = digitalRead(reedy);
//    Serial.println(datareedy);
    if(datareedy == 0){
      Serial.println("2");
      float i =0.0;
      float n = 1370;
      while(n>i){
        digitalWrite(pinyccw,1);
        delay(1);
        digitalWrite(pinyccw,0);
        delay(1);
        n-=1.0;
                }
                n=0.0;
      
      
      }
   if(a == 'v'){
    datareedxx = digitalRead(reedxx);
//   Serial.println(datareedxx);
   if(datareedxx == 0){
      float i =0.0;
      float n = 500;
      while(n>i){
        digitalWrite(pinzcw,1);
        delay(1);
        digitalWrite(pinzcw,0);
        delay(1);
        n-=1.0;
                }
//      a=0;
//      Serial.println(datareedxx);
                     }
        a=0;
                }
   if(a == 's'){
   datareedyy = digitalRead(reedyy);
//   Serial.println(datareedx);
   if(datareedyy == 0){  
      float i =0.0;
      float n = 45;
      while(n>i){
        digitalWrite(pinycw,1);
        delay(1);
        digitalWrite(pinycw,0);
        delay(1);
        n-=1.0;
                 }
                     }
    a=0;
              }
    if(a == 'b'){
   datareedyy = digitalRead(reedyy);
//   Serial.println(datareedx);
   if(datareedyy == 0){  
      float i =0.0;
      float n = 500;
      while(n>i){
        digitalWrite(pinzccw,1);
        delay(1);
        digitalWrite(pinzccw,0);
        delay(1);
        n-=1.0;
                }
                     }
      a=0;
              }
     if(a == 'n'){
   datareedyy = digitalRead(reedyy);
//   Serial.println(datareedx);
   if(datareedyy == 1){  
      float i =0.0;
      float n = 45;
      while(n>i){
        digitalWrite(pinyccw,1);
        delay(1);
        digitalWrite(pinyccw,0);
        delay(1);
        n-=1.0;
                }
                     }
      a=0;
              }
     if(a == 'm'){
        myStepper1.setSpeed(50);
        myStepper1.step(stepsPerRevolution1);
        a=0;
                  }
     if(a == 'j'){
   datareedyy = digitalRead(reedyy);
//   Serial.println(datareedx);
   if(datareedyy == 1){  
      float i =0.0;
      float n = 500;
      while(n>i){
        digitalWrite(pinzcw,1);
        delay(1);
        digitalWrite(pinzcw,0);
        delay(1);
        n-=1.0;
                }
                     }
      a=0;
              }
     if(a == 'g'){
   datareedyy = digitalRead(reedyy);
//   Serial.println(datareedx);
   if(datareedyy == 0){  
      float i =0.0;
      float n = 500;
      while(n>i){
        digitalWrite(pinzccw,1);
        delay(1);
        digitalWrite(pinzccw,0);
        delay(1);
        n-=1.0;
                }
                     }
     a=0;
              }
     if(a == 'f'){
   datareedyy = digitalRead(reedyy);
//   Serial.println(datareedx);
   if(datareedyy == 1){  
      float i =0.0;
      float n = 1315;
      while(n>i){
        digitalWrite(pinxccw,1);
        delay(1);
        digitalWrite(pinxccw,0);
        delay(1);
        n-=1.0;
                }
                     }
     a=0;
              }

              
   if(a == 'w'){
      String b = Serial.readString();
      float i =0.0;
      float n = 1315;
      while(n>i){
//        Serial.println(n);
        digitalWrite(pinxcw,1);
        delay(1);
        digitalWrite(pinxcw,0);
        delay(1);
        n-=1.0;
                }
//      Serial.println("o");
      a="x1";
                  }
    if(a == 'e'){
      datareedxx = digitalRead(reedxx);
          if (datareedxx == 0 ){
            float i =0.0;
            float n = 215.0;
            while(n>i){
            digitalWrite(pinxccw,1);
            delay(1);
            digitalWrite(pinxccw,0);
            delay(1);
            n-=1.0;
                      }      
                               }
       a=0;
                }
    if(a == 'p'){
      datareedxx = digitalRead(reedxx);
          if (datareedxx == 1 ){
            float i =0.0;
            float n = 500.0;
            while(n>i){
            digitalWrite(pinzcw,1);
            delay(1);
            digitalWrite(pinzcw,0);
            delay(1);
            n-=1.0;
                      }      
                               }
      a=0;
                }
      if(a == '1'){
      datareedyy = digitalRead(reedyy);
      if(datareedyy == 0){
            float i =0.0;
            float n = 45.0;
            while(n>i){
            digitalWrite(pinycw,1);
            delay(1);
            digitalWrite(pinycw,0);
            delay(1);
              n-=1.0;
                      }      
                               }
              a=0;
                }
     if(a == '2'){
      datareedyy = digitalRead(reedyy);
      if(datareedyy == 0){
            float i =0.0;
            float n = 500.0;
            while(n>i){
            digitalWrite(pinzccw,1);
            delay(1);
            digitalWrite(pinzccw,0);
            delay(1);
              n-=1.0;
                      }      
                               }
              a=0;
                }
      if(a == '3'){
      datareedyy = digitalRead(reedyy);
      if(datareedyy == 1){
            float i =0.0;
            float n = 45.0;
            while(n>i){
            digitalWrite(pinyccw,1);
            delay(1);
            digitalWrite(pinyccw,0);
            delay(1);
              n-=1.0;
                      }      
                               }
              a=0;
                }
      if(a == '4'){
        myStepper2.setSpeed(50);
        myStepper2.step(-stepsPerRevolution2);
              a=0;
                }
      if(a == '5'){
      datareedyy = digitalRead(reedyy);
      if(datareedyy == 1){
            float i =0.0;
            float n = 500.0;
            while(n>i){
            digitalWrite(pinzcw,1);
            delay(1);
            digitalWrite(pinzcw,0);
            delay(1);
              n-=1.0;
                      }      
                         }
              a=0;
                }
      if(a == '6'){
      datareedyy = digitalRead(reedyy);
      if(datareedyy == 0){
            float i =0.0;
            float n = 500.0;
            while(n>i){
            digitalWrite(pinzccw,1);
            delay(1);
            digitalWrite(pinzccw,0);
            delay(1);
              n-=1.0;
                      }      
                         }
              a=0;
                }
       if(a == '7'){
      datareedyy = digitalRead(reedyy);
      if(datareedyy == 1){
            float i =0.0;
            float n = 1100.0;
            while(n>i){
            digitalWrite(pinxccw,1);
            delay(1);
            digitalWrite(pinxccw,0);
            delay(1);
              n-=1.0;
                      }      
                         }
              a=0;
                }
      
}
}
