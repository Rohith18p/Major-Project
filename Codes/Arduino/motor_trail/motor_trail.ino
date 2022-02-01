# define dirl1 8

# define pwml1 9

void setup() {

  Serial.begin(9600);
  pinMode(dirl1, OUTPUT);
  pinMode(pwml1, OUTPUT);  
}

int speedy = 50;
int speedn = 0;

void loop() {

  if(Serial.available()>=0){
  
    digitalWrite(dirl1, HIGH);
    analogWrite(pwml1, speedy);
    delay(500);
    
    Serial.print("Motors are running with a speed of : ");
    Serial.print(speedy);
    Serial.println(" pwm");

    /*
    char a = Serial.read();

    if(a == '8'){
      forward();
      delay(2000);
    }
    else if(a == '2'){
      reverse();
      delay(2000);
    }
    else if(a == '4'){
      left();
      delay(2000);
    }
    else if(a == '6'){
      right();
      delay(2000);
    }
    */
  }
}

/*
void forward() {
    digitalWrite(dirr1, HIGH);
    digitalWrite(dirr2, HIGH);
    digitalWrite(dirl1, HIGH);
    digitalWrite(dirl2, HIGH);
    analogWrite(pwmr1, speed);
    analogWrite(pwmr2, speed);
    analogWrite(pwml1, speed);
    analogWrite(pwml1, speed);
    Serial.println("FORWARD");
}

void reverse() {
    digitalWrite(dirr1, LOW);
    digitalWrite(dirr2, LOW);
    digitalWrite(dirl1, LOW);
    digitalWrite(dirl2, LOW);
    analogWrite(pwmr1, speed);
    analogWrite(pwmr2, speed);
    analogWrite(pwml1, speed);
    analogWrite(pwml1, speed);
    Serial.println("REVERSE");  
}

void left() {
    digitalWrite(dirr1, HIGH);
    digitalWrite(dirr2, HIGH);
    digitalWrite(dirl1, LOW);
    digitalWrite(dirl2, LOW);
    analogWrite(pwmr1, speed);
    analogWrite(pwmr2, speed);
    analogWrite(pwml1, speed);
    analogWrite(pwml1, speed);
    Serial.println("LEFT");
}

void right() {
    digitalWrite(dirr1, HIGH);
    digitalWrite(dirr2, HIGH);
    digitalWrite(dirl1, LOW);
    digitalWrite(dirl2, LOW);
    analogWrite(pwmr1, speed);
    analogWrite(pwmr2, speed);
    analogWrite(pwml1, speed);
    analogWrite(pwml1, speed);
    Serial.println("RIGHT");
}
*/
