#include <SoftwareSerial.h>
 #include<string.h>
 
 int pump=13;   //pin for contrlling water pump
 int LED=12;    //pin for controlling LEDs
 int buz=11;    //pin for controlling buzzer
 int TV=10;    //pin for controlling TV
 int d=0;
 
 
 
 void setup() {
     
     pinMode(LED, OUTPUT);      //initialise LED pin as OUTPUT
     pinMode(buz, OUTPUT);      //initialise buzzer pin as OUTPUT
     pinMode(pump, OUTPUT);     //initialise pump pin as OUTPU
     pinMode(TV, OUTPUT);      //initialise Tv pin as OUTPUT
     pinMode(LED, LOW);      //initialise LED pin as OUTPUT
     pinMode(buz, LOW);      //initialise buzzer pin as OUTPUT
     pinMode(pump, LOW);    //initialise pump pin as OUTPUT
     pinMode(LED, LOW);      //initialise LED pin as OUTPUT
     Serial.begin(9600);       //start serial communication with PC
 }
 
 void loop() {
     d=Serial.read();        //read output from PC
    
     if(d == 'p') {         
 
         digitalWrite(LED, HIGH);
         digitalWrite(buz, HIGH);
         digitalWrite(pump, HIGH);
         digitalWrite(TV, HIGH);
         delay(5000);
     
     }
   
     if(d == 's' ) {        //if no fire detected
         
         digitalWrite(LED, LOW); 
         digitalWrite(buz, LOW); 
         digitalWrite(pump, LOW);
         digitalWrite(TV, LOW);
         delay(5);
     }
 }