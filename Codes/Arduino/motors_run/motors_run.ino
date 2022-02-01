# define dirl1 4
# define dirl2 8
# define dirr1 12
# define dirr2 13

# define pwml1 3
# define pwml2 6
# define pwmr1 9
# define pwmr2 11


void setup() {

  Serial.begin(9600);
  pinMode(dirl1, OUTPUT);
  pinMode(dirl2, OUTPUT);
  pinMode(dirr1, OUTPUT);
  pinMode(dirr2, OUTPUT);
  pinMode(pwml1, OUTPUT);
  pinMode(pwml2, OUTPUT);
  pinMode(pwmr1, OUTPUT);
  pinMode(pwmr2, OUTPUT);
  
  
}

int speedy = 50;
int speedn = 0;

void loop() {

  if(Serial.available()>=0){
    /*
    digitalWrite(dirl1, LOW);
    digitalWrite(dirl2, LOW);
    digitalWrite(dirr1, LOW);
    digitalWrite(dirr2, LOW);
    analogWrite(pwml1, speedy);
    analogWrite(pwml2, speedy);
    analogWrite(pwmr1, speedy);
    analogWrite(pwmr2, speedy);
    
    delay(500);
    
    Serial.print("Motors are running with a speed of : ");
    Serial.print(speedy);
    Serial.println(" pwm");
    */
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
  }
}

void forward() {
    digitalWrite(dirr1, HIGH);
    digitalWrite(dirr2, HIGH);
    digitalWrite(dirl1, HIGH);
    digitalWrite(dirl2, HIGH);
    analogWrite(pwmr1, speedy);
    analogWrite(pwmr2, speedy);
    analogWrite(pwml1, speedy);
    analogWrite(pwml2, speedy);
    Serial.println("FORWARD");
}

void reverse() {
    digitalWrite(dirr1, LOW);
    digitalWrite(dirr2, LOW);
    digitalWrite(dirl1, LOW);
    digitalWrite(dirl2, LOW);
    analogWrite(pwmr1, speedy);
    analogWrite(pwmr2, speedy);
    analogWrite(pwml1, speedy);
    analogWrite(pwml1, speedy);
    Serial.println("REVERSE");  
}

void left() {
    digitalWrite(dirr1, HIGH);
    digitalWrite(dirr2, LOW);
    digitalWrite(dirl1, LOW);
    digitalWrite(dirl2, HIGH);
    analogWrite(pwmr1, speedy);
    analogWrite(pwmr2, speedy);
    analogWrite(pwml1, speedy);
    analogWrite(pwml1, speedy);
    Serial.println("LEFT");
}

void right() {
    digitalWrite(dirr1, LOW);
    digitalWrite(dirr2, HIGH);
    digitalWrite(dirl1, HIGH);
    digitalWrite(dirl2, LOW);
    analogWrite(pwmr1, speedy);
    analogWrite(pwmr2, speedy);
    analogWrite(pwml1, speedy);
    analogWrite(pwml1, speedy);
    Serial.println("RIGHT");
}
