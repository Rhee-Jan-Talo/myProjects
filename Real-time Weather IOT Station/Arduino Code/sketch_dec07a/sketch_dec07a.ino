#include <LiquidCrystal.h>
LiquidCrystal lcd(2, 3, 4, 5, 6, 7); 
int tempC;
int tempF;


void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(10, INPUT);
  pinMode(9, INPUT);
  pinMode(8, INPUT);
}

void loop() {
  
  pinLoop(); 
  int temp = analogRead(A0);
  int waterlvl = analogRead(A3);
  int humidity = analogRead(A4);
  int air_p = analogRead(A2);
  int wind_s = analogRead(A1);
  float voltage = temp*5.0;
  tempC = (((voltage-0.5)*100+50)/1000)-1;
  tempF = (tempC*9/5)+32;
  Serial.print(tempC);
  Serial.print(" ");
  Serial.print(waterlvl);
  Serial.print(" ");
  Serial.print(humidity);
  Serial.print(" ");
  Serial.print(air_p);
  Serial.print(" ");
  Serial.print(wind_s);
  Serial.print(" ");
  Serial.println(tempF);
  if (digitalRead(11)==HIGH){
   if(digitalRead(10)==HIGH){
     lcd.clear();
     lcd.setCursor(0,0);
     lcd.print("TEMP in C:");
     lcd.setCursor(0,1);
     lcd.print(tempC);
   }
   else if(digitalRead(9)==HIGH){
     lcd.clear();
     lcd.setCursor(0,0);
     lcd.print("HUMIDITY:");
     lcd.setCursor(0,1);
     lcd.print(humidity);  
   }
   else if(digitalRead(8)==HIGH){
     lcd.clear();
     lcd.setCursor(0,0);
     lcd.print("WIND SPEED:");
     lcd.setCursor(0,1);
     lcd.print(wind_s);  
   }
  }
  else if(digitalRead(12)==HIGH){ 
   if(digitalRead(10)==HIGH){
     lcd.clear();
     lcd.setCursor(0,0);
     lcd.print("TEMP in F:");
     lcd.setCursor(0,1);
     lcd.print(tempF);
   }
   else if(digitalRead(9)==HIGH){
     lcd.clear();
     lcd.setCursor(0,0);
     lcd.print("AIR PRESSURE:");
     lcd.setCursor(0,1);
     lcd.print(air_p);  
   }
   else if(digitalRead(8)==HIGH){
     lcd.clear();
     lcd.setCursor(0,0);
     lcd.print("WATER LEVEL:");  
     lcd.setCursor(0,1);
     lcd.print(waterlvl);  
   }
  }
}


//  FUNCITONS
void pinLoop(){
  int num = rand() % 2 + 1;
  if(num==1){
    loop2();
  }
  else{
    loop1();
  }
}
void loop1(){
  digitalWrite(12, LOW);
  digitalWrite(11, HIGH);
  delay(50);
  digitalWrite(12, HIGH);
  digitalWrite(11, LOW);
  delay(50);
  }
void loop2(){
  digitalWrite(11, LOW);
  digitalWrite(12, HIGH);
  delay(50);
  digitalWrite(11, HIGH);
  digitalWrite(12, LOW);
  delay(50);
  }

  
void temp_C(){
}
void temp_F(){
}
void wat_lvl(){
}
void humid(){
}
void air_p(){
}
void wind_s(){
}
