#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

String ssid = "Rohith's Realme";
String password = "love9audi";

ESP8266WebServer server(80);

#define dirl1 D1
#define dirl2 D2
#define dirr1 D3
#define dirr2 D4

#define pwml1 D5
#define pwml2 D6
#define pwmr1 D7
#define pwmr2 D8

int val;
int speedy = 200;
int speedn = 0;

void setup() {
  Serial.begin(115200);
  
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.println(" ");
  WiFi.begin(ssid, password);
  while(WiFi.status()!=WL_CONNECTED){
    Serial.print(".");
    delay(500);
  }
  Serial.println("/n Connected to: ");
  Serial.println(WiFi.localIP());

  server.on("/forward", forward);
  server.on("/backward", backward);
  server.on("/left", left);
  server.on("/right", right);
  server.on("/halt", halt);
  
  server.begin();
  
}

void loop() {
  server.handleClient();
 
}

void forward(){
  digitalWrite(dirl1, HIGH);
  digitalWrite(dirl2, HIGH);
  digitalWrite(dirr1, HIGH);
  digitalWrite(dirr2, HIGH);

  analogWrite(pwml1, speedy);
  analogWrite(pwml2, speedy);
  analogWrite(pwmr1, speedy);
  analogWrite(pwmr2, speedy);
  
  server.send(200);
  Serial.println("forward");
}

void backward(){
  digitalWrite(dirl1, LOW);
  digitalWrite(dirl2, LOW);
  digitalWrite(dirr1, LOW);
  digitalWrite(dirr2, LOW);

  analogWrite(pwml1, speedy);
  analogWrite(pwml2, speedy);
  analogWrite(pwmr1, speedy);
  analogWrite(pwmr2, speedy);
  
  server.send(200);
  Serial.println("backward");
}

void left(){
  digitalWrite(dirl1, HIGH);
  digitalWrite(dirl2, LOW);
  digitalWrite(dirr1, LOW);
  digitalWrite(dirr2, HIGH);

  analogWrite(pwml1, speedy);
  analogWrite(pwml2, speedy);
  analogWrite(pwmr1, speedy);
  analogWrite(pwmr2, speedy);
  
  server.send(200);
  Serial.println("left");
}

void right(){
  digitalWrite(dirl1, LOW);
  digitalWrite(dirl2, HIGH);
  digitalWrite(dirr1, HIGH);
  digitalWrite(dirr2, LOW);

  analogWrite(pwml1, speedy);
  analogWrite(pwml2, speedy);
  analogWrite(pwmr1, speedy);
  analogWrite(pwmr2, speedy);
  
  server.send(200);
  Serial.println("right");
}

void halt(){
  digitalWrite(dirl1, LOW);
  digitalWrite(dirl2, HIGH);
  digitalWrite(dirr1, HIGH);
  digitalWrite(dirr2, LOW);

  analogWrite(pwml1, speedn);
  analogWrite(pwml2, speedn);
  analogWrite(pwmr1, speedn);
  analogWrite(pwmr2, speedn);
  
  server.send(200);
  Serial.println("halt");
}
